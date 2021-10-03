
class GetBaseUrl:
    def __init__(self, live):
        self.live = live
    def urls(self):
        if self.live == True:
            return 'https://api.monnify.com'
        elif self.live == False:
            return 'https://sandbox.monnify.com'
        
        else:
            # print(self.live)
            return 'live can either be True or False'
