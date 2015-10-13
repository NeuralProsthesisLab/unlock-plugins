import logging

from yapsy.IPlugin import IPlugin


class DAQPlugin(IPlugin):
    """
    DAQ plugins consume raw information from a DAQ card (enobio, mobilab, any
    LSL device, tobii eye tracker, etc.) and emit processed data (as a numpy
    array, probably) to a decoder.
    """
    def activate(self):
        self.open()

    def deactivate(self):
        self.close()

    def open(self):
        print('open')

    def close(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def acquire(self):
        pass

    def get_data(self, samples):
        pass
