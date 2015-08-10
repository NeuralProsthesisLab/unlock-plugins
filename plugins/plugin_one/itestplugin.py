__author__ = 'gvoysey'
from yapsy.IPlugin import IPlugin


class ITestPlugin(IPlugin):

    def print_status(self):
        return NotImplementedError

    def start(self):
        return NotImplementedError