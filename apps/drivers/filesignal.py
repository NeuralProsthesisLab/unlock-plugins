__author__ = 'Graham Voysey'
from apps.drivers.daqpluginbase import DAQPluginBase


class FileSignal(DAQPluginBase):
    def name(self):
        return "File Signal"

