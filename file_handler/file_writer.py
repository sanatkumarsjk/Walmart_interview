import abc

class FileWriter(abc.ABC):
    @abc.abstractmethod
    def write_file(self):
        pass