import abc

class Seat(abc.ABC):
    def __init__(self, id, seat_type):
        self.id = 0
        self.status = None
        self.seat_type = seat_type
