from abc import ABCMeta, abstractmethod


class TypoAbstract(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    @classmethod
    def get_instance(cls, input):
        """Method that should initialize the instance
        The input here is  a dict, where you can load whatever you want
        """

    @abstractmethod
    def parse_input(self,input):
        """Method that parse the input and do a auto sentence correction base on the input."""
    #
    # @abstractmethod
    # def send_message(self,input,receiver):
    #     """Method that allows us to send message to the specific sender."""
