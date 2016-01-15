import logging

import pyglet

import core.event as event


class PygletWindow(pyglet.window.Window):
    key_event = event.Event()

    def __init__(self, plugin_manager, fullscreen=False, show_fps=True,
                 vsync=False, width=None, height=None):
        super(PygletWindow, self).__init__(fullscreen=fullscreen, vsync=vsync,
                                           width=width, height=height)
        self.plugin_manager = plugin_manager
        self.active_apps = set([])
        self.active_decoders = set([])
        self.active_daq = None

        self.fps = lambda *args: None
        if show_fps:
            self.fps = pyglet.clock.ClockDisplay().draw

        self.set_exclusive_mouse(True)
        self.set_mouse_visible(False)

        pyglet.clock.schedule(self.poll_and_decode)

        @self.event
        def on_key_press(symbol, modifiers):
            command = PygletKeyboardCommand(symbol, modifiers)
            # self.key_event()
            if command.stop:
                return self.handle_stop_request()
            for app in self.active_apps:
                app.process_command(command)
            # if self.active_controller and (command.decision or command.selection):
            #     self.active_controller.keyboard_input(command)

        @self.event
        def on_mouse_motion(x, y, dx, dy):
            command = Command()
            command.decision = (dx / self.width, dy / self.height)
            for app in self.active_apps:
                app.process_command(command)

        @self.event
        def on_close():
            pass

        @self.event
        def on_draw():
            self.render()

    def render(self):
        self.clear()
        for app in self.active_apps:
            for canvas in app.canvases:
                canvas.batch.draw()
            for view in app.views:
                view.render()
        self.fps()

    def poll_and_decode(self, dt):
        samples = self.active_daq.get_data(1)
        command = Command(data=samples)
        for decoder in self.active_decoders:
            command = decoder.process_data(command)
        for app in self.active_apps:
            app.process_command(command)

    def _initialize_plugins(self, conf):
        if conf['DAQ'] is not None:
            daq = self.plugin_manager.activatePluginByName(conf['DAQ'], 'DAQ')
            if daq is not None:
                self.active_daq = daq

        if conf['Decoder'] is not None:
            decoder = self.plugin_manager.activatePluginByName(conf['Decoder'],
                                                               'Decoder')
            if decoder is not None:
                self.active_decoders.add(decoder)

        if conf['App'] is not None:
            app = self.plugin_manager.activatePluginByName(conf['App'], 'App')
            if app is not None:
                app.register(self)
                self.active_apps.add(app)

    def handle_stop_request(self):
        for plugin in self.plugin_manager.getPluginsOfCategory('App'):
            self.plugin_manager.deactivatePluginByName(plugin.name)
        for plugin in self.plugin_manager.getPluginsOfCategory('DAQ'):
            self.plugin_manager.deactivatePluginByName(plugin.name)
        pyglet.app.exit()

    def activate_app(self, app_name):
        app = self.plugin_manager.getPluginByName(app_name, 'App')
        if app is not None:
            self.active_apps.add(app.plugin_object)

    def deactivate_app(self, app_name):
        app = self.plugin_manager.getPluginByName(app_name, 'App')
        if app is not None:
            self.active_apps.remove(app.plugin_object)

    def start_with(self, conf):
        self._initialize_plugins(conf)
        pyglet.app.run()

    def get_app_canvas(self, size=None, offset=(0, 0)):
        batch = pyglet.graphics.Batch()
        background = pyglet.graphics.OrderedGroup(0)
        foreground = pyglet.graphics.OrderedGroup(1)
        if size is None:
            size = self.width, self.height
        return Canvas(batch, background, foreground, size[0], size[1],
                      offset[0], offset[1])


class Canvas(object):
    def __init__(self, batch, background, foreground, width, height,
                 xoffset=0, yoffset=0):
        self.batch = batch
        self.background = background
        self.foreground = foreground
        self.width = width
        self.height = height
        self.x = xoffset
        self.y = yoffset

    def center(self):
        xc = self.width / 2 + self.x
        yc = self.height / 2 + self.y
        return xc, yc


class Command(object):
    def __init__(self, delta=None, decision=None, selection=None, data=None, json=False):
        super(Command, self).__init__()
        self.delta = delta
        self.decision = decision
        self.selection = selection
        self.predicted_decision = None
        self.predicted_decision_confidence = None
        self.data = data
        self.json = json
        self.ready = True
        self.stop = False

    def is_valid(self):
        return False

    def set_ready_value(self, ready_value):
        self.ready = ready_value

    def is_ready(self):
        return self.ready

    # @staticmethod
    # def serialize(command):
    #     if command.json:
    #         ret = json.dumps(command)
    #     else:
    #         ret = pickle.dumps(command)
    #     return ret
    #
    # @staticmethod
    # def deserialize(serialized_command, json=False):
    #     if json:
    #         ret = json.loads(serialized_command)
    #     else:
    #         ret = pickle.loads(serialized_command)
    #     return ret


class PygletKeyboardCommand(Command):
    def __init__(self, symbol, modifiers):
        super(PygletKeyboardCommand, self).__init__()
        self.stop = False
        labels = [ord(c) for c in 'abcdefghijklmnopqrstuvwxyz_12345']
        if symbol == pyglet.window.key.UP:
            self.decision = 1
            logging.log(logging.INFO, 'Received UP key press')
        elif symbol == pyglet.window.key.DOWN:
            self.decision = 2
            logging.log(logging.INFO, 'Received DOWN key press')
        elif symbol == pyglet.window.key.LEFT:
            self.decision = 3
            logging.log(logging.INFO, 'Received LEFT key press')
        elif symbol == pyglet.window.key.RIGHT:
            self.decision = 4
            logging.log(logging.INFO, 'Received RIGHT key press')
        elif symbol == pyglet.window.key.SPACE:
            self.selection = 1
            logging.log(logging.INFO, 'Received SPACE key press')
        elif symbol == pyglet.window.key.ESCAPE:
            self.stop = True
        elif symbol in labels:
            self.decision = labels.index(symbol) + 1
