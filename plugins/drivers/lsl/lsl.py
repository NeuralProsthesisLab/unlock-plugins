__author__ = 'Graham Voysey'
import numpy as np

from plugins.drivers.daqplugin import DAQPlugin
from plugins.drivers.lsl.pylsl import StreamInlet, resolve_stream, resolve_bypred


class LSL(DAQPlugin):
    def name(self):
        return "Lab Streaming Layer"

    def get_data(self):
        chunk, timestamps = self.inlet.pull_chunk()
        return np.array(chunk).T

    def stop(self):
        try:
            self.inlet.close_stream()
        except:
            return False
        return True

    def start(self):
        try:
            self.inlet.open_stream()
        except:
            return False
        return True

    def close(self):
        pass

    def open(self, stream_name="", stream_type=""):
        self.stream_name = stream_name
        self.stream_type = stream_type
        self.n_channels = 5

        self.outlet = None

        self.data = None
        #print("looking for an EEG stream...")

        pred = "name='%s' and type='%s'" % ('NiDaq', 'emg')
        self.streams = resolve_bypred(pred.encode('ascii'))
        self.inlet = StreamInlet(self.streams[0])


