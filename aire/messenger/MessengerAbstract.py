from abc import ABCMeta, abstractmethod


class MessengerAbstract(object):
    __metaclass__ = ABCMeta

    @classmethod
    def get_instance(cls, input=None):
        """Method that should initialize the instance
        The input here is  a dict, where you can load whatever you want
        """

    @abstractmethod
    def get_message(self,input):
        """Method that get the message from the input, if you don't need to do that, just return the message in the method."""

    @abstractmethod
    def send_message(self,input,receiver):
        """Method that allows us to send message to the specific sender."""
