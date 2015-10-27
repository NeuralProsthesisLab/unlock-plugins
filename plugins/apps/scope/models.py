import numpy as np

from core import UnlockModel


class TimeScopeModel(UnlockModel):
    def __init__(self, n_channels, fs, duration=2, refresh=0.05):
        super(TimeScopeModel, self).__init__()
        self.n_channels = n_channels
        self.n_samples = duration * fs
        self.refresh = refresh * fs
        self.elapsed = 0
        self.cursor = 0
        self.traces = np.zeros((self.n_channels, self.n_samples))
        self.y_scale = 1
        self.y_shift = np.zeros(self.n_channels)

    def get_state(self):
        update = self.state_change
        if self.state_change:
            self.state_change = False
        return update, self.cursor, self.traces, self.yshift, self.yscale

    def on_data(self, data):
        """
        :param data: (n_channels, n_samples)
        """
        s = data.shape[1]
        idx = np.arange(self.cursor, self.cursor+s) % self.n_samples
        self.traces[:, idx] = data
        last_cursor = self.cursor
        self.cursor = (self.cursor + s) % self.n_samples

        # recompute scaling parameters on cursor wrap-around
        if self.cursor < last_cursor:
            trace_max = np.max(self.traces)
            scale = np.round(0.5*(trace_max - np.min(self.traces)), 2)
            shift = np.max(self.traces, axis=1) - scale
            if scale != 0:
                self.y_scale = 100.0 / scale
                self.y_shift = shift
