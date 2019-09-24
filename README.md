# Walmart_interview

## Assumptions

1. Algorithm requested is part of larger system, thus a file input is used to simulate reservation requests ordered by time.
2. Requests need to be handled as and when they come. I.e. Allocation of seats for request i needs to be done before processing requests>i
3. Input file does not contain any errors. I.e. file always has format as follow:
   - <request_id> <seat_count>    
   - E.g. R001 4
4. Customer satisfaction depends on following parameters:
   - How many of the requested seats are assigned next to each other.
   - Which section is seat alloted. Therater being divided in three section Viz Top, Center, Bottom.
     - Customer prefer Center, Top and then Bottom section.