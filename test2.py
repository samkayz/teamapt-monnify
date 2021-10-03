from monnify.monnify import MonnifyCredential, Monnify

reserve = Monnify()

api_key = "MK_TEST_8ZSVXMX9ZU"
secret_key = "GFHW6W69BREVLMBZ8FQ653W6KQHXFUXT"
contractCode = '2858152371'
walletId = '2269258532'

credentials = MonnifyCredential(api_key, secret_key, contractCode, walletId, is_live=False)

# token = x.get_token()
# print(x.secretKey)

# print(token)


# transfer = reserve.tranfer(x, amount='1000', reference='66635525333', narration='Test Transfer', bankCode='044', accountNumber='0020657879')
# print(transfer)

# bank_verify = reserve.verify_account(credentials, accountNumber='0020657879', bankCode='044')
# print(bank_verify)

# reserve_account = reserve.reserve_account(x, accountReference='tw663552', accountName='Samson Olu', customerEmail='olusam@gmail.com', customerName="Samson Olu", customerBvn='66377273233', availableBank=True)
# print(reserve_account)

# get_transfer = reserve.get_transfer_details(x, reference='66635525333')
# print(get_transfer)
# get_all_single = reserve.get_all_single_transfer(x, pageSize=1, pageNo=1)
# print(get_all_single)

walletBal = reserve.get_wallet_balance(credentials)
print(walletBal)

# create_invoice = reserve.create_invoice(x, amount='1000', invoiceReference='uueyyws', description='test invoice', customerEmail='test@gmail.com', customerName='Samson', expiryDate='2021-09-30 12:00:00', paymentMethods=['CARD', 'ACCOUNT_TRANSFER'], redirectUrl='')
# print(create_invoice)

# refund_money = reserve.initiate_refund(credentials, refundReference='6637whhhwe', transactionReference='MNFY|96|20210918092618|000615', refundAmount='1000.0', refundReason='Order cancelled!', customerNote='Canceled', destinationAccountNumber='2211440871', destinationAccountBankCode='057')
# print(refund_money)

# one_time_payment = reserve.one_time_payment(x, amount='1000', customerName='Samson Akin', customerEmail='ilemobayosamson@gmail.com', paymentReference='77uuuwyyq', paymentDescription='Test Payment', redirectUrl='http://savitechng.com', paymentMethods=['ACCOUNT_TRANSFER', 'CARD'])
# print(one_time_payment)