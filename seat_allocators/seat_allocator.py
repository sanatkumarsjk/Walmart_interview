import abc

class SeatAllocator(abc.ABC):
    @abc.abstractmethod
    def assign_seat(self):
        pass