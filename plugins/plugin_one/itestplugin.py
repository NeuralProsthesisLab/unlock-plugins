__author__ = 'gvoysey'
from yapsy.IPlugin import IPlugin


class ITestPlugin(IPlugin):

    def test(self):
        return NotImplementedError