"""
models.py
Where the business logic goes

The Hello World app places the string "Hello World!" at the center of the
screen. Arrow key presses will move the text in the corresponding direction
one space only i.e. the text can take one of 5 positions: up, down, left, right,
and center. A space bar press will randomly change the color of the text.
"""
from core import UnlockModel


class HelloWorldModel(UnlockModel):
    def __init__(self):
        super(HelloWorldModel, self).__init__()
        self.text_position = (0.5, 0.5)
        self.text_color = (255, 255, 255, 255)
