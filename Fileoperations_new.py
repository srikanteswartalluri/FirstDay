f = open("desc_file", "r")

#read the entire
txt = f.read(6)

print(txt)

txt = f.read(3)
print(txt)

f.seek(0,0)
#begining of the file
print(f.read(6))

print(f.tell())

print(f.closed)
print(f.mode)
print(f.name)

f.close()