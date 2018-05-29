#for loop
# while loop

a = "Alex"

for ch in a:
    print(ch)

l = len(a)
count = 0
print(l)

while count < l:
    print(a[count])
    #increment count by 1 in each iteration
    count = count + 1

#
#          A l e x
# count -> 0 1 2 3
#
#     l -> 4

print(a[0]) #prints 'A'
print(a[1]) #prints 'l'


# 1
# 1 2
# 1 2 3
# 1 2 3 4

# loop to print numbers until line count
# another loop to print a new line \n

lines = 6

for i in range(1,lines): #decides how many number of lines you want to print
    #print numbers equal to the line number
    for j in range(1,i+1): #prints numbers equal to line number
        print j,  # if you are using python 3   =>   print(j, end="")
    #printing newline after each line
    print "\n"
