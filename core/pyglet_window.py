__author__ = 'Graham Voysey'
import pyglet
import logging

class PygletWindow(pyglet.window.Window):
    def __init__(self, signal, fullscreen=False, show_fps=True, vsync=False):
        super(PygletWindow, self).__init__(fullscreen=fullscreen, vsync=vsync)
        self.signal = signal
        self.controller_stack = []
        self.views = []
        self.batches = set([])
        if show_fps:
            self.fps = pyglet.clock.ClockDisplay().draw
        else:
            def empty():
                pass

            self.fps = empty
        self.active_controller = None

        @self.event
        def on_key_press(symbol, modifiers):
            command = PygletKeyboardCommand(symbol, modifiers)
            if command.stop:
                return self.handle_stop_request()
            if self.active_controller and (command.decision or command.selection):
                self.active_controller.keyboard_input(command)

        @self.event
        def on_close():
            pass

        @self.event
        def on_draw():
            self.render()


    def render(self):
        self.clear()
        for batch in self.batches:
            if batch:
                batch.draw()
        for view in self.views:
            view.render()
        self.fps()

    def handle_stop_request(self):
        if self.active_controller:
            stop = self.active_controller.deactivate()
            if stop:
                self.signal.stop()
                self.signal.close()
                pyglet.app.exit()
            return pyglet.event.EVENT_HANDLED
        else:
            if self.signal is not None:
                self.signal.stop()
                self.signal.close()
            pyglet.app.exit()

    def activate_controller(self, controller):
        if self.active_controller:
            self.controller_stack.append(self.active_controller)
            pyglet.clock.unschedule(self.active_controller.poll_signal)

        self.views = controller.views
        self.batches = controller.batches
        pyglet.clock.schedule(controller.poll_signal)  # , controller.poll_signal_frequency)
        self.active_controller = controller

    def deactivate_controller(self):
        if self.active_controller:
            self.views = []
            self.batches = set([])
            pyglet.clock.unschedule(self.active_controller.poll_signal)
            self.active_controller = None

        if len(self.controller_stack) > 0:
            controller = self.controller_stack[-1]
            controller.activate()
            self.controller_stack = self.controller_stack[:-1]

    def start(self):
        pyglet.app.run()


class Canvas(object):
    def __init__(self, batch, width, height, xoffset=0, yoffset=0):
        self.batch = batch
        self.width = width
        self.height = height
        self.x = xoffset
        self.y = yoffset

    def center(self):
        return self.xcenter(), self.ycenter()

    def xcenter(self):
        return self.width / 2 + self.x

    def ycenter(self):
        return self.height / 2 + self.y


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

    @staticmethod
    def serialize(command):
        if command.json:
            ret = json.dumps(command)
        else:
            ret = pickle.dumps(command)
        return ret

    @staticmethod
    def deserialize(serialized_command, json=False):
        if json:
            ret = json.loads(serialized_command)
        else:
            ret = pickle.loads(serialized_command)
        return ret


class PygletKeyboardCommand(Command):
    def __init__(self, symbol, modifiers):
        super(PygletKeyboardCommand, self).__init__()
        self.stop = False
        labels = [ord(c) for c in 'abcdefghijklmnopqrstuvwxyz_12345']
        if symbol == pyglet.window.key.UP:
            self.decision = 1
            logging.log(logging.INFO,'Received UP key press')
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
