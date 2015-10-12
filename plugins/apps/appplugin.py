from collections import namedtuple

from yapsy.IPlugin import IPlugin


class AppPlugin(IPlugin):
    """
    An App is a plugin that contains at least one model, view, and controller
    class. The app entry point receives a reference to the pyglet window and
    event loop that handles the lifecycle of all applications.
    """
    def __init__(self):
        super(AppPlugin, self).__init__()
        self.models = []
        self.views = []
        self.canvases = []

    def activate(self):
        """
        Called by the plugin manager when activating the plugin
        """
        pass

    def deactivate(self):
        """
        Called by the plugin manager when deactivating the plugin
        """
        pass

    def register(self, window):
        """
        The register method is where the models and views should be
        instantiated.
        """
        return NotImplementedError

    def process_command(self, command):
        pass
