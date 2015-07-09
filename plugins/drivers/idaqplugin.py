__author__ = 'Graham Voysey'

from yapsy import IPlugin
import logging
logging.getLogger('yaspy').setLevel(logging.DEBUG)

class IDAQPlugin(IPlugin):

    name = ""

    def __init__(self):
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


    def open(self,address):
        """

        :param address:
        :return:
        """


    def close(self):
        """

        :return:
        """


    def get_data(self,samples):
        """

        :param samples:
        :return:
        """