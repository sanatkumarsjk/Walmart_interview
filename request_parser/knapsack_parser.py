class RequestParser:

    def parse(self, req_list, theater):
        theater_size = theater.get_size()[0] * theater.get_size()[1]
        req_list = self.knapSack(theater_size, req_list, req_list, len(req_list))
        return req_list

    def knapSack(self, W, wt, val, n):
        K = [[0 for w in range(W + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif wt[i - 1][1] <= w:
                    K[i][w] = max(val[i - 1][1] + K[i - 1][w - wt[i - 1][1]], K[i - 1][w])
                else:
                    K[i][w] = K[i - 1][w]

        res = K[n][W]
        ans = []
        w = W
        for i in range(n, 0, -1):
            if res <= 0:
                break
            if res == K[i - 1][w]:
                continue
            else:

                ans.append(wt[i - 1])
                res = res - val[i - 1][1]
                w = w - wt[i - 1][1]
        return ans
