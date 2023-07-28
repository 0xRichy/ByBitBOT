import requests
from dotenv import load_dotenv
import os

load_dotenv()

class BybitAPI:
    def __init__(self):
        self.base_url = "https://api.bybit.com"
        self.api_key = os.getenv("BYBIT_API_KEY")
        self.api_secret = os.getenv("BYBIT_API_SECRET")

    def get_market_price(self, symbol):
        response = requests.get(f"{self.base_url}/v2/public/tickers?symbol={symbol}")
        return response.json()["result"]["last_price"]

    def place_order(self, order_type, symbol, side, quantity, price):
        data = {
            "api_key": self.api_key,
            "symbol": symbol,
            "side": side,
            "order_type": order_type,
            "qty": quantity,
            "price": price,
            "time_in_force": "GoodTillCancel"
        }
        response = requests.post(f"{self.base_url}/v2/private/order/create", data=data)
        return response.json()

    def get_balance(self):
        data = {"api_key": self.api_key}
        response = requests.get(f"{self.base_url}/v2/private/wallet/balance", params=data)
        return response.json()["result"]["BTC"]["available_balance"]
