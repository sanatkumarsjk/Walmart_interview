class ValidateRequest:

    def validate(self,requests):
        i=0
        while i < len(requests):
            try:
                int(requests[i][0][1:])  # checks
                requests[i][1] = int(requests[i][1])
                if requests[i][0][0] != 'R' or requests[i][1] < 0:
                    raise Exception()
                i += 1
            except:
                print("Discarding request:", requests[i][0])
                del requests[i]
        return requests
