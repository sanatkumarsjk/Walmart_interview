import abc

class requestConverter(abc.ABC):
    def __init__(self):
        self.id = 0
        self.status = None
        self.seatType = None
        self.rank = 1