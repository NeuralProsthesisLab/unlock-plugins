__author__ = 'Graham Voysey'

from plugins.drivers.daqplugin import DAQPlugin

class LSL(DAQPlugin):
    def name(self):
        return "Lab Streaming Layer"

    def get_data(self, samples):
        pass

    def stop(self):
        pass

    def start(self):
        pass

    def close(self):
        pass

    def init(self):
        pass

    def open(self, address):
        pass



