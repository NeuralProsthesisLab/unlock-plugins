__author__ = 'Graham Voysey'
import abc
import six

@six.add_metaclass(abc.ABCMeta)
class DAQBase(object):
    @abc.abstractmethod
    def start(self):
        """

        :return:
        """

    @abc.abstractmethod
    def stop(self):
        """

        :return:
        """

    @abc.abstractmethod
    def init(self):
        """

        :return:
        """

    @abc.abstractmethod
    def open(self,address):
        """

        :param address:
        :return:
        """

    @abc.abstractmethod
    def close(self):
        """

        :return:
        """

    @abc.abstractmethod
    def get_data(self,samples):
        """

        :param samples:
        :return:
        """