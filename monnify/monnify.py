"""
This code is developed by Samson Ilemobayo.
Software Developer and Fintech Advocate
Email: ilemobayosamson@gmail.com
"""

import requests
import json
from requests.auth import HTTPBasicAuth
from . getlive import GetBaseUrl


class MonnifyCredential:
    """
    Function that get all the Monnify Credentials.
    The credential is then use to authenticate all
    the Endpoint for Use
    """
    def __init__(self, api_key, secret_key, contract, walletAccountNumber, is_live):
        self.apikey = api_key
        self.secretKey = secret_key
        self.contract = contract
        self.walletId = walletAccountNumber
        self.is_live = is_live

    def credentials(self):
        """
        This function is used to get credentials from user.
        visit https://monnify.com to get your credentials
        """
        data = (self.apikey, self.secretKey, self.contract, self.walletId, self.is_live)
        return data

    def get_token(self):
        """
        This function is used to log in, get token and prepared the token for use.
        """
        live = self.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            print(baseurl)
            username = self.apikey
            password = self.secretKey
            response = requests.post(f'{baseurl}/api/v1/auth/login',
            auth=HTTPBasicAuth(username, password))

            response_dict = json.loads(response.text)

            a = response_dict['responseBody']['accessToken']
            res = 'Bearer {}'
            token = res.format(a)

            self.tokens = token

            d = (self.tokens)
            return d
        else:

            return GetBaseUrl(live).urls()


