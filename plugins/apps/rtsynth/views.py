"""
views.py
Where the display rendering code goes

The UI for the RTSynth app is a static grid of symbols and a movable cursor
"""
import os

from core import UnlockView


class RTSynthView(UnlockView):
    def __init__(self, canvas, model):
        super(RTSynthView, self).__init__(canvas, model)
        base = os.path.dirname(os.path.realpath(__file__))
        self.keyboard = self.create_sprite(os.path.join(base, 'keyboard.png'),
                                           background=True)
        self.cursor = self.create_label('+')

    def render(self):
        if self.model.is_dirty():
            self.cursor.x = self.canvas.width*self.model.cursor_position[0]
            self.cursor.y = self.canvas.height*self.model.cursor_position[1]
