class optimalAllocation:

    def assign_seat(self, req_id: str, seat_count: int, theater: object) -> object:
        # if theater is full/seat_count overflows.
        if theater.get_unassigned_seats() < seat_count:
            return (False, 0)
        print("Searching for best seats for request: ", req_id)
        seats_to_be_allotted = seat_count
        seat_counter = 0
        allocated_seats = [req_id]
        while seats_to_be_allotted > 0 and seat_counter != seat_count:
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
        theater_size = theater.get_size()[0]
        sections=[[],[],[]]
        for i in range(theater_size):
            if i < theater_size*0.3:
                sections[1].append(i)
            elif i < theater_size*0.7:
                sections[0].append(i)
            else:
                sections[2].append(i)
        for section in sections:
            proposed_seats = self.__check_seats_in_section(section, seat_count, available_slots, theater)
            if proposed_seats:
                return proposed_seats
        return False

    def __check_seats_in_section(self, section, seat_count, available_slots, theater):
        for row in section:
            if seat_count == available_slots[row]:
                return (row, theater.get_size()[1] - available_slots[row])
        for row in section:
            if seat_count < available_slots[row]:
                return (row, theater.get_size()[1] - available_slots[row])
        return False