class OneTimePayment:
    """
    If (for some reason) you don't want to use the web sdk, you can call the checkout APIs directly.
    You can use this API to charge your customer. Read more about this option
    here: https://teamapt.atlassian.net/wiki/spaces/MON/pages/213909255/Using+The+APIs+-+One+Time+Payments
    """
    def __init__(self, credentials):
        self.credentials = credentials

    def headers(self):
        return {
                'Content-Type': 'application/json',
                'Authorization': self.credentials.get_token()
            }

    def initialize_card(self, payload: dict):
        """
        This endpoint allows you to initialize a transaction on Monnify,
        and it returns a checkout URL which you can load within a browser
        to display the payment form to your customer. The checkout URL
        has an expiry time of 40 minutes.
        """
        required_fields = [
            "amount", "customerName",
            "customerEmail", "paymentReference",
            "paymentDescription", "currencyCode",
            "contractCode", "redirectUrl",
            "paymentMethods"]
        for field in required_fields:
            if field not in payload.keys():
                return dict(status=False, message=f"`{field}` is required in card details")

        if type(payload.get("paymentMethods")) != list:
            return dict(status=False, message="payment method must be a list ['CARD','ACCOUNT_TRANSFER']")

        live = self.credentials.is_live
        if live or not live:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/merchant/transactions/init-transaction'
            response = requests.request("POST", url, headers=self.headers(), data=json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict

        else:
            return GetBaseUrl(live).urls()

    def pay_with_card(
            self,
            transaction_ref: str,
            collection_channel: str = "API_NOTIFICATION",
            card_details: dict = None
    ):
        """
        To be granted access to this API, you will be required to be PCI-DSS certified.
        contact monnify team for inquiries
        :return: The response that will be gotten depends on the kind of card used for the transaction.
        There are cards charged with the use of an OTP, without an OTP, and also with 3DS Secure Authentication.
        An extra mandatory object parameter(deviceInformation) is required to capture the user’s  device information.
        See https://teamapt.atlassian.net/wiki/spaces/MON/overview to get more on card payment
        """
        required_card_fields = ["number", "expiryMonth", "expiryYear", "pin", "cvv"]
        for field in required_card_fields:
            if field not in card_details.keys():
                return dict(status=False, message=f"`{field}` is required in card details")

        live = self.credentials.is_live
        if live or not live:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/merchant/cards/charge'
            payload = dict(
                transactionReference=transaction_ref,
                collectionChannel=collection_channel,
                card=card_details
            )
            response = requests.request("POST", url, headers=self.headers(), data=json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict

        else:
            return GetBaseUrl(live).urls()

    def authorize_otp(self, payload: dict):
        """
        This endpoint is to be called whenever an OTP is to be authorized.
        """
        required_fields = ["transactionReference", "collectionChannel", "tokenId", "token"]
        for field in required_fields:
            if field not in payload.keys():
                return dict(status=False, message=f"`{field}` is required in card details")

        live = self.credentials.is_live
        if live or not live:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/merchant/cards/otp/authorize'
            response = requests.request("POST", url, headers=self.headers(), data=json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict

        else:
            return GetBaseUrl(live).urls()

    def secured_auth_3d(self, payload: dict):
        """
        To authorize charge on a users card using 3DS Secure Transactions,
        you make an authenticated post request providing transaction reference,
        collection channel, API key and card details to the 3DS Secure Transactions endpoint.
        """
        required_fields = ["transactionReference", "apiKey", "collectionChannel", "card"]
        for field in required_fields:
            if field not in payload.keys():
                return dict(status=False, message=f"`{field}` is required in the body")

        if type(payload.get('card')) != dict:
            return dict(status=False, message="card must be a dictionary and must contain the card details")

        card_required_fields = ["number", "expiryMonth", "expiryYear", "pin", "cvv"]
        for c_field in card_required_fields:
            if c_field not in payload.get('card').keys():
                return dict(status=False, message=f"`{c_field}` is required in card details")

        live = self.credentials.is_live
        if live or not live:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/sdk/cards/secure-3d/authorize'
            response = requests.request("POST", url, headers=self.headers(), data=json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict

        else:
            return GetBaseUrl(live).urls()

    def pay_with_ussd(self, payload: dict):
        """
        To get the USSD code of the desired bank, you simply need to pass the transaction reference
        to the endpoint above and also the desired bank code.
        :param credentials:
        :param payload:
        :return:
        """
        required_fields = ["transactionReference", "bankUssdCode"]
        for field in required_fields:
            if field not in payload.keys():
                return dict(status=False, message=f"`{field}` is required in the body")

        live = self.credentials.is_live
        if live or not live:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/merchant/ussd/initialize'
            response = requests.request("POST", url, headers=self.headers(), data=json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict

        else:
            return GetBaseUrl(live).urls()

    def pay_with_bank_transfer(self, payload: dict):
        required_fields = ["transactionReference", "bankCode"]
        for field in required_fields:
            if field not in payload.keys():
                return dict(status=False, message=f"`{field}` is required in the body")

        live = self.credentials.is_live
        if live or not live:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/merchant/bank-transfer/init-payment'
            response = requests.request("POST", url, headers=self.headers(), data=json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict

        else:
            return GetBaseUrl(live).urls()


class CustomerReservedAccount:
    """
    The Customer Reserved Account is used to reserve virtual account for customer which can be used to transact
    across all bank in Nigeria
    """
    def __init__(self, credentials):
        self.credentials = credentials

    def headers(self):
        return {
                'Content-Type': 'application/json',
                'Authorization': self.credentials.get_token()
                }

    def reserve_account(self, payload: dict):
        """
            This function is used to reserve virtual account on the monnify platform.
            It takes Auth Token, merchant credentials, account reference, accoun name,
            customer email, customer name, customer BVN, and available bank. this
            endpoint will then create a virtual account number in the name of customer
            supplied and return the details of the account created.
        """
        required_fields = ["accountReference", "accountName",
                           "customerEmail", "bvn", "customerName", "getAllAvailableBanks"]
        for field in required_fields:
            if field not in payload.keys():
                return dict(status=False, message=f"`{field}` is required in the payload")

        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v2/bank-transfer/reserved-accounts'
            payload['currencyCode'] = "NGN"
            payload['contractCode'] = self.credentials.contract
            response = requests.request("POST", url, headers=self.headers(), data=json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def add_link_account(self, accountReference, payload: dict):
        """
        This API allows you to add accounts with another partner bank and link to an existing
        customer with the customer's account reference.
        """
        required_fields = ["getAllAvailableBanks", "preferredBanks"]
        for field in required_fields:
            if field not in payload.keys():
                return dict(status=False, message=f"`{field}` is required in the payload")
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/bank-transfer/reserved-accounts/add-linked-accounts/{accountReference}'

            response = requests.request("PUT", url, headers=self.headers(), data=json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def update_bvn_reserve(self, accountReference, payload: dict):
        """
        This API is to be used to update a customer's BVN mapped to a Reserved Account
        :param accountReference:
        :param payload:
        :return:
        """
        required_fields = ["bvn"]
        for field in required_fields:
            if field not in payload.keys():
                return dict(status=False, message=f"`{field}` is required in the payload")
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/bank-transfer/reserved-accounts/update-customer-bvn/{accountReference}'
            response = requests.request("PUT", url, headers=self.headers(), data=json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def deallocate_account(self, accountNumber):
        """
        This method is used to deallocate or delete reserved account.
        NOTE: Once Account is deleted, it can not be retrieved again.
        :param accountNumber:
        :return:
        """
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/bank-transfer/reserved-accounts/{accountNumber}'
            payload = {}

            response = requests.request("DELETE", url, headers=self.headers(), data=json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def reserve_account_transactions(self, accountReference, page, size):
        """
        By specifying the accountReference as a query parameter, Monnify will return a paginated
        list of transactions processed to a reserved account. You can optionally define the
        number of pages and the size (number of transactions) of each page you want returned
        :param accountReference:
        :param page:
        :param size:
        :return:
        """
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/bank-transfer/reserved-accounts/transactions?accountReference={accountReference}&page={page}&size={size}'
            payload = {}

            response = requests.request("GET", url, headers=self.headers(), data=json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()


class Disbursement:
    """
    The Monnify Disbursements APIs enable a merchant to initiate payouts from his Monnify
    Wallet to any Nigerian bank account. We provide you with all the tools you'll need to
    fully automate your disbursement processes.
    """
    def __init__(self, credentials):
        self.credentials = credentials

    def headers(self):
        return {
                'Content-Type': 'application/json',
                'Authorization': self.credentials.get_token()
                }

    def tranfer(self, amount, reference, narration, bankCode, accountNumber):
        """
        This method is used for single transfer to any nigerian bank.
        if the merchant does not have Two-Factor Authentication (2FA) enabled,
        the transaction will be processed instantly.
        If the merchant has Two-Factor Authentication (2FA) enabled,
        a One Time Password (OTP) will be sent to the designated email address(es).
        That OTP will need to be supplied via the VALIDATE OTP REQUEST before the
        transaction can be approved
        :param amount:
        :param reference:
        :param narration:
        :param bankCode:
        :param accountNumber:
        :return:
        """
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            walletId = self.credentials.walletId
            username = self.credentials.apikey
            password = self.credentials.secretKey
            url = f'{baseurl}/api/v2/disbursements/single'

            f_amount = float(amount)
            payload = {
                'amount': f_amount,
                'reference': reference,
                'narration': narration,
                'destinationBankCode': bankCode,
                'destinationAccountNumber': accountNumber,
                'currency': 'NGN',
                'sourceAccountNumber': walletId
            }
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, auth=HTTPBasicAuth(username, password),
                                        headers=headers, data=json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def resend_otp(self, payload):
        """
        This endpoint will help you resend OTP’s in scenarios where your customers
        don’t get the previous ones sent or in cases of expiration.
        :param payload:
        :return:
        """
        required_fields = ["reference"]
        for field in required_fields:
            if field not in payload.keys():
                return f"`{field}` is required in the payload"
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            username = self.credentials.apikey
            password = self.credentials.secretKey
            url = f'{baseurl}/api/v1/disbursements/single/resend-otp'
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, auth=HTTPBasicAuth(username, password),
                                        headers=headers, data=json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def authorize_tranfer(self, payload: dict):
        """
        This method is used to validate OTP in a case where 2FA is activated
        :param payload:
        :return:
        """
        required_fields = ["reference", "authorizationCode"]
        for field in required_fields:
            if field not in payload.keys():
                return f"`{field}` is required in the payload"
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            username = self.credentials.apikey
            password = self.credentials.secretKey
            url = f'{baseurl}/api/v2/disbursements/single/validate-otp'
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, auth=HTTPBasicAuth(username, password),
                                        headers=headers, data=json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def get_transfer_details(self, reference):
        """
        This method is used to get details of a disbursement transaction
        :param reference:
        :return:
        """
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            username = self.credentials.apikey
            password = self.credentials.secretKey

            url = f'{baseurl}/api/v2/disbursements/single/summary?reference={reference}'

            payload = {}
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("GET", url, auth=HTTPBasicAuth(username, password),
                                        headers=headers, data=json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def get_all_single_transfer(self, pageSize, pageNo):
        """
        This method is used to get list of all single transaction
        :param pageSize:
        :param pageNo:
        :return:
        """
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            username = self.credentials.apikey
            password = self.credentials.secretKey
            url = f'{baseurl}/api/v2/disbursements/single/transactions?pageSize={pageSize}&pageNo={pageNo}'

            payload = {}
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("GET", url, auth=HTTPBasicAuth(username, password),
                                        headers=headers, data=json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def get_wallet_balance(self):
        """
        This endpoint allows you to get the available balance in your monnify wallet
        :return:
        """
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            walletId = self.credentials.walletId
            username = self.credentials.apikey
            password = self.credentials.secretKey
            url = f'{baseurl}/api/v2/disbursements/wallet-balance?accountNumber={walletId}'
            payload = {}
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, auth=HTTPBasicAuth(username, password),
                                        headers=headers, data=json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def verify_account(self, accountNumber, bankCode):
        """
        This is the endpoint that verify bank account, and it takes value of the merchant credentials
        account number to be verified and the bank code of the bank. this endpoint will run a check to
        verify whether the bank account number is valid by returning the name registered with the
        account number.
        """
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/disbursements/account/validate?accountNumber={accountNumber}&bankCode={bankCode}'

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()


class Invoicing:
    """
    Monnify invoicing allows you to generate invoices via APIs.
    For each invoice, we will generate a virtual account number
    tied to that invoice so your customers can simply transfer
    to that account number to pay. We will also return a checkout
    URL so your customers can pay via their Debit Cards.
    """
    def __init__(self, credentials):
        self.credentials = credentials

    def create_invoice(self, payload):
        """
        This method is used to creat invoice and sent to customer.
        When the request is sent, an account number will be returned.
        You should include that account number (and bank) on the invoice
        being sent to your customer. We also return a checkout URL which
        can be included on your invoices. This way customers who want to
        pay using their debit cards can simply click on the link and pay using
        the Monnify payment interface.
        :param payload:
        :return:
        """
        required_fields = ["amount", "invoiceReference", "description",
                           "customerEmail", "customerName", "expiryDate", "paymentMethods", "redirectUrl"]
        for field in required_fields:
            if field not in payload.keys():
                return f"`{field}` is required in the body"

        if type(payload.get('paymentMethods')) != list:
            return "paymentMethods must be list"

        payment_method = ["ACCOUNT_TRANSFER", "CARD"]
        for method in payload.get('paymentMethods'):
            if method not in payment_method:
                return f"`{method}` is not allowed. It can either be any of this {payment_method}"

        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            username = self.credentials.apikey
            password = self.credentials.secretKey
            url = f'{baseurl}/api/v1/invoice/create'
            payload['currencyCode'] = "NGN"
            payload['contractCode'] = self.credentials.contract
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, auth=HTTPBasicAuth(username, password),
                                        headers=headers, data=json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()


class SubAccount:
    """
    You can easily split a single payment across multiple accounts.
    This means for one transaction, Monnify can help you share the
    amount paid between up to 5 different accounts.

    In order to be able to split payments between subaccounts,
    you will need to create subaccounts. This can be done either
    through API’s or through the Monnify Dashboard.
    """
    def __init__(self, credentials):
        self.credentials = credentials

    def create_sub_account(self, payload: dict):
        """
        This method creates a subaccount for a merchant,
        allowing the merchant split transaction settlement
        between the main account and one or more subaccount(s)
        :param payload:
        :return:
        """
        required_fields = ["bankCode", "accountNumber", "email", "defaultSplitPercentage"]
        for field in required_fields:
            if field not in payload.keys():
                return f"`{field}` is required in the payload"

        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            username = self.credentials.apikey
            password = self.credentials.secretKey
            url = f'{baseurl}/api/v1/sub-accounts'
            payload['currencyCode'] = "NGN"
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, auth=HTTPBasicAuth(username, password),
                                        headers=headers, data=json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def get_sub_account(self):
        """
        This method returns a list of subaccounts previously created by the merchant.
        :return:
        """
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            username = self.credentials.apikey
            password = self.credentials.secretKey
            url = f'{baseurl}/api/v1/sub-accounts'
            payload = {}
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, auth=HTTPBasicAuth(username, password),
                                        headers=headers, data=payload)
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def update_sub_account(self, payload):
        """
        This endpoint updates the information on an existing sub-account for a merchant.
        :param payload:
        :return:
        """
        required_fields = ["subAccountCode", "bankCode", "accountNumber", "email", "splitPercentage"]
        for field in required_fields:
            if field not in payload.keys():
                return f"`{field}` is required in the payload"
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            username = self.credentials.apikey
            password = self.credentials.secretKey
            url = f'{baseurl}/api/v1/sub-accounts'
            payload['currencyCode'] = "NGN"
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("PUT", url, auth=HTTPBasicAuth(username, password),
                                        headers=headers, data=json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def delete_sub_account(self, subAccountCode):
        """
        This endpoint deletes a merchant’s sub-account
        :param subAccountCode:
        :return:
        """
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            username = self.credentials.apikey
            password = self.credentials.secretKey
            url = f'{baseurl}/api/v1/sub-accounts/{subAccountCode}'

            payload = {}
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("DELETE", url, auth=HTTPBasicAuth(username, password),
                                        headers=headers, data=json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

class Monnify:
    def __init__(self, credentials):
        self.credentials = credentials

    def headers(self):
        return {
                'Content-Type': 'application/json',
                'Authorization': self.credentials.get_token()
                }

    def initiate_refund(
            self,
            refundReference,
            transactionReference,
            refundAmount,
            refundReason,
            customerNote,
            destinationAccountNumber,
            destinationAccountBankCode
    ):
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/refunds/initiate-refund'
            payload = {
                "refundReference": refundReference,
                "transactionReference": transactionReference,
                "refundAmount": refundAmount,
                "refundReason": refundReason,
                "customerNote": customerNote,
                "destinationAccountNumber": destinationAccountNumber,
                "destinationAccountBankCode": destinationAccountBankCode
            }

            response = requests.request("POST", url, headers=self.headers(), data = json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def get_refund_status(self, transactionReference,):
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/refunds/{transactionReference}'
            payload = {}
            response = requests.request("GET", url, headers=self.headers(), data=json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def get_all_refund(self, page, size):
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/refunds?page={page}&size={size}'
            payload = {}
            response = requests.request("GET", url, headers=self.headers(), data=json.dumps(payload))
            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def one_time_payment(
            self,
            amount,
            customerName,
            customerEmail,
            paymentReference,
            paymentDescription,
            redirectUrl,
            paymentMethods
    ):
        live = self.credentials.is_live
        if live == True or live == False:
            baseurl = GetBaseUrl(live).urls()
            url = f'{baseurl}/api/v1/merchant/transactions/init-transaction'
            famount = float(amount)
            payload = {
                "amount": famount,
                "customerName": customerName,
                "customerEmail": customerEmail,
                "paymentReference": paymentReference,
                "paymentDescription": paymentDescription,
                "currencyCode": "NGN",
                "contractCode": self.credentials.contract,
                "redirectUrl": redirectUrl,
                "paymentMethods": paymentMethods
            }
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url,
                                        auth=HTTPBasicAuth(self.credentials.apikey, self.credentials.secretKey),
                                        headers=headers, data=json.dumps(payload))

            r_dict = json.loads(response.text)
            return r_dict
        else:
            return GetBaseUrl(live).urls()

    def webhook(self, request):
        request_json = request.body.decode('utf-8')
        body = json.loads(request_json)
        return body
