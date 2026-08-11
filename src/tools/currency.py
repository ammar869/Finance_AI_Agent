from langchain_core.tools import tools
from dotenv import load_dotenv
import requests
import os

load_dotenv()
@tools
def get_exchange_rate(base_currency:str, target_currency:str)-> float:
   """Fetches the exchange rate between two currencies using the ExchangeRate-API.""""
   api_key = os.environ.get("EXCHANGE_API_KEY")
   response = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}")
   data = response.json()
   if data["result"] == "success":
         exchange_rate = data["conversion_rates"][target_currency]
         return exchange_rate
   else:
         raise Exception("Error fetching exchange rate")
   
#print(get_exchange_rate("USD", "PKR"))
print(get_exchange_rate.args)