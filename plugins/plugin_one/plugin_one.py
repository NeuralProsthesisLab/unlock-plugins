__author__ = 'Graham Voysey'
from plugins.plugin_one.itestplugin import ITestPlugin


class PluginOne(ITestPlugin):
    def print_name(self):
        print("This is a test plugin!")

    def print_status(self):
        print("hello, world!")
