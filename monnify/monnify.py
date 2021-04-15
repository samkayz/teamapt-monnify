## This code is developed by Samson Ilemobayo.
## Software Developer and Fintech Advocate
## Email: ilemobayosamson@gmail.com

import requests
import json
from requests.auth import HTTPBasicAuth
from . monnify_details import getlive



## Funtction that get all the Monnify Credentials.
## The credential is then use to authenticate all 
## the Endpoint for Use

def monnifyCredential(api_key, secret_key, contract, walletId, is_live):
    credentials = {
        'api_key': api_key, 
        'secret_key': secret_key, 
        'contract': contract,
        'walletId': walletId,
        'is_live': is_live
        }
    return credentials
__name__ == "__main__"



### Function that send a request to the Authentication endpoint and 
### get the Toking and retun the token for use

def get_token(credentials):
    live = credentials['is_live']
    if live == True or live == False:
        baseurl = getlive(live)
        username = credentials['api_key']
        password = credentials['secret_key']
        response = requests.post(f'{baseurl}/api/v1/auth/login', 
        auth=HTTPBasicAuth(username, password))

        response_dict = json.loads(response.text)
    
        a = response_dict['responseBody']['accessToken']
        return f'Bearer {a}'
    else:
        return getlive(live)
__name__ == "__main__"


