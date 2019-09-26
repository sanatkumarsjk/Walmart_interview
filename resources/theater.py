class theater:
    def __init__(self, name, seats):
        self.__name = name
        self.__size = (len(seats),len(seats[0]))
        self.__seats = seats
        self.__unassigned_seats = len(seats)*len(seats[0])
        self.__available_seat = {}
        for i in range(len(seats)):
            self.__available_seat[i] = len(seats[0])

    #trivial data for theater
    def get_name(self):
        return self.__name

    def set_name__(self, name):
        self.__name = name

    def get_size(self):
        return self.__size

    #keeps track of number of unassigned seats
    def get_unassigned_seats(self):
        return self.__unassigned_seats

    def __set_unassigned_seats(self,number):
        self.__unassigned_seats -= number

    #theater structure
    def get_seats(self):
        return self.__seats

    def set_seats(self, row, column, request_id):
        if self.__seats[row][column].status == None:
            self.set_available_seats(row, 1)
            self.__set_unassigned_seats(1)
            self.__seats[row][column].status = request_id
            return True
        return False

    # returns number of available seat in particular row.
    def get_available_seats(self):
        return self.__available_seat

    def set_available_seats(self, row, seat_count):
        if self.get_available_seats()[row] >= seat_count:
            self.__available_seat[row] -= seat_count
            return True
        return False


