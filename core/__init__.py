import pyglet


class UnlockView(object):
    """
    In the Unlock MVC architecture, the View is an app screen i.e. the visual
    components that may appear on a single screen of an app's functionality.
    """
    def __init__(self, canvas, model=None):
        self.canvas = canvas
        self.model = model

    def render(self):
        pass

    def create_label(self, text):
        cx, cy = self.canvas.center()
        return pyglet.text.Label(text, x=cx, y=cy, color=(255, 255, 255, 255),
                                 font_size=48, font_name="Helvetica",
                                 anchor_x='center', anchor_y='center',
                                 batch=self.canvas.batch)

    def draw_line(self, p1, p2, color=(255, 255, 255), group=None):
        return self.canvas.batch.add(2, pyglet.gl.GL_LINES, group,
            ('v2f', (self.canvas.x+p1[0], self.canvas.y+p1[1],
                     self.canvas.x+p2[0], self.canvas.y+p2[1])),
            ('c3B', color*2))

    def draw_line_plot(self, vertices, color=(255,255,255), group=None):
        data_points = int(len(vertices) / 2)
        # create points - 1 line segments
        # both endpoints of each segment need to be specified, so all but the
        # two endpoints of the entire trace need to be repeated
        vertices[::2] = [x + self.canvas.x for x in vertices[::2]]
        vertices[1::2] = [y + self.canvas.y for y in vertices[1::2]]
        line_segments = vertices[0:4]  # (x0, y0, x1, y1)
        for i in range(1, data_points-1):
            line_segments.extend([vertices[i*2], vertices[i*2+1],
                                  vertices[(i+1)*2], vertices[(i+1)*2+1]])
        plot_points = int(len(line_segments) / 2)

        return self.canvas.batch.add(plot_points, pyglet.gl.GL_LINES, group,
            ('v2f', line_segments),
            ('c3B', color*plot_points))


class UnlockModel(object):
    """
    In the Unlock MVC architecture, the Model encapsulates the application state
    and business logic.
    """
    def __init__(self):
        self._dirty = True

    def __setattr__(self, name, value):
        if name != '_dirty':
            self._dirty = True
        object.__setattr__(self, name, value)

    def is_dirty(self):
        if self._dirty:
            self._dirty = False
            return True
        else:
            return False

    def on_decision(self, decision):
        pass

    def on_selection(self):
        pass

    def on_data(self, data):
        pass
