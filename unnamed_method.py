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


def mult_num4(i):
    return i*4

def mult_num5(i):
    return i*5

#unnamed method to return a number multiplied by a given number

m4 = lambda x: x*4
m5 = lambda x: x*5

#calling unnamed method
res = m4(6)
print(res)

res = m5(6)
print(res)


#returns a function
def func(m):
    return lambda x: x*m

doubler = func(2)  #doubler is a method  which is lambda x: x*2
tripler = func(3)  #tripler is a method  which is lambda x: x*3

p = 4
print(doubler(p))
print(tripler(p))
#print("Doubled: {} , Tripled: {}".format(doubler(p), tripler(p)))




