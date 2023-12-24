#!/usr/bin/python3 env
#https://freecurrencyapi.com/

import requests
API_KEY = 'Your Api Key'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ['USD','CAD','EUR','AUD','CNY','INR']

def convert_currency(base):
  currencies = ",".join(CURRENCIES)
  url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
  try:
    response = requests.get(url)
    data = response.json()
    return data
  except Exception as e:
    print(e)
    return None

while True:
  base = input("Enter a base currency (q for quit)").upper()
  if(base == 'Q'):
    exit()

   
  data = convert_currency(base)
  for ticker, value in data.items():
    print(f"{ticker}: {value}")
    

