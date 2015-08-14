__author__ = 'Graham Voysey'
from plugins.apps.iappplugin import IAppPlugin
from pyglet import graphics
from core import pyglet_window, unlockstate,pyglet_text

import logging

class HelloWorld(IAppPlugin):

    def __init__(self):
        self.isConfigured = False
        self.window = None
        self.model = None

    def configure(self):
        #define model
        self.model = unlockstate.UnlockState(True)
        #define view
        batch = graphics.Batch()
        canvas = pyglet_window.Canvas(batch, 200, 200)
        #define controller
        self.window = pyglet_window.PygletWindow(signal=None, fullscreen=False)
        appview = pyglet_text.PygletTextLabel(self.model, canvas, 'Hello, world',
                                              x=self.window.width // 2,
                                              y=self.window.height // 2,
                                              )
        #assemble state chain
        self.window.views.append(appview)
        self.isConfigured = True

    def start(self):
        assert self.isConfigured
        # sandbox; just do all the app creation here for now.
        self.window.render()
        self.window.start()
        logging.log(logging.INFO, "Hello World execution complete ...")


