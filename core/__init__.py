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


class UnlockModel(object):
    """
    In the Unlock MVC architecture, the Model encapsulates the application state
    and business logic.
    """
    def __init__(self):
        self._dirty = True

    def __setattr__(self, name, value):
        if name != '_dirty':
            try:
                if getattr(self, name) != value:
                    self._dirty = True
            except AttributeError:
                pass
        object.__setattr__(self, name, value)

    def is_dirty(self):
        if self._dirty:
            self._dirty = False
            return True
        else:
            return False
