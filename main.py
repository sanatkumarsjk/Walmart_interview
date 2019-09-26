import sys
import pandas as pd
from resources.theater import theater
from seat_allocators.weighted_allocator import OptimalAllocation
from file_reader.txt_reader import TxtReader
from request_parser.knapsack_parser import RequestParser as knapsack_requestparser

#entry function to the assign seats
def handle_requests():
    filename = sys.argv[1]
    requests = TxtReader().read_file(filename)   #reads file data
    if not requests:
        return
    walmart = theater("Walmart",(10,20))     #new theater object
    requests = knapsack_requestparser().parse(requests, walmart)     #parses file data
    allocations = []
    for i in range(len(requests)):
        allocations.append(OptimalAllocation().assign_seat(requests[i][0],requests[i][1],walmart))   #assigns seats as requested params(ID, seat_count,theare_object)
    pd.DataFrame(allocations).to_csv('output/Walmart.txt', sep='\t', index=False, header=None)
handle_requests()