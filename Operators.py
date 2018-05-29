a = 10
b = 2

# addition

c = a + b
print("{} {} {} = {} ".format(a, "+", b, c))
# subtraction

c = a - b

# Multiplication

c = a * b

# Division

c = a / b

# Modulus

c = a % b

print(c)

#exponent

c = a ** b
print("exponent")
print(c)


a = "Hello"
b = "Srikant"
#string concatenation
c = a + b

#TODO: please print "Hello Srikant" add a space in between two strings
print(c)

rows = 5
for line in range(1, rows+1):
    #print spaces
    for space in range(rows-line):
        print " ",
    #print stars
    for j in range((2*line - 1)):
        print "*",
    print("\n")





