__author__ = 'Graham Voysey'
from yapsy.IPlugin import IPlugin

class AppPlugin(IPlugin):
    """
    Apps consume commands (up, down, left, right) and selections (yes/no) to perform basically arbitrary actions on a pyglet window.
    """
    def start(self):
        return NotImplementedError

    def configure(self):
        return NotImplementedError

    def update(self, command):
        #process command (state)
        return NotImplementedError

    def render(self):
        #in the view (?)
        return NotImplementedError

    def stop(self):
        return NotImplementedError