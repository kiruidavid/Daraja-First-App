import requests 
import keys 
from requests.auth import HTTPBasicAuth 
from accesstoken import get_access_token


 

def register_url():
  
    access_token = get_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
             "ShortCode": keys.shortcode,
             "ResponseType": "Completed",
             "ConfirmationURL": "https://kiruiapp.com/confirmation/",
             "ValidationURL": "https://kiruiapp.com/validation/"
            }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text) 

#register_url() 

def simulate_c2b(): 

  access_token = get_access_token()
  api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
  headers = {"Authorization": "Bearer %s" % access_token}
  request = { "ShortCode":keys.shortcode,
    "CommandID":"CustomerPayBillOnline",
    "Amount":"1",
    "Msisdn":keys.test_msisdn,
    "BillRefNumber":"123456" }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)


simulate_c2b()
  