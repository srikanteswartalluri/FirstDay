a = [1, 2, 3 , 4 , 5, 6, 7, 8, 9]

print(a)

print(type(a))

#accessing elements in a list
# access element at index 2
print(a[2])
#print(a[45])

#different types of elements
b = [1, "alex", 2.4]
print(b)

#assign a value at an index

b[1] = "marina"


print(b)

#find the length of a list

print(len(b))

#slicing

print(a[:8])
print(a[3:5])
c = a[3:5]

print(c)

#delete an element
print(a)
del a[2]

print(a)

#append

l1 = [1,2,3,4]
print(l1)
l2 = [5, 6, 7]
# l1.append(l2)
# print(l1)
# l1.append(8)
# print(l1)
#
# print(l1[4])

l3 = l1 + l2
print(l3)

print(l3[::-1]) #reverse

print(l3)
print(l3[:])
print(l3[::2])

print(l3[-1])
print(l3[-2])
print(max(l3))
print(min(l3))


#iterating through a list
for element in l3:
    print(element)

if 3 in l3:
    print("found")
else:
    print("not found")

a = [4,5]
print(a*4)
