__author__ = 'Graham Voysey'
from plugins.drivers.idaqplugin import IDAQPlugin


class FileSignal(IDAQPlugin):
    def name(self):
        return "File Signal"

