from plugins.apps.appplugin import AppPlugin

from plugins.apps.helloworld.models import HelloWorldModel
from plugins.apps.helloworld.views import HelloWorldView


class HelloWorld(AppPlugin):
    def register(self, window):
        model = HelloWorldModel()

        canvas = window.get_app_canvas()
        view = HelloWorldView(canvas, model)

        self.models.append(model)
        self.views.append(view)

        window.views = self.views

    def activate(self):
        pass

    def deactivate(self):
        pass
