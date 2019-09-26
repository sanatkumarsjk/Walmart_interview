import abc

class RequestReader(abc.ABC):
    @abc.abstractmethod
    def read_file(self):
        pass