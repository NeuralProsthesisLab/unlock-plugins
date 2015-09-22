from core.event import Event


class UnlockView(object):
    """
    In the Unlock MVC architecture, the View is an app screen i.e. the visual
    components that may appear on a single screen of an app's functionality.
    """
    def __init__(self, model=None):
        self.model = model
        self.on_render = Event("View render call")

    def render(self):
        if self.model is None:
            return
        if self.model.is_dirty:
            self.on_render()


class UnlockModel(object):
    """
    In the Unlock MVC architecture, the Model encapsulates the application state
    and business logic.
    """
    def __init__(self):
        self._dirty = False

    def __setattr__(self, name, value):
        if getattr(self, name) != value:
            self._dirty = True
        object.__setattr__(self, name, value)

    def is_dirty(self):
        if self._dirty:
            self._dirty = False
            return True
        else:
            return False
