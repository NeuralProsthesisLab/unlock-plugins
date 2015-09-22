"""
views.py
Where the display rendering code goes

The Hello World app places the string "Hello World!" at the center of the
screen. Arrow key presses will move the text in the corresponding direction
one space only i.e. the text can take one of 5 positions: up, down, left, right,
and center. A space bar press will randomly change the color of the text.
"""
from core import UnlockView


class HelloWorldView(UnlockView):
    def __init__(self, canvas, model):
        super(HelloWorldView, self).__init__(canvas, model)
        self.label = self.create_label("Hello World!")

    def render(self):
        if self.model.is_dirty():
            self.label.x = self.canvas.width*self.model.text_position[0]
            self.label.y = self.canvas.height*self.model.text_position[1]
            self.label.color = self.model.text_color
