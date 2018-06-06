class AmountTooSmallException(Exception):
    def __init__(self, amount):
        self.amount = amount
        self.message = "Deposited amount should be greater than 50$"

class InsufficientBalanceException(Exception):
    def __init__(self, amount):
        self.amount = amount
        self.message = "Your account doesn't have enough Balance"




