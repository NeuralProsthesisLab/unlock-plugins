from yapsy.IPlugin import IPlugin


class DecoderPlugin(IPlugin):
    """
    Decoder plugins consume an array of data from a DAQ plugin, and emit a
    stream of commands and selections.
    """
    def process_data(self, data):
        return NotImplementedError