__author__ = 'Graham Voysey'
from plugins.plugin_one.itestplugin import ITestPlugin


class PluginOne(ITestPlugin):

    def print_status(self):
        print("Test plugin status: operational!")