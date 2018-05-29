# #  def <nameofthemethod> <parameters>:
# #      return
#
# #method to add two numbers and print the result
# def add(i, j = 10): #default argument
#     print("add function")
#     print(i+j)
#
# def sub(i, j):
#     print("sub function")
#     print(i-j)
#
#
# def subtract(i, j):
#     return i-j
#
#
# add(2,3)
# sub(4, 3)
# add(3, 6)
# add(10, 11)
#
# add("marina", "student")
#
# result = subtract(10, 6)
# print(result)
#
# add(9)
# add(9, 9)
#
#
# # method to multiply two numbers
# def multiply(first ,second = 7 ):
#     return first * second
#
#
# mult_result = multiply(10, 3)
# print(mult_result)
# mult_result = multiply(6)
# print(mult_result)
#
# mult_result = multiply(5)
# print(mult_result)
#
# #add(1,2)
# #add(1,2,3)
# #add(1,2,3,6)
# #add(12,34,54,36,66)

#variable number of argument
def add(first, *args):
    sum = 0
    print("first arg: {}".format(first))
    sum = sum + first
    for k in args:
        print(k)
        sum = sum + k

    print("Final result {}".format(sum))


add(1, 2, 3, 4)

#keyword arguments
#addy(first=10, second=20, third=30)
def addy(*positions, **kwargs):
    print positions
    print str(kwargs)



addy("one", "two", "three", first=10, second=50, third=60)










