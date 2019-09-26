import abc

class RequestParser(abc.ABC):
    @abc.abstractmethod
    def parse(self):
        pass