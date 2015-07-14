__author__ = 'Graham Voysey'
from yapsy.IPlugin import IPlugin

class IAppPlugin(IPlugin):
    """
    Apps consume commands (up, down, left, right) and selections (yes/no) to perform basically arbitrary actions on a pyglet window.
    """
    pass
