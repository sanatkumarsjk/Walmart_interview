from request_parser.parser import RequestParser

class Knapsack(RequestParser):

    def parse(self, req_list, theater):
        theater_size = theater.get_size()[0] * theater.get_size()[1]
        req_list = self.__knapSack(theater_size, req_list, len(req_list))
        return req_list

    def __knapSack(self, theater_size, req_list, n):
        Ks = [[0 for theater_size in range(theater_size + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            for theater_size in range(theater_size + 1):
                if i == 0 or theater_size == 0:
                    Ks[i][theater_size] = 0
                elif req_list[i - 1][1] <= theater_size:
                    Ks[i][theater_size] = max(req_list[i - 1][1] + Ks[i - 1][theater_size - req_list[i - 1][1]], Ks[i - 1][theater_size])
                else: Ks[i][theater_size] = Ks[i - 1][theater_size]
        best_req, max_seating = [], Ks[n][theater_size]
        theater_size = theater_size
        for i in range(n, 0, -1):
            if max_seating <= 0:
                break
            if max_seating == Ks[i - 1][theater_size]:
                continue
            else:
                best_req.append(req_list[i - 1])
                max_seating = max_seating - req_list[i - 1][1]
                theater_size = theater_size - req_list[i - 1][1]
        return best_req
