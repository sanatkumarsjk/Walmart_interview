import sys
import pandas as pd
from theater import theater
from weighted_scoring import optimalAllocation
from requests_parser import fileParser
# from linear_allocation import assignSeat

#read request from file; returns a list of requests
def read_requests():
    try:
        data = pd.read_csv(sys.argv[1],sep=' ', header = None)
        request = [[],[]]
        for index, row in data.iterrows():
            request[0].append(row[0])
            request[1].append(row[1])
        return request
    except:
        print('Invalid file name or error in file; please provide correct file path as first argument. E.g. python main.py test.txt')

#entry function to the assign seats
def handle_requests():
    requests = read_requests()
    if not requests:
        return
    #new theater object
    walmart = theater("Walmart",(10,5))
    requests = fileParser().parse(requests,walmart)
    allocations = []
    for i in range(len(requests[0])):
        allocations.append(optimalAllocation().assign_seat(requests[0][i],requests[1][i],walmart)  )   #assigns seats as requested params(ID, seat_count,theare_object)
    pd.DataFrame(allocations).to_csv('Walmart.txt', sep='\t', index=False, header=None)
    print(walmart.get_seats())
handle_requests()