from plugins.apps.appplugin import AppPlugin

from plugins.apps.rtsynth.models import RTSynthModel
from plugins.apps.rtsynth.views import RTSynthView


class RTSynth(AppPlugin):
    def register(self, window):
        model = RTSynthModel()
        canvas = window.get_app_canvas()
        view = RTSynthView(canvas, model)

        self.models.append(model)
        self.canvases.append(canvas)
        self.views.append(view)
