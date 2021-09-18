from monnify.monnify import monnifyCredential, get_token, Monnify

reserve = Monnify()

api_key = "MK_TEST_8UBXGKTFSB"
secret_key = "ENRC4FDYKSTUYQKA53YPXBFLUFXWYHG2"
contractCode = '2917634474'
walletId = '654CAB2118124760A659C787B2AA38E8'


login_credential = monnifyCredential(api_key, secret_key, contractCode, walletId, is_live=000)
# print(login_credential)
token = get_token(login_credential)
# print(token)

# create_invoice = reserve.create_invoice(login_credential, amount='1000', invoiceReference='uueyyws', description='test invoice', customerEmail='test@gmail.com', customerName='Samson', expiryDate='2021-04-30 12:00:00', paymentMethods=['CARD', 'ACCOUNT_TRANSFER'], redirectUrl='')
# print(create_invoice)

# bank_verify = VerifyAccount(login_credential, accountNumber='0020657879', bankCode='044')
# print(bank_verify)

# reserve_account = reserve.reserve_account(token, login_credential, accountReference='tw663552', accountName='Samson Olu', customerEmail='olusam@gmail.com', customerName="Samson Olu", customerBvn='66377273233', availableBank=True)
# print(reserve_account)


# link_account = reserve.add_link_account(token, login_credential, accountReference='tw663552', getAllAvailableBanks=True, preferredBanks=[''])
# print(link_account)

# update_bvn = reserve.update_bvn_reserve(token, login_credential, bvn='66377283884', accountReference='635525663623')
# print(update_bvn)

# delete_account = reserve.deallocate_account(token, login_credential, accountNumber='3000040408')
# print(delete_account)

# alltrans = reserve.reserve_account_transactions(token, login_credential, accountReference='08039440154', page=0, size=10)
# print(alltrans)

# refund_money = refund.initiate_refund(token, login_credential, refundReference='6637whhhwe', transactionReference='MNFY|63|20210413134205|000113', refundAmount='1000.0', refundReason='Order cancelled!', customerNote='Canceled')
# print(refund_money)

# get_refund_status = refund.get_refund_status(token, login_credential, transactionReference='MNFY|63|20210413134205|000113')
# print(get_refund_status)

# get_all_refund = reserve.get_all_refund(token, login_credential, page=0, size=10)
# print(get_all_refund)

# create_sub_account = reserve.create_sub_account(login_credential, bankCode='044', accountNumber='0020657879', email='ilemobayosamson@gmail.com', splitPercentage='20')
# print(create_sub_account)

# get_sub_account = reserve.get_sub_account(login_credential)
# print(get_sub_account)

# update_sub_account = reserve.update_sub_account(login_credential, subAccountCode='MFY_SUB_248731941563', bankCode='057', accountNumber='2211440871', email='ilemobayosamson@gmail.com', splitPercentage='23')
# print(update_sub_account)

# delete_sub_account = reserve.delete_sub_account(login_credential, subAccountCode='MFY_SUB_248731941563')
# print(delete_sub_account)

# one_time_payment = reserve.one_time_payment(login_credential, amount='1000', customerName='Samson Akin', customerEmail='ilemobayosamson@gmail.com', paymentReference='77uuuwyyq', paymentDescription='Test Payment', redirectUrl='http://savitechng.com', paymentMethods=['ACCOUNT_TRANSFER', 'CARD'])
# print(one_time_payment)

# transfer = reserve.tranfer(login_credential, amount='1000', reference='66635525', narration='Test Transfer', bankCode='044', accountNumber='0020657879')
# print(transfer)

# authorize = reserve.authorize_tranfer(login_credential, reference='66635525', authorizationCode='725006')
# print(authorize)

# resendOtp = reserve.resend_otp(login_credential, reference='66635525')
# print(resendOtp)

# get_transfer = reserve.get_transfer_details(login_credential, reference='66635525')
# print(get_transfer)

get_all_single = reserve.get_all_single_transfer(login_credential, pageSize=5, pageNo=1)
print(get_all_single)


# walletBal = reserve.get_wallet_balance(login_credential)
# print(walletBal)

# bank = reserve.verify_account(login_credential, accountNumber='2211440871', bankCode='057')
# print(bank)