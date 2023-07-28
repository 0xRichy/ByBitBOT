from bybit_api import BybitAPI
from macd_indicator import MACDIndicator

class TradingBot:
    def __init__(self, symbol, quantity):
        self.api = BybitAPI()
        self.symbol = symbol
        self.quantity = quantity
        self.macd = None

    def run(self):
        while True:
            price = self.api.get_market_price(self.symbol)
            self.macd = MACDIndicator(price)
            self.trade()

    def trade(self):
        macd_line, signal_line = self.macd.calculate()
        if macd_line > signal_line:
            self.api.place_order("Market", self.symbol, "Buy", self.quantity, price)
        elif macd_line < signal_line:
            self.api.place_order("Market", self.symbol, "Sell", self.quantity, price)
