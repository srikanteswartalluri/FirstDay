from person import Person
#creating objects/instances of a class

p1 = Person("20", "John", "male")
p2 = Person("25", "Serena", "female")
p3 = Person("23", "Selena", "female")
print(p1.age)
print(p1.name)
print(p1.gender)

print(p2.age)
print(p2.name)
print(p2.gender)

#calling methods of an object
p1.talk("good morning")

p1.run()

p1.walk()

p1.setAge(33)

age = p1.getAge()

print(age)


print(Person.personCount)

print(Person.__name__)
print(Person.__module__)
print(Person.__dict__)
print(Person.__doc__)
print(Person.__bases__)



