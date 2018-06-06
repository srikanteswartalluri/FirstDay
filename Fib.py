

#
# #1,1,2,3,5,8....
# n = 7
#
# l = []
#
# for i in range(n):
#     if i == 0 or i == 1:
#         l.append(1)
#         print("1")
#     else:
#         l.append(l[i-2] + l[i-1])
#         print(l[i-2] + l[i-1])

def fib_recursion(m):
    if m == 1 or m == 2:
        return 1
    else:
        return fib_recursion(m-1) + fib_recursion(m-2)

for i in range(1, 7):
    result = fib_recursion(i)
    print(result)