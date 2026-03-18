class TradingStrategy:
    def __init__(self, lot_size=0.01):
        self.lot_size = lot_size
        self.position = None

    def generate_signal(self, market_data):
        # Basic signal generation logic
        # Replace with actual trading signal logic based on market data
        if market_data['signal'] == 'buy':
            return 'buy'
        elif market_data['signal'] == 'sell':
            return 'sell'
        return None

    def manage_trade(self, signal):
        # Trade management logic
        if signal == 'buy' and self.position != 'long':
            self.open_buy_trade()
        elif signal == 'sell' and self.position != 'short':
            self.open_sell_trade()
        elif signal is None and self.position:
            self.close_trade()

    def open_buy_trade(self):
        self.position = 'long'
        print(f"Opening buy trade with lot size: {self.lot_size}")

    def open_sell_trade(self):
        self.position = 'short'
        print(f"Opening sell trade with lot size: {self.lot_size}")

    def close_trade(self):
        print(f"Closing trade: {self.position}")
        self.position = None

# Example usage:
# strategy = TradingStrategy()
# market_data = {'signal': 'buy'}
# signal = strategy.generate_signal(market_data)
# strategy.manage_trade(signal)