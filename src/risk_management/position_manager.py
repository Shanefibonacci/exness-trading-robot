# Position Manager

class PositionManager:
    def __init__(self, account_balance, risk_per_trade):
        self.account_balance = account_balance  # total account balance
        self.risk_per_trade = risk_per_trade  # risk per trade as a decimal (e.g., 0.01 for 1%)

    def calculate_position_size(self, stop_loss_distance):
        """
        Calculate the position size based on account balance, risk, and stop loss distance.

        :param stop_loss_distance: The distance to stop loss in pips or price units
        :return: Position size
        """
        risk_amount = self.account_balance * self.risk_per_trade
        position_size = risk_amount / stop_loss_distance
        return position_size

    def update_account_balance(self, amount):
        """
        Update the account balance by adding or subtracting a specified amount.

        :param amount: The amount to adjust the account balance
        """
        self.account_balance += amount

# Example usage:
# pm = PositionManager(account_balance=10000, risk_per_trade=0.01)
# position_size = pm.calculate_position_size(stop_loss_distance=50)
# print(f"Position Size: {position_size}")