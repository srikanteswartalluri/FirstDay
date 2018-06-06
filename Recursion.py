#calling the function/method itself inside the function

# def sum(i):
#     return i + sum(i-1)

# fibanocci series

# 1 1 2 3 5 8 ......
# fib(1) = 1
# fib(2) = 1, 1
# fib(3) = 1, 1, 2
# fib(4) = 1, 1, 2, 3
# fib(5) = 1, 1, 2, 3, 5
#
# fib(5) =        fib(4), 5
#        = fib(3),    4 , 5
#        = fib(2), 3, 4 , 5
#        = fib(1), 2 ,3 ,4, 5

#factorial of a number
# fact(1) =             1
#fact(2) =          2 * 1
# fact(3) =     3 * 2 * 1
# fact(4) = 4 * 3 * 2 * 1
# fact(4) = 4 * fact(3)
#         = 4 * 3 * fact(2)
#         = 4 * 3 * 2 * fact(1)
#         = 4 * 3 * 2 * 1


#with recursion
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

#without recursion
n = 3
factorial = 1
for i in range(1,n+1):
    factorial = factorial * i

print(factorial)



# res = fact(6)
#
# print(res)

# fact(1)
#
# fact(2)

res = fact(3)
print(res)




