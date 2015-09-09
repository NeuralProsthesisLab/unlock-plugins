__author__ = 'gvoysey'
from yapsy.IPlugin import IPlugin


class TestPlugin(IPlugin):

    def test(self):
        return NotImplementedError