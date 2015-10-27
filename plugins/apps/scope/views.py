import numpy as np

from core import UnlockView


class TimeScopeView(UnlockView):
    def __init__(self, canvas, model, labels=None):
        super(TimeScopeView, self).__init__(canvas, model)
        self.xlim = (canvas.width*0.05, canvas.width*0.95)
        self.ylim = (canvas.height*0.05, canvas.height*0.95)

        self.x_scale = (self.xlim[1] - self.xlim[0]) / self.model.n_samples
        self.trace_height = (self.ylim[1]-self.ylim[0]) / self.model.n_channels
        self.trace_margin = 0.1 * self.trace_height
        self.trace_height -= self.trace_margin
        self.y_scale = self.trace_height / 200

        self.traces = []
        for trace in range(self.model.n_channels):
            x = self.scale_width(np.arange(0, self.model.n_samples))
            y = self.scale_height(np.zeros(self.model.n_samples), 0, 1, trace)
            values = zip(x, y)
            vertices = [point for points in values for point in points]
            self.traces.append(self.draw_line_plot(vertices))

        self.cursor = self.draw_line((self.xlim[0], self.ylim[0]),
                                     (self.xlim[0], self.ylim[1]),
                                     color=(255, 0, 0))

    def render(self):
        if self.model.is_dirty():
            x = self.scale_width(self.model.cursor)
            self.cursor.vertices[::2] = (x,)*2
            for i, trace in enumerate(self.traces):
                y = self.scale_height(self.model.traces[i],
                                      self.model.y_shift[i], self.model.y_scale,
                                      i)
                data_points = len(y)
                y_points = np.zeros(len(trace.vertices)/2)
                for j in range(data_points-1):
                    y_points[[j*2, j*2+1]] = y[j:j+2]
                trace.vertices[1::2] = y_points

    def scale_width(self, x):
        """
        Scale the position of the data points to fit the width of the screen
        """
        return x * self.x_scale + self.xlim[0]

    def scale_height(self, y, shift, scale, trace=0):
        """
        Scale the position of the data points to fit the height of the screen
        and the number of traces. The scale factor is automatically adjusted
        to the data, and is thus part of the model.
        """
        offset = self.ylim[0] + 0.5*self.trace_height + \
            trace*(self.trace_height + self.trace_margin)
        y = (y - shift) * scale
        return y * self.y_scale + offset
