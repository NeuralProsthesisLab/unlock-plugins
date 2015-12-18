"""
models.py
Where the business logic goes

The RTSynth app presents a grid of phonemic symbols and plays the appropriate
phoneme when the user moves a cursor over a symbol and selects it.
"""
import numpy as np

from core import UnlockModel


class RTSynthModel(UnlockModel):
    def __init__(self):
        super(RTSynthModel, self).__init__()
        self.cursor_position = np.array([0.5, 0.5])

    def on_decision(self, decision):
        self.cursor_position += decision

    def on_selection(self):
        pass
