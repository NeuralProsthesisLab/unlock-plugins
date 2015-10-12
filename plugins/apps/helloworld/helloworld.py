from plugins.apps.appplugin import AppPlugin

from plugins.apps.helloworld.models import HelloWorldModel
from plugins.apps.helloworld.views import HelloWorldView


class HelloWorld(AppPlugin):
    def register(self, window):
        model = HelloWorldModel()
        canvas = window.get_app_canvas()
        view = HelloWorldView(canvas, model)

        self.models.append(model)
        self.canvases.append(canvas)
        self.views.append(view)

    def process_command(self, command):
        if command.decision is not None:
            for model in self.models:
                model.on_decision(command.decision)
