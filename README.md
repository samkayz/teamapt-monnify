                                  MONNIFY PYTHON LIBRARY USER GUIDE
                                            Version 1.0.0

Monnify is one of the products of TeamApt <https://www.teamapt.com/> . Monnify empowers businesses in the formal & informal sectors with the right tools & solutions to manage their finances and grow their businesses. Businesses in the formal economy benefit from our payment infrastructure that simplifies how they accept, manage and make payments. While smaller-scale businesses and entrepreneurs benefit from our market-community focused products that give them accessible, affordable and convenient short term working capital.

                                  MONNIFY PYTHON LIBRARY USER GUIDE

Before you can start integrating to Monnify, you will need to sign up on Monnify. Click <https://app.monnify.com/create-account> to sign up. After successful registration, login and for your credentials. 

                                            CREDENTIAL NEEDED

1. API KEY
2. SECRET KEY
3. CONTRACT
4. WALLET ID

All this can be seen on the setting area when you login to you logged in.


                                            API ENDPOINT IN THE LIBRARY
                                            
1. monnifyCredential
2. get_token
3. verify_account
4. reserve_account
5. add_link_account
6. update_bvn_reserve
7. deallocate_account
8. transactions
9. tranfer
10. authorize_tranfer
11. resend_otp
12. get_transfer_details
13. get_all_single_transfer
14. get_wallet_balance
15. create_invoice
17. initiate_refund
18. get_refund_status
19. get_all_refund
20. create_sub_account
21. get_sub_account
22. update_sub_account
23. delete_sub_account
24. one_time_payment

                                            HOW TO USE THE LIBRARY
To use the library, we have to use package installer (pip) by running: pip install teamapt-monnify

After successfull installation, we can now use the package in our development by importing it in our script


            from monnify.monnify import monnifyCredential, get_token, Monnify

            monnify = Monnify()

            api_key = "MK_TEST_8UBXGKTYYYWB"
            secret_key = "ENRC4FDYYYETKA53YPXBFLUFXWYHG2"
            contractCode = '2917634883'
            walletId = '654CAB211YY36760A659C787B2AA38E8'

            merchant_credential = monnifyCredential(api_key, secret_key, contractCode, walletId, is_live=False)

            NOTE: If you are in sandbox please is_live = False and can only be set to True when you are in 
                  production and make sure you change credentials to live credentials

            token = get_token(merchant_credential)



          1.VERIFY BANK ACCOUNT - This allows you check if an account number is a valid NUBAN, get the account name if valid.

            bank = monnify.verify_account(merchant_credential, accountNumber='2213324087', bankCode='057')
            print(bank)

            {
              'requestSuccessful': True, 
              'responseMessage': 'success', 
              'responseCode': '0', 
              'responseBody': {
                'accountNumber': '2213324087', 
                'accountName': 'SAMSON   ILEMOBAYO', 
                'bankCode': '057'
              }
            }
          
          2 INVOICE - Monnify invoicing allows you generate invoices via APIs. For each invoice, 
                      a virtual account number will be generated and tied to that invoice so your 
                      customers can simply transfer to that account number to pay

            create_invoice = monnify.create_invoice(merchant_credential, amount='1000', invoiceReference='uueyyws', description='test invoice', 
            customerEmail='test@gmail.com', customerName='Samson', expiryDate='2021-04-30 12:00:00', paymentMethods=['CARD', 'ACCOUNT_TRANSFER'], 
            redirectUrl='http://abc.com')
            print(create_invoice)

            {
              'requestSuccessful': True, 
              'responseMessage': 'success', 
              'responseCode': '0', 
              'responseBody': {
                'amount': 1000, 
                'invoiceReference': 'uueyyws', 
                'invoiceStatus': 'PENDING', 
                'description': 'test invoice', 
                'contractCode': '2917634883', 
                'customerEmail': 'test@gmail.com', 
                'customerName': 'Samson', 
                'expiryDate': '2021-04-30 12:00:00', 
                'createdBy': 'MK_TEST_8UBXGKTFSB', 
                'createdOn': '2021-04-14 15:18:31', 
                'checkoutUrl': 'https://sandbox.sdk.monnify.com/checkout/MNFY|63|20210414151813|000197', 
                'accountNumber': '3000041788', 
                'accountName': 'tes', 
                'bankName': 'Wema bank', 
                'bankCode': '035', 
                'redirectUrl': 'http://abc.com'
              }
            }

          3 RESERVE ACCOUNT - Reserved account APIs enable merchants create accounts that can be dedicated 
                              to each of their customers. Once any payment is done to that account, we 
                              notify your webhook with the payment information


            reserve_account = monnify.reserve_account(token, merchant_credential, accountReference='tw663552ppw', accountName='Test Account', 
            customerEmail='test2@gmail.com', customerName="Test Account", customerBvn='66377273233', availableBank=True)
            print(reserve_account)

            {
              'requestSuccessful': True, 
              'responseMessage': 'success', 
              'responseCode': '0', 
              'responseBody': {
                'contractCode': '2917634883', 
                'accountReference': 'tw663552ppw', 
                'accountName': 'Tes', 
                'currencyCode': 'NGN', 
                'customerEmail': 
                'test2@gmail.com', 
                'customerName': 'Test Account', 
                'accountNumber': '3000041799', 
                'bankName': 'Wema bank', 
                'bankCode': '035', 
                'collectionChannel': 'RESERVED_ACCOUNT', 
                'reservationReference': 'CHVQBNP3DRTGU6CZFXQW', 
                'reservedAccountType': 'GENERAL', 
                'status': 'ACTIVE', 
                'createdOn': '2021-04-14 15:29:51.976', 
                'incomeSplitConfig': [], 
                'bvn': '66377273233', 
                'restrictPaymentSource': False
              }
            }

            NOTE: When the availableBank is set to True,random account number amount there partner bank will be reserved. if you want to
                  to reserved you choice of bank e.g WEMA, you have to set the availableBank to the code of the bank you wish to reserve.
                  i.e availableBank='035'. available partner bank codes are (Rolez MFB = 50515, Wema Bank = 035, Sterling Bank = 232)

          
          4 ADD LINK ACCOUNT - This API allows you to add accounts with another partner bank and link to an existing customer 
                              with the customer's account reference.


            link_account = monnify.add_link_account(token, merchant_credential, accountReference='tw663552', getAllAvailableBanks=True, preferredBanks=['035'])
            print(link_account)

            {
              "requestSuccessful": true,
              "responseMessage": "success",
              "responseCode": "0",
              "responseBody": {
                  "contractCode": "915483727511",
                  "accountReference": "121615386005862",
                  "accountName": "reservedAccountName",
                  "currencyCode": "NGN",
                  "customerEmail": "nnaemekapaschal@gmail.com",
                  "customerName": "Pascool",
                  "accounts": [
                      {
                        "bankCode": "035",
                        "bankName": "WEMA Bank",
                        "accountNumber": "XXXX123456"
                      },
                      {
                        "bankCode": "50515",
                        "bankName": "ROLEZ MFB",
                        "accountNumber": "XXXX123456"
                      },
                      {
                        "bankCode": "123",
                        "bankName": "Bank 3",
                        "accountNumber": "XXXX123456"
                      }
                  ],
                  "collectionChannel": "RESERVED_ACCOUNT",
                  "reservationReference": "8MHKXZS8GCEPVXB59ML6",
                  "reservedAccountType": "GENERAL",
                  "status": "ACTIVE",
                  "createdOn": "2021-03-10 15:20:07.0",
                  "restrictPaymentSource": false
              }
            }

            NOTE: If getAllAvailableBanks is set to true, then an account with all available banks not yet linked will be added. 
            Set getAllAvailableBanks to false if you want to specify preferred banks to reserve accounts with. set to true if 
            you want to add all other available partner bank accounts to your reserved account.

          5 UPDATE BVN FOR RESERVE ACCOUNT - This Function is to be used to update a customer's BVN mapped to a Reserved Account.

            update_bvn = monnify.update_bvn_reserve(token, merchant_credential, bvn='66377283884', accountReference='635525663623')
            print(update_bvn)

            {
              "requestSuccessful": true,
              "responseMessage": "success",
              "responseCode": "0",
              "responseBody": {
                "contractCode": "2917634883",
                "accountReference": "635525663623",
                "currencyCode": "NGN",
                "customerEmail": "testuser@test.com",
                "customerName": "Test Oj",
                "accountNumber": "4290733572",
                "bankName": "Wema Bank",
                "bankCode": "035",
                "collectionChannel": "RESERVED_ACCOUNT",
                "reservationReference": "R8J4LCW3P82WN4X6LQCW",
                "reservedAccountType": "GENERAL",
                "status": "ACTIVE",
                "createdOn": "2021-02-01 21:40:55.0",
                "bvn": "66377283884",
                "restrictPaymentSource": false
              }
           }
          
          6 DEALLOCATE RESERVE ACCOUNT: This is used to deallocate/delete reserved account.

            delete_account = monnify.deallocate_account(token, merchant_credential, accountNumber='3000041799')
            print(delete_account)


            {
              "requestSuccessful": true,
              "responseMessage": "success",
              "responseCode": "0",
              "responseBody": {
                  "contractCode": "797854529434",
                  "accountReference": "reference12345#",
                  "accountName": "Test Reserved Account",
                  "currencyCode": "NGN",
                  "customerEmail": "test@tester.com",
                  "accountNumber": "3000041799",
                  "bankName": "Wema bank",
                  "bankCode": "035",
                  "reservationReference": "NRF72EMEBCGNN6WUKD35",
                  "status": "ACTIVE",
                  "createdOn": "2021-04-14 17:05:50.0"
                }
            }

            NOTE: Any Account deallocated/delete can not be reversed.
          
          7 TRANSFER: This is use to initiate transfer to bank

            transfer = monnify.tranfer(merchant_credential, amount='1000', reference='66635525', narration='Test Transfer', bankCode='044', accountNumber='0020657659')
            print(transfer)


            {
              "amount": 1000,
              "reference":"66635525",
              "narration":"Test Transfer",
              "destinationBankCode": "044",
              "destinationAccountNumber": "0020657659",
              "currency": "NGN",
              "sourceAccountNumber": "9624937372"
            }






