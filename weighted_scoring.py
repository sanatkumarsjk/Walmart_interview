class optimalAllocation:

    def assign_seat(self, req_id: object, seat_count: int, theater: object) -> tuple:
        # if theater is full/seat_count overflows.
        if theater.get_unassigned_seats() < seat_count:
            return (False, 0)
        print(req_id)
        self.__check_availability(seat_count, theater)

    def __check_availability(self, seat_count, theater):
        available_slots = theater.get_available_seats()

        def check_seats_in_section(sections):
            for row in sections:
                if seat_count == available_slots[row]:
                    print("Seats are available next to each other and no more seats are available in this row", seat_count)
                    return ()
            for row in sections:
                if seat_count < available_slots[row]:
                    print("Seats are available next to each other", seat_count)
                    return
            for row in sections:
                if available_slots[row] > 0:
                    print("Seats are not available next to each other", seat_count)
                    return
        check_seats_in_section([3,4,5,6])
        return
