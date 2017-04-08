from abc import ABCMeta,abstractmethod

class GeneratorAbstract(object):
    __metaclass__ = ABCMeta

    @classmethod
    def get_instance(cls,input):
        """Method that should initialize the instance
        The input here is  a dict, where you can load whatever you want
        """

    @abstractmethod
    def generate(self,input):
        """Method that should generate the output base on input"""