## class that handle all the function and endpoint of monnify.
class Monnify:
    
    
    ## This is the endpoint that verify bank account and it take value of the merchant credentials
    ## account number to be verify and the bank code of the bank. this endpoint will run a check to
    ## verify whether the bank account number is valid by returning the name registered with the 
    ## account number.
    
    def verify_account(self, credentials, accountNumber, bankCode):
        live = credentials['is_live']
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


    ## This function is use to reserve virtual account on the monnify platform.
    ## It take Auth Token, merchant credentials, account reference, accoun name,
    ## customer email, customer name, customer BVN, and available bank. this 
    ## endpoint will then create a virtual account number in the name of customer
    ## suplied and return the details of the account created.
     
    def reserve_account(self,token, credentials, accountReference,  accountName, customerEmail, customerName, customerBvn, availableBank):
        live = credentials['is_live']
        if live == True or live == False:
            contractCode = credentials['contract']
            baseurl = getlive(live)
            url = f'{baseurl}/api/v1/bank-transfer/reserved-accounts'
            payload = {
                "accountReference": accountReference,
                "accountName": accountName,
                "currencyCode": "NGN",
                "contractCode": contractCode,
                "customerEmail": customerEmail,
                "bvn": customerBvn, 
                "customerName": customerName,
                "getAllAvailableBanks": availableBank
                }
            headers = {
                'Content-Type': 'application/json',
                'Authorization': token
                }

            response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
    
    
    def add_link_account(self, token, credentials, accountReference, getAllAvailableBanks, preferredBanks):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            url = f'{baseurl}/api/v1/bank-transfer/reserved-accounts/add-linked-accounts/{accountReference}'
            payload = {
                "getAllAvailableBanks": getAllAvailableBanks,
                "preferredBanks": preferredBanks
            }
            headers = {
                'Content-Type': 'application/json',
                'Authorization': token
                }

            response = requests.request("PUT", url, headers=headers, data = json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        
    
    def update_bvn_reserve(self, token, credentials, bvn, accountReference):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            url = f'{baseurl}/api/v1/bank-transfer/reserved-accounts/update-customer-bvn/{accountReference}'
            payload = {
                "bvn": bvn
            }
            headers = {
                'Content-Type': 'application/json',
                'Authorization': token
                }

            response = requests.request("PUT", url, headers=headers, data = json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        
    
    def deallocate_account(self, token, credentials, accountNumber):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            url = f'{baseurl}/api/v1/bank-transfer/reserved-accounts/{accountNumber}'
            payload = {}
            headers = {
                'Content-Type': 'application/json',
                'Authorization': token
                }

            response = requests.request("DELETE", url, headers=headers, data = json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        
        
    
    def reserve_account_transactions(self, token, credentials, accountReference, page, size):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            url = f'{baseurl}/api/v1/bank-transfer/reserved-accounts/transactions?accountReference={accountReference}&page={page}&size={size}'
            payload = {}
            headers = {
                'Content-Type': 'application/json',
                'Authorization': token
                }

            response = requests.request("GET", url, headers=headers, data = json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
    
    
    def tranfer(self,credentials, amount, reference, narration, bankCode, accountNumber):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            walletId = credentials['walletId']
            username = credentials['api_key']
            password = credentials['secret_key']
            url = f'{baseurl}/api/v1/disbursements/single'
            
            f_amount = float(amount)
            payload = {
                'amount': f_amount,
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
        
        
        
    
    def authorize_tranfer(self,credentials, reference, authorizationCode):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            username = credentials['api_key']
            password = credentials['secret_key']
            url = f'{baseurl}/api/v1/disbursements/single/validate-otp'
        
            payload = {
                "reference": reference,
                "authorizationCode": authorizationCode
            }
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, auth=HTTPBasicAuth(username, password), headers=headers, data = json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        
        
    
    def resend_otp(self,credentials, reference):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            username = credentials['api_key']
            password = credentials['secret_key']
            url = f'{baseurl}/api/v1/disbursements/single/resend-otp'
        
            payload = {
                "reference": reference
            }
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, auth=HTTPBasicAuth(username, password), headers=headers, data = json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        
    
    def get_transfer_details(self,credentials, reference):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            username = credentials['api_key']
            password = credentials['secret_key']
            url = f'{baseurl}/api/v1/disbursements/single/summary?reference={reference}'
        
            payload = {}
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("GET", url, auth=HTTPBasicAuth(username, password), headers=headers, data = json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        
        
        
    def get_all_single_transfer(self,credentials, pageSize, pageNo):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            username = credentials['api_key']
            password = credentials['secret_key']
            url = f'{baseurl}/api/v1/disbursements/single/transactions?pageSize={pageSize}&pageNo={pageNo}'
        
            payload = {}
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("GET", url, auth=HTTPBasicAuth(username, password), headers=headers, data = json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        
    
    
    def get_wallet_balance(self,credentials):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            walletId = credentials['walletId']
            username = credentials['api_key']
            password = credentials['secret_key']
            url = f'{baseurl}/api/v1/disbursements/wallet-balance?walletId={walletId}'
        
            payload = {}
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("GET", url, auth=HTTPBasicAuth(username, password), headers=headers, data = json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        
    
    
    def create_invoice(self, credentials, amount, invoiceReference, description, customerEmail, customerName, expiryDate, paymentMethods, redirectUrl):
        
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            username = credentials['api_key']
            password = credentials['secret_key']
            contractCode = credentials['contract']
            url = f'{baseurl}/api/v1/invoice/create'
            
            payload = {
                "amount": amount,
                "invoiceReference": invoiceReference,
                "description": description,
                "currencyCode": "NGN",
                "contractCode": contractCode,
                "customerEmail": customerEmail,
                "customerName": customerName,
                "expiryDate": expiryDate,
                "paymentMethods": paymentMethods,
                
                "redirectUrl": redirectUrl
            }
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, auth=HTTPBasicAuth(username, password), headers=headers, data = json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
    
    
    def initiate_refund(self, token, credentials, refundReference, transactionReference, refundAmount, refundReason, customerNote):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            url = f'{baseurl}/api/v1/refunds/initiate-refund'
            payload = {
                "refundReference": refundReference,
                "transactionReference": transactionReference,
                "refundAmount": refundAmount,
                "refundReason": refundReason,
                "customerNote": customerNote
            }
            headers = {
                'Content-Type': 'application/json',
                'Authorization': token
                }

            response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
    
    
    def get_refund_status(self, token, credentials, transactionReference,):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            url = f'{baseurl}/api/v1/refunds/{transactionReference}'
            payload = {}
            headers = {
                'Content-Type': 'application/json',
                'Authorization': token
                }

            response = requests.request("GET", url, headers=headers, data = json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        
    
    
    def get_all_refund(self, token, credentials, page, size):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            url = f'{baseurl}/api/v1/refunds?page={page}&size={size}'
            payload = {}
            headers = {
                'Content-Type': 'application/json',
                'Authorization': token
                }

            response = requests.request("GET", url, headers=headers, data = json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        
    
    
    def create_sub_account(self, credentials, bankCode, accountNumber, email, splitPercentage):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            username = credentials['api_key']
            password = credentials['secret_key']
            url = f'{baseurl}/api/v1/sub-accounts'

            payload = json.dumps([
                {
                    "currencyCode": "NGN",
                    "bankCode": bankCode,
                    "accountNumber": accountNumber,
                    "email": email,
                    "defaultSplitPercentage": splitPercentage
                }
            ])
                                  
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, auth=HTTPBasicAuth(username, password), headers=headers, data = payload)

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        
        
        
    def get_sub_account(self, credentials):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            username = credentials['api_key']
            password = credentials['secret_key']
            url = f'{baseurl}/api/v1/sub-accounts'

            payload = {}
                                  
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("GET", url, auth=HTTPBasicAuth(username, password), headers=headers, data = payload)

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        
    
    
    def update_sub_account(self, credentials, subAccountCode, bankCode, accountNumber, email, splitPercentage):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            username = credentials['api_key']
            password = credentials['secret_key']
            url = f'{baseurl}/api/v1/sub-accounts'

            payload = {
                "subAccountCode": subAccountCode,
                "currencyCode": "NGN",
                "bankCode": bankCode,
                "accountNumber": accountNumber,
                "email": email,
                "defaultSplitPercentage": splitPercentage
            }               
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("PUT", url, auth=HTTPBasicAuth(username, password), headers=headers, data = json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        
    
    
    def delete_sub_account(self, credentials, subAccountCode):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            username = credentials['api_key']
            password = credentials['secret_key']
            url = f'{baseurl}/api/v1/sub-accounts/{subAccountCode}'

            payload = {}               
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("DELETE", url, auth=HTTPBasicAuth(username, password), headers=headers, data = json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        
        
        
    
    def one_time_payment(self, credentials, amount, customerName, customerEmail, paymentReference, paymentDescription, redirectUrl, paymentMethods):
        live = credentials['is_live']
        if live == True or live == False:
            baseurl = getlive(live)
            username = credentials['api_key']
            password = credentials['secret_key']
            contractCode = credentials['contract']
            url = f'{baseurl}/api/v1/merchant/transactions/init-transaction'
            famount = float(amount)
            payload = {
                "amount": famount,
                "customerName": customerName,
                "customerEmail": customerEmail,
                "paymentReference": paymentReference,
                "paymentDescription": paymentDescription,
                "currencyCode": "NGN",
                "contractCode":contractCode,
                "redirectUrl": redirectUrl,
                "paymentMethods": paymentMethods
            }               
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, auth=HTTPBasicAuth(username, password), headers=headers, data = json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return getlive(live)
        