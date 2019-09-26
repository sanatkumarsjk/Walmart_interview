import abc

class FileReader(abc.ABC):
    @abc.abstractmethod
    def read_file(self):
        pass