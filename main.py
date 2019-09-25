import sys
import pandas as pd
from theater import theater
from weighted_scoring import optimalAllocation
from txtParser import txtParser
# from linear_allocation import assignSeat

#entry function to the assign seats
def handle_requests():
    filename = sys.argv[1]
    parser = txtParser()
    requests = parser.read_requests(filename)   #reads file data
    if not requests:
        return
    walmart = theater("Walmart",(10,5))     #new theater object
    requests = txtParser().parse(requests, walmart)     #parses file data
    allocations = []
    for i in range(len(requests[0])):
        allocations.append(optimalAllocation().assign_seat(requests[0][i],requests[1][i],walmart))   #assigns seats as requested params(ID, seat_count,theare_object)
    pd.DataFrame(allocations).to_csv('Walmart.txt', sep='\t', index=False, header=None)
    print(walmart.get_seats())
handle_requests()