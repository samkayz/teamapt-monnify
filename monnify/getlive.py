
class GetBaseUrl:
    """
    This Class return URL for live or sandbox based on what the user passed
    """
    def __init__(self, live):
        self.live = live

    def urls(self):
        if self.live:
            return 'https://api.monnify.com'
        elif not self.live:
            return 'https://sandbox.monnify.com'
        else:
            return 'live can either be True or False'
