__author__ = 'gvoysey'
from yapsy.IPlugin import IPlugin

class IDecoderPlugin(IPlugin):
    """
    Decoder plugins consume an array of data from a DAQ plugin, and emit a stream of commands and selections.
    """
    pass