# Walmart_interview

## Assumptions

1. The algorithm requested is part of larger system, thus a file input is used to simulate reservation requests.
2. Input file is a text file and input is considered as a static input consisting of all the requests.
3. Optimal solution consists maximum theater utilization and maximum Customer satisfaction.
4. **Maximum theater utilization** is possible when maximum theater(number of seats) is filled.
4. **Customer satisfaction** depends on two parameters:
   - How many of the requested seats are assigned next to each other.
   - Which section the alloted seat belong to; therater being divided in three section, viz. Top, Center, Bottom.
     - Customers prefer Center, Top and then Bottom section .
5. Customer satisfaction can be clculated be following formula:
   - CSI =  ![equation](http://www.sciweavers.org/tex2img.php?eq=\sum_{i=1}^{k}c_{i}%2Bc_{i}*seatVal_{i}&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=)
     - k is number of groups formed for a request.
     - where c in number of people in group i.
     - seatvalue if the value of seats in a group.
    