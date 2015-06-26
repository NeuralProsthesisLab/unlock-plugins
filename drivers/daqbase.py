__author__ = 'Graham Voysey'
from abc import ABCMeta,abstractmethod

class DAQBase(metaclass=ABCMeta):
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