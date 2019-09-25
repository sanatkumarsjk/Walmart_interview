import abc

class requestConverter(abc.ABC):
    @abc.abstractmethod
    def parse(self):
        pass