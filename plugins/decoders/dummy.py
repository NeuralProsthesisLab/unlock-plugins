from plugins.decoders.decoderplugin import DecoderPlugin


class DummyDecoder(DecoderPlugin):
    def process_data(self, command):
        if 1 <= command.data[0, 0] <= 4:
            command.decision = command.data[0, 0]
        elif command.data[0, 0] == 5:
            command.selection = True
        return command
