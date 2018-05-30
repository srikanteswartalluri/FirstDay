import os
#open the file to write

# f = open("newfile", "w")
# f.write("writing the file using python")
# f.write("new write")
#
# f.close()
#
# f = open("newfile", "w")
# f.write("overwriting the file content")
# f.close()

#open a file to append the content
f = open("newfile", "a")
f.write("\nwriting the file\t from python")
f.close()


#read the file
f = open("newfile")
print(f.read())
f.close()

#remove the file
os.remove("newfile")