#lambda functions

a = 1

def doublevalues(i):
    return a*2

print(doublevalues(a))

b = doublevalues(a)

c = lambda a: a * 2

d = lambda e: e ** 2

result = d(4)
print(result)

print(c(4))

print("b : {}".format(b))
print("c : {}".format(c(a)))

