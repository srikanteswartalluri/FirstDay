d = { "name" : "john",
      "age"  : 20,
      "occupation": "student"
}

print(d)

#accessing each element
print(d["age"])

#changing a value for a key
d["age"] = 40

print(d)

del d["age"]

print(d)

#iterating through key value pairs
for key, value in d.items():
    print("{} : {}".format(key, value))

a = d.keys()
print("keys: {}".format(a))
b = d.values()
print("values: {}".format(b))

print(d.has_key("name"))

# d["age"]

if d.has_key("age"):
    print(d["age"])
else:
    print("key not present")


