__author__ = 'Graham Voysey'

from abc import ABCMeta, abstractmethod, abstractproperty
from yapsy import IPlugin

class DAQPluginBase(metaclass=ABCMeta, IPlugin):
    @abstractproperty
    def name(self):
        return None

    @abstractmethod
    def start(self):
        """

        :return:
        """

    @abstractmethod
    def stop(self):
        """

        :return:
        """

    @abstractmethod
    def init(self):
        """

        :return:
        """

    @abstractmethod
    def open(self,address):
        """

        :param address:
        :return:
        """

    @abstractmethod
    def close(self):
        """

        :return:
        """

    @abstractmethod
    def get_data(self,samples):
        """

        :param samples:
        :return:
        """