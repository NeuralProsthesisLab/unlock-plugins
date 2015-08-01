__author__ = 'Graham Voysey'
from plugins.plugin_one.itestplugin import ITestPlugin
from core import pyglet_window, pyglet_text, pyglet_sprite, unlockstate
#from pyglet import graphics, app, text, window
import pyglet
import logging


class PluginOne(ITestPlugin):
    def print_status(self):
        print("Plugin registration status: operational!")



    def display(self):
        # start pyglet
        # window = pyglet_window.PygletWindow(signal=None)
        # window.set_fullscreen(fullscreen=True)
        if False:
            batch = graphics.Batch()
            canvas = pyglet_window.Canvas(batch, 200, 200)
            model = unlockstate.UnlockState()
            model.start()
            label = pyglet_text.PygletLabel(model, canvas, "Hello, World", canvas.xcenter(), canvas.ycenter())
            window = pyglet_window.PygletWindow(signal=None)
            window.views.append(label)
            window.canvas = canvas
            label.render()
            window.activate()
            app.run()

        window = pyglet.window.Window()
        label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

        @window.event
        def on_draw():
            window.clear()
            label.draw()

        pyglet.app.run()

        logging.log(logging.INFO, "done!")
        # window.start()
