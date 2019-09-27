import sys
from resources.handle_requests import HandleRequests

try:
    print(HandleRequests().handle_requests(sys.argv[1], "/output/Walmart.txt"))
except:
    print("Please provide vaild file name")