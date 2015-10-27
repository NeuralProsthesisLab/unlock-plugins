from plugins.apps.appplugin import AppPlugin

from plugins.apps.scope.models import TimeScopeModel
from plugins.apps.scope.views import TimeScopeView


class TimeScope(AppPlugin):
    def register(self, window):
        model = TimeScopeModel(4, 500)
        canvas = window.get_app_canvas()
        view = TimeScopeView(canvas, model)

        self.models.append(model)
        self.canvases.append(canvas)
        self.views.append(view)


