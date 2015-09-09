__author__ = 'Graham Voysey'
from plugins.drivers.daqplugin import DAQPlugin


class FileSignal(DAQPlugin):
    def name(self):
        return "File Signal"

