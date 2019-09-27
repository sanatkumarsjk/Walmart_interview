from resources.helper import helper
from resources.theater import theater
from file_handler.txt_writer import TxtWriter
from file_handler.txt_reader import TxtReader
from seat_allocators.weighted_allocator import WeightedAllocation
from request_parser.knapsack_parser import Knapsack as knapsack_request_parser

class HandleRequests:

    def handle_requests(self,filename,output_file):
        requests = TxtReader().read_file(filename)   #reads file data
        if not requests: return "No valid request found"
        walmart = theater("Walmart", helper().generate_seat(10,20))     #new theater object
        requests = knapsack_request_parser().parse(requests, walmart)     #parses file data
        allocations = []
        for i in range(len(requests)):
            allocations.append(WeightedAllocation().assign_seat(requests[i][0],requests[i][1],walmart))
        return TxtWriter().write_file(allocations, output_file)

    # print(HandleRequests().handle_requests(sys.argv[1]))