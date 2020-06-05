import requests  
from requests.auth import HTTPBasicAuth



import keys 

from accesstoken import get_access_token 
from encoded import decoded_password  
from utils import get_timestamp





  
  
  

  

def lipa_na_mpesa(): 
   formated_time = get_timestamp()

   
   decoded_pass = decoded_password(formated_time) 
  
   access_token = get_access_token()
   api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
   headers = { "Authorization": "Bearer %s" % access_token }
   request = {
        "BusinessShortCode": keys.business_short_code,
        "Password": decoded_pass,
        "Timestamp": formated_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_short_code,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://kiruiapp.com/lipanampesa/",
        "AccountReference": "123456",
        "TransactionDesc": "Pay haircut",
    }
    
   response = requests.post(api_url, json = request, headers=headers)
    
   print (response.text) 

   


lipa_na_mpesa()

  