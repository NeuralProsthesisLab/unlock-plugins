__author__ = 'Graham Voysey'
from yapsy.IPlugin import IPlugin

class PluginOne(IPlugin):

    def print_name(self):
        print("This is plugin 1")
    def print_status(self):
        print("hello, world!")