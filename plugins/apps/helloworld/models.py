"""
models.py
Where the business logic goes

The Hello World app places the string "Hello World!" at the center of the
screen. Arrow key presses will move the text in the corresponding direction
one space only i.e. the text can take one of 5 positions: up, down, left, right,
and center. A space bar press will randomly change the color of the text.
"""
from functools import partial
from random import randint

from core import UnlockModel


rand8bit = partial(randint, 0, 255)


class HelloWorldModel(UnlockModel):
    def __init__(self):
        super(HelloWorldModel, self).__init__()
        self.text_position = (0.5, 0.5)
        self.text_color = (255, 255, 255, 255)

    def on_decision(self, decision):
        if decision == 1:
            self.text_position = (0.5, 0.75)
        elif decision == 2:
            self.text_position = (0.5, 0.25)
        elif decision == 3:
            self.text_position = (0.25, 0.5)
        elif decision == 4:
            self.text_position = (0.75, 0.5)

    def on_selection(self):
        self.text_color = (rand8bit(), rand8bit(), rand8bit(), 255)
