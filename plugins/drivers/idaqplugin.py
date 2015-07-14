__author__ = 'Graham Voysey'

from yapsy.IPlugin import IPlugin
import logging

logging.getLogger('yaspy').setLevel(logging.DEBUG)


class IDAQPlugin(IPlugin):
    """
    DAQ plugins consume raw information from a DAQ card (enobio, mobilab, any LSL device, tobii eye tracker, etc.)
    and emit processed data (as a numpy array, probably) to a decoder.
    """
    name = ""

    def __init__(self, *params):
        pass

    def start(self):
        """

        :return:
        """

    def stop(self):
        """

        :return:
        """

    def init(self):
        """

        :return:
        """

    def open(self, address):
        """

        :param address:
        :return:
        """

    def close(self):
        """

        :return:
        """

    def get_data(self, samples):
        """

        :param samples:
        :return:
        """
