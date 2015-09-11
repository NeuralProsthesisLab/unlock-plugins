__author__ = 'Graham Voysey'
from plugins.apps.appplugin import AppPlugin
from pyglet import graphics
from core import pyglet_window, unlockmodels,pyglet_text

import logging

class HelloWorld(AppPlugin):

    def __init__(self):
        self.isConfigured = False
        self.window = None
        self.model = None

    def configure(self):
        #define model
        self.model = unlockmodels.UnlockModel(True)
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
        self.window.start()
        logging.log(logging.INFO, "Hello World execution complete ...")
