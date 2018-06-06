#open the file
f = open("desc_file")
g = open("new_desc_file", 'a') #append

# conversion = {"first" : "1st",
#               "second" : "2nd",
#               "third" : "3rd",
#               "four" : "4th",
#               "fifth" : "5th"}

lines = f.readlines()

for line in lines:
    # if line has "first" replace it with "1st" ex: conversion["first"]
    if line.

    g.write(line)


f.close()
g.close()
