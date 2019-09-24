class optimalAllocation:

    def assign_seat(self, req_id: object, seat_count: int, theater: object) -> tuple:
        # if theater is full/seat_count overflows.
        if theater.get_unassigned_seats() < seat_count:
            return (False, 0)
        print("Searching for best seats for request: ", req_id)
        seats_to_be_allotted = seat_count
        seat_counter = 0
        allocated_seats = [req_id]
        while seats_to_be_allotted > 0:
            # print(seat_counter, seats_to_be_allotted)
            proposed_seats = self.__check_availability(min(seat_count-seat_counter,seats_to_be_allotted), theater)
            if proposed_seats:
                for offset in range(min(seat_count-seat_counter,seats_to_be_allotted)):
                    theater.set_seats(proposed_seats[0], proposed_seats[1]+offset, req_id)
                    allocated_seats.append(chr(74-proposed_seats[0])+str(proposed_seats[1]+offset+1))
                    seats_to_be_allotted-=1
                continue
            seat_counter+=1
        print("Seats allocated to request: ", req_id)

        return allocated_seats

    def __check_availability(self, seat_count, theater):
        available_slots = theater.get_available_seats()
        for section in ((3,4,5,6),(0,1,2),(7,8,9)):
            proposed_seats = self.__check_seats_in_section(section, seat_count, available_slots, theater)
            if proposed_seats:
                return proposed_seats
        return False

    def __check_seats_in_section(self, sections, seat_count, available_slots, theater):
        for row in sections:
            if seat_count == available_slots[row]:
                # print("Seats are available next to each other and the row is full", seat_count)
                return (row, theater.get_size()[1] - available_slots[row])
        for row in sections:
            if seat_count < available_slots[row]:
                # print("Seats are available next to each other", seat_count)
                return (row, theater.get_size()[1] - available_slots[row])
        return False
