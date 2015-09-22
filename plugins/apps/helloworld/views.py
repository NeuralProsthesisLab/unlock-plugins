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
    def __init__(self):
        super(HelloWorldView, self).__init__()
        self.label = self.drawText("Hello World!", 0, 0, None)
