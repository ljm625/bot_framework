from abc import ABCMeta,abstractmethod

class ActionAbstract(object):
    __metaclass__ = ABCMeta

    @classmethod
    def get_instance(cls,input):
        """Method that should initialize the instance
        The input here is  a dict, where you can load whatever you want
        """

    @abstractmethod
    def parse_input(self,input):
        """Method that should parse the input value"""

