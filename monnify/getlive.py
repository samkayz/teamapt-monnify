
def getlive(live):
    if live == True:
        return 'https://api.monnify.com'
    elif live == False:
        return 'https://sandbox.monnify.com'
    else:
        return 'live can either be True or False'
__name__ == "__main__"