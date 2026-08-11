from langchain_core.tools import tool
from dotenv import load_dotenv
import requests
import os

load_dotenv()
@tool
def get_exchange_rate(base_currency:str, target_currency:str)-> float:
   """Fetches the exchange rate between two currencies using the ExchangeRate-API."""
   api_key = os.environ.get("EXCHANGE_API_KEY")
   response = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}")
   data = response.json()
   if data["result"] == "success":
         exchange_rate = data["conversion_rates"][target_currency]
         return exchange_rate
   else:
         raise Exception("Error fetching exchange rate")
   
result = get_exchange_rate.invoke({
    "base_currency": "USD",
    "target_currency": "EUR"
})

print(result)
