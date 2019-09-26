import sys
import pandas as pd
from resources.theater import theater
from seat_allocators.weighted_allocator import OptimalAllocation
from file_reader.txt_reader import TxtReader
from request_parser.request_parser import RequestParser

#entry function to the assign seats
def handle_requests():
    filename = sys.argv[1]
    requests = TxtReader().read_file(filename)   #reads file data
    if not requests:
        return
    walmart = theater("Walmart",(10,20))     #new theater object
    requests = RequestParser().parse(requests, walmart)     #parses file data
    print(requests, "final answer")
    allocations = []
    for i in range(len(requests[0])):
        allocations.append(OptimalAllocation().assign_seat(requests[0][i],requests[1][i],walmart))   #assigns seats as requested params(ID, seat_count,theare_object)
    pd.DataFrame(allocations).to_csv('output/Walmart.txt', sep='\t', index=False, header=None)
    print(walmart.get_seats())
handle_requests()