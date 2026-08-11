
from dotenv import load_dotenv
import requests
import os

load_dotenv()
def get_exchange_rate(base_currency, target_currency):
   api_key = os.environ.get("EXCHANGE_API_KEY")
   response = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}")
   data = response.json()
   if data["result"] == "success":
         exchange_rate = data["conversion_rates"][target_currency]
         return exchange_rate
   else:
         raise Exception("Error fetching exchange rate")
   
get_exchange_rate("PKR", "USD")