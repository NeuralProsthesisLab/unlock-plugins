__author__ = 'Graham Voysey'

from yapsy import IPlugin

class DAQPluginBase(IPlugin):

    name = ""


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