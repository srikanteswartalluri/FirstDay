#Class  {properties  + functions}
# ex: Person  {properties: age, name, height, weight
#              functions: walk(), talk(), run(), smell()
# }
# Object : It is an instance of a class
#          ex: Alex is an instance of the class Person()

class Person:
    'this is a person class'
    personCount = 0
    #constructor
    def __init__(self, age, name, gender):
        print("constructor is called")
        self.name = name
        self.age = age
        self.gender = gender
        Person.personCount = Person.personCount + 1

    #behaviour of a person (actions)
    def walk(self):
        print("I am walking")

    def talk(self, text):
        print("I am talking: {}".format(text))

    def run(self):
        print("I am running")

    def setAge(self, a):
        self.age = a

    def getAge(self):
        return self.age
