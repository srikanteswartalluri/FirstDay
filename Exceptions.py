try:
    f = open("testfile", 'r')
    #p = 2/0
    #raise IOError
    #assert 2 == 3
    [] + 3

#IOError,ZeroDivisionError,AssertionError
except  Exception as p:
    print("EXCEPT: exception {}".format(p.message) )
    print("argument : {}".format(p.args))
    # print("EXCEPT: Assertion error")
    # print("EXCEPT: either a zerodivision error or ")
    # print("Not able to open file for read")
    # print("check whether the file is present or not")
else:
    print("ELSE: I am able to read the file")
finally:
    print("FINALLY: It executes whether an exception is "
          "occured or not")





# f = open("testfile", 'r')

print("execution continues")