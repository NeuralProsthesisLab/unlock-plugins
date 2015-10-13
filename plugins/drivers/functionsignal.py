import numpy as np

from plugins.drivers.daqplugin import DAQPlugin


class FunctionSignal(DAQPlugin):
    def __init__(self):
        super(FunctionSignal, self).__init__()
        self.n_channels = 1
        self.t = 0

        def cycle(t):
            if t % 30 == 0:
                return np.random.choice([1, 2, 3, 4, 5])
            else:
                return 0
        self.fn = cycle

    def acquire(self):
        return 1

    def get_data(self, samples):
        buffer = np.zeros((samples, self.n_channels))
        for i in range(samples):
            buffer[i] = self.fn(self.t)
            self.t += 1
        return buffer
