from core.pyglet_window import Command
from plugins.decoders.decoderplugin import DecoderPlugin


class DummyDecoder(DecoderPlugin):
    def process_data(self, data):
        command = Command()
        if 1 <= data[0] <= 4:
            command.decision = data[0]
        elif data[0] == 5:
            command.selection = True
        return command
