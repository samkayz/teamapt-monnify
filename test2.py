from monnify.monnify import \
    (
        MonnifyCredential,
        OneTimePayment,
        CustomerReservedAccount,
        Disbursement,
        Invoicing,
        SubAccount,
        Refund
     )

api_key = "MK_TEST_8UBXGKTFSB"
secret_key = "ENRC4FDYKSTUYQKA53YPXBFLUFXWYHG2"
contractCode = '2917634474'
walletId = '654CAB2118124760A659C787B2AA38E8'

credentials = MonnifyCredential(api_key, secret_key, contractCode, walletId, is_live=False)

# token = x.get_token()
# print(x.secretKey)

# print(token)

# transfer = reserve.tranfer(x, amount='1000', reference='66635525333', narration='Test Transfer', bankCode='044', accountNumber='0020657879')
# print(transfer)

# bank_verify = reserve.verify_account(credentials, accountNumber='0020657879', bankCode='044')
# print(bank_verify)

reserve = CustomerReservedAccount(credentials=credentials)
reserve_account = reserve.reserve_account(
    payload=dict(
        accountReference='tw663533',
        accountName='Samson Olu',
        customerEmail='olusam@gmail.com',
        customerName="Samson Olu",
        bvn='66377273233',
        getAllAvailableBanks=True
    )
)
print(reserve_account)

# get_transfer = reserve.get_transfer_details(x, reference='66635525333')
# print(get_transfer)
# get_all_single = reserve.get_all_single_transfer(x, pageSize=1, pageNo=1)
# print(get_all_single)

# walletBal = reserve.get_wallet_balance(credentials)
# print(walletBal)

# create_invoice = reserve.create_invoice(x, amount='1000', invoiceReference='uueyyws', description='test invoice', customerEmail='test@gmail.com', customerName='Samson', expiryDate='2021-09-30 12:00:00', paymentMethods=['CARD', 'ACCOUNT_TRANSFER'], redirectUrl='')
# print(create_invoice)

# refund_money = reserve.initiate_refund(credentials, refundReference='6637whhhwe', transactionReference='MNFY|96|20210918092618|000615', refundAmount='1000.0', refundReason='Order cancelled!', customerNote='Canceled', destinationAccountNumber='2211440871', destinationAccountBankCode='057')
# print(refund_money)

# one_time_payment = reserve.one_time_payment(x, amount='1000', customerName='Samson Akin', customerEmail='ilemobayosamson@gmail.com', paymentReference='77uuuwyyq', paymentDescription='Test Payment', redirectUrl='http://savitechng.com', paymentMethods=['ACCOUNT_TRANSFER', 'CARD'])
# print(one_time_payment)

# initiate_card = reserve.initialize_card(
#     credentials=credentials,
#     payload={
#           "amount": 100.00,
#           "customerName": "Stephen Ikhane",
#           "customerEmail": "stephen@ikhane.com",
#           "paymentReference": "123031klsadkad",
#           "paymentDescription": "Trial transaction",
#           "currencyCode": "NGN",
#           "contractCode":"2917634474",
#           "redirectUrl": "https://my-merchants-page.com/transaction/confirm",
#           "paymentMethods":["CARD","ACCOUNT_TRANSFER"]
#         }
#     )
# print(initiate_card)
# card_payment = reserve.pay_with_card(
#     credentials=credentials,
#     transaction_ref="MNFY|38|20230211175101|000058",
#     collection_channel="API_NOTIFICATION",
#     card_details=dict(
#         number="4111111111111111",
#         expiryMonth="10",
#         expiryYear="2022",
#         pin="1234",
#         cvv="122"
#     )
# )
# print(card_payment)