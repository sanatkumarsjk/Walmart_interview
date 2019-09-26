import operator
class RequestParser:

    def __init__ (self):
        self.__max_possible_seating = 0
        self.dp = {}

    def parse(self, req_list, theater):
        print("Searching for optimal request sequence for Maximum theater utilization")
        req_list = sorted(req_list, key=operator.itemgetter(1), reverse=True)
        requests = [[],[]]
        for i in req_list:
            requests[0].append(i[0])
            requests[1].append(i[1])
        if sum(requests[1]) > theater.get_size()[0] * theater.get_size()[1]:
            max, best_request_sequence = 0, None
            for i in self.__findMaximum(requests[0], requests[1], set(), 0, theater):
                if max < i[0]:
                    best_request_sequence = i
                    max = i[0]
            requests=[[],[]]
            for i in range(1,len(best_request_sequence),2):
                requests[0].append(best_request_sequence[i])
                requests[1].append(best_request_sequence[i+1])
        print("Optimal request sequence found for Maximum theater utilization")
        return requests

    def __findMaximum(self,req, seats_req, ans, seat_count, theater):
        theater_size = theater.get_size()
        if self.__max_possible_seating == theater_size[0]*theater_size[1]:
            return
        for i in self.dp:
            if i==(repr(sorted(ans))):
                return self.dp[i]

        #termination condition
        if len(req) == 1:
            new_seat_count = seat_count + seats_req[0]
            if new_seat_count > self.__max_possible_seating and new_seat_count < 20:
                self.__max_possible_seating = new_seat_count
                return [[self.__max_possible_seating]+[req[0],seats_req[0]]]
            return
        candidates, index = [], -1
        for req_id, seat_req in zip(req, seats_req):
            index+=1
            if seat_count + seat_req > theater_size[0]*theater_size[1]:
                continue
            answer = ans
            answer.add(req[index])
            request_sequence = self.__findMaximum(req[:index] + req[index+1:], seats_req[:index] + seats_req[index+1:], answer , seat_count + seat_req, theater)
            self.__max_possible_seating = max(self.__max_possible_seating ,seat_count+seats_req[index])
            if request_sequence:
                for item in request_sequence:
                    candidates.append(item+[req[index],seats_req[index]])
            else: candidates.append([seat_count+seats_req[index],req[index],seats_req[index]])
        self.dp[repr(sorted(ans))] = candidates
        return candidates