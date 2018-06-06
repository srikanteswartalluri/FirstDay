from userdefined_exceptions import AmountTooSmallException
from userdefined_exceptions import InsufficientBalanceException
class Account:
    'this is a class for Bank Account'

    def __init__(self, holder, number, balance):
        self.holder = holder
        self.number = number
        self.balance = balance

    #checkBalance
    def checkBalance(self):
        #print("The balance is {}".format(self.balance))
        return self.balance

    #withDrawal
    def withDraw(self, amount):
        if amount > self.balance:
            iexception = InsufficientBalanceException(amount)
            raise iexception
        else:
            self.balance = self.balance - amount


    #if the balance is sufficient then withdrawal should be succesful
    #otherwise fail

    #deposit
    def deposit(self, amount):
        if amount < 50:
            a = AmountTooSmallException(amount)
            raise a
        self.balance = self.balance + amount
        #print("Deposit is succesful and balance is {}".format(self.balance))
        return True, self.balance


