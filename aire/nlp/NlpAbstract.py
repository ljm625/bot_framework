from abc import ABCMeta, abstractmethod


# TODO : Consider which function is essential for NLP engine here.

class NlpAbstract(object):
    __metaclass__ = ABCMeta

    @classmethod
    def get_instance(cls, input):
        """Method that should initialize the instance
        The input here is  a dict, where you can load whatever you want
        """

    @abstractmethod
    def parse_sentence(self,input):
        """Method that get the message from the input, if you don't need to do that, just return the message in the method."""

