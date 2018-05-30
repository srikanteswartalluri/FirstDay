# file read
# file write and append
 # file delete

#open a file for reading
f = open("Sample")

text = f.read()
print(text)
f.close()

#open a file for reading
f = open("Sample")

# read first 10 characters in a  file
text = f.read(10)
print(text)
f.close()

#open a file for reading
f = open("Sample")
#read line by line
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

#open a file for reading
f = open("Sample", "r")

lines = f.readlines()
for line in lines:
    print(line)











f.close()


