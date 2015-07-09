__author__ = 'Graham Voysey'
##from plugins.drivers.daqpluginbase import DAQPluginBase
import plugins.drivers as drivers

class LSL(drivers.DAQPluginBase):
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



