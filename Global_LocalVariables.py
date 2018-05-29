def marina_method(i):
    i = 10 #local to this method
    print(i)
    i = 30
    print(i)

i = 20 #global variable
print(i)

marina_method(i)

print(i)


