from seat_allocators.seat_allocator import SeatAllocator


class LinearAllocation(SeatAllocator):

    def assign_seat(self, req_id, seat_count, theater):
        available_slots = theater.get_available_seats()
        if seat_count in available_slots.values():
            row = list(available_slots.values()).index(seat_count)
            seat_assigned_count = 0
            while seat_assigned_count < seat_count:
                theater.set_seats(row,5-available_slots[row], req_id)
                seat_assigned_count+=1
            return
        for row in range(10):
            if seat_count < available_slots[row]:
                seat_assigned_count = 0
                while seat_assigned_count < seat_count:
                    theater.set_seats(row,5-available_slots[row], req_id)
                    seat_assigned_count+=1
                return
        for row in range(10):
            if available_slots[row] > 0:
                temp_seat_count = available_slots[row]
                while temp_seat_count != 0:
                    theater.set_seats(row, 5 - available_slots[row], req_id)
                    temp_seat_count -= 1
                    seat_count -= 1
                    if seat_count == 0:
                        return
        print("In assign")
        return True