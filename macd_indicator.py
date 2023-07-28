import pandas as pd
import numpy as np

class MACDIndicator:
    def __init__(self, prices, short_period=12, long_period=26, signal_period=9):
        self.prices = prices
        self.short_period = short_period
        self.long_period = long_period
        self.signal_period = signal_period

    def calculate(self):
        exp1 = self.prices.ewm(span=self.short_period, adjust=False).mean()
        exp2 = self.prices.ewm(span=self.long_period, adjust=False).mean()
        macd_line = exp1 - exp2
        signal_line = macd_line.ewm(span=self.signal_period, adjust=False).mean()
        return macd_line, signal_line
