from resources.seat import Seat
from resources.seat_type import SeatType

class helper:
    def generate_seat(self,row,column):
        seat_type = []
        for i in range(row):
            temp = []
            for j in range(column):
                temp.append(Seat(i * j, SeatType.top))
            seat_type.append(temp)
        return seat_type

    def display_seats(self, row, column, seats):
        for i in range(row):
            temp = []
            for j in range(column):
                temp.append(seats[i][j].status)
            print(temp)