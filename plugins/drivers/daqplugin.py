__author__ = 'Graham Voysey'

from yapsy.IPlugin import IPlugin
import logging

logging.getLogger('yaspy').setLevel(logging.DEBUG)


class DAQPlugin(IPlugin):
    """
    DAQ plugins consume raw information from a DAQ card (enobio, mobilab, any LSL device, tobii eye tracker, etc.)
    and emit processed data (as a numpy array, probably) to a decoder.
    """


    def __init__(self, *params):
        pass

    def start(self):
        """

        :return:
        """
        return NotImplementedError

    def stop(self):
        """

        :return:
        """
        return NotImplementedError

    def init(self):
        """

        :return:
        """
        return NotImplementedError

    def open(self, address):
        """

        :param address:
        :return:
        """
        return NotImplementedError

    def close(self):
        """

        :return:
        """
        return NotImplementedError

    def get_data(self, samples):
        """

        :param samples:
        :return:
        """
        return NotImplementedError
