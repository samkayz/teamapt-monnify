import requests
import json
from requests.auth import HTTPBasicAuth

def getlive(live):
    if live == True:
        return 'https://sandbox.monnify.com'
    elif live == False:
        return 'https://sandbox.monnify.com'
    else:
        return 'live can either be True or False'
__name__ == "__main__"



def Authenticate(username, password, live):

    if live == True or live == False:
        baseurl = getlive(live)
        response = requests.post(f'{baseurl}/api/v1/auth/login', 
        auth=HTTPBasicAuth(username, password))

        response_dict = json.loads(response.text)
    
        a = response_dict['responseBody']['accessToken']
        return f'Bearer {a}'
    else:
        return getlive(live)
__name__ == "__main__"





class Monnify:


    def VerifyAccount(self, accountNumber, bankCode, live):
        if live == True or live == False:
            baseurl = getlive(live)
            url = f'{baseurl}/api/v1/disbursements/account/validate?accountNumber={accountNumber}&bankCode={bankCode}'

            payload = {}
            headers= {}

            response = requests.request("GET", url, headers=headers, data = payload)

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)


    def ReserveAccount(self,token, accountReference,  accountName, contractCode, customerEmail, customerName, live):
        if live == True or live == False:
            baseurl = getlive(live)
            url = f'{baseurl}/api/v1/bank-transfer/reserved-accounts'
            payload = {
                "accountReference": accountReference,
                "accountName": accountName,
                "currencyCode": "NGN",
                "contractCode": contractCode,
                "customerEmail": customerEmail, 
                "customerName": customerName 
                }
            headers = {
                'Content-Type': 'application/json',
                'Authorization': token
                }

            response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

            #print(response.text.encode('utf8'))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)


    def Disbursement(self, api_key, secret_key, amount, reference, narration, bankCode, accountNumber, walletId, live):
        if live == True or live == False:
            baseurl = getlive(live)
            username = api_key
            password = secret_key
            url = f'{baseurl}/api/v1/disbursements/single'

            payload = {
                'amount': amount,
                'reference': reference,
                'narration': narration,
                'bankCode': bankCode,
                'accountNumber': accountNumber,
                'currency': 'NGN',
                'walletId': walletId
                }
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, auth=HTTPBasicAuth(username, password), headers=headers, data = json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)

