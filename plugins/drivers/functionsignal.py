import numpy as np

from plugins.drivers.daqplugin import DAQPlugin


class FunctionSignal(DAQPlugin):
    def __init__(self):
        super(FunctionSignal, self).__init__()
        self.n_channels = 4
        self.t = 0

        def cycle(t):
            if t % 30 == 0:
                return np.random.choice([1, 2, 3, 4, 5])
            else:
                return 0

        def random(t):
            return np.random.random(self.n_channels)

        self.fn = random  # cycle

    def acquire(self):
        return 1

    def get_data(self, samples):
        buffer = np.zeros((self.n_channels, samples))
        for i in range(samples):
            buffer[:, i] = self.fn(self.t)
            self.t += 1
        return buffer
