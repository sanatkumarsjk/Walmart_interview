class optimalAllocation:

    def assign_seat(self, req_id: object, seat_count: int, theater: object) -> tuple:
        # if theater is full/seat_count overflows.
        if theater.get_unassigned_seats() < seat_count:
            return (False, 0)
        print(req_id,'--------------------------------------------------------------------------------------------')
        for i in range(seat_count):
            proposed_seats1 = self.__check_availability(seat_count-i, theater)
            if proposed_seats1:
                proposed_seats2 = self.__check_availability(i, theater)
                if proposed_seats2:
                    print(proposed_seats1, proposed_seats2)
                    for offset in range(seat_count-i):
                        theater.set_available_seats(proposed_seats1[0],1)
                        theater.set_seats(proposed_seats1[0], proposed_seats1[1]+offset, req_id)
                    for offset in range(i):
                        theater.set_available_seats(proposed_seats2[0],1)
                        theater.set_seats(proposed_seats2[0], proposed_seats2[1]+offset, req_id)
                    return

    def __check_availability(self, seat_count, theater):
        available_slots = theater.get_available_seats()
        for section in ((3,4,5,6),(0,1,3),(7,8,9)):
            proposed_seats = self.__check_seats_in_section(section, seat_count, available_slots, theater)
            if proposed_seats:
                return proposed_seats
        return False

    def __check_seats_in_section(self, sections, seat_count, available_slots, theater):
        for row in sections:
            if seat_count == available_slots[row]:
                print("Seats are available next to each other and the row is full", seat_count)
                return (row, theater.get_size()[1] - available_slots[row])
        for row in sections:
            if seat_count < available_slots[row]:
                print("Seats are available next to each other", seat_count)
                return (row, theater.get_size()[1] - available_slots[row])
        return False
