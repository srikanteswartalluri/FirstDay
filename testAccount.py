from account import Account
from userdefined_exceptions import AmountTooSmallException
from userdefined_exceptions import InsufficientBalanceException
a1 = Account("mike", 12345, 200)

balance = a1.checkBalance()
print("Balance in {}'s account is {}".format(a1.holder,
                                             balance))

success, balance = a1.deposit(1000)

print("Deposit status: {}".format(success))
print("Balance after deposit is {}".format(balance))

#success, balance = a1.deposit(10)

try:
    success, balance = a1.deposit(10)
except AmountTooSmallException as e:
    # print("give an amount greater than 50")
    print(e.message)


a1.withDraw(300)

try:
    a1.withDraw(2000000)
except InsufficientBalanceException as i:
    print(i.message)
    print("you tried to withdrew an amount of {}".format(i.amount))

