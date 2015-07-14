__author__ = 'gvoysey'
from yapsy.IPlugin import IPlugin

class ITestPlugin(IPlugin):
    def print_name(self):
        return NotImplementedError