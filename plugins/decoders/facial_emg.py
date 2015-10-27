__author__ = 'Graham Voysey'
from core.pyglet_window import Command
from plugins.decoders.decoderplugin import DecoderPlugin
import numpy as np


class FacialEmg(DecoderPlugin):
    def __init__(self, n_electrodes,n_samples):
        self.n_samples = 1000 #gross.
        self.n_electrodes = 5
        self.buffer = np.zeros((self.n_electrodes, self.n_samples))
        self.threshold  = None #really, from training


    def process_data(self, command):

        rms = np.sqrt(np.mean(command.data ** 2, axis=1))

        self.buffer = np.roll(self.buffer, -1, axis=1) # shift the window
        self.buffer[-1] = rms[0:self.n_electrodes]

        activations = np.max(self.buffer, axis=0) > self.thresholds
        if activations[4]: #electrode 4 is "select"
            decision = None
            for key, pattern_value in self.decision_patterns.items():
                if np.array_equal(activations[0:3], pattern_value):
                    decision = key
                    break

            # always clear the window after a selection
            self.buffer = np.zeros((self.window_size, self.channels))

            if decision is not None:
                command.decision = decision

        return command


