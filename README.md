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

            token = get_token(merchant_credential)

                  VERIFY BANK ACCOUNT
                                                        
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






