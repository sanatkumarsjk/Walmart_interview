class ValidateRequest:

    def validate(self,requests):
        i=0
        while i < len(requests):
            try:
                requests[i][1] = int(requests[i][1])
                i+=1
            except:
                print("Discarding request:", requests[i][0])
                del requests[i]
        return requests
