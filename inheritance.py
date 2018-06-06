#Animal     name, make_sound, height, has_tail, no_of_legs, can_walk

#Dog inherits Animal and has some extra attributes and functions

#Snake inherits Animal
#Tiger
#Hippo

class Animal:
    'this is the base class for all animals'

    def __init__(self,name, no_of_legs, can_walk):
        self.name = name
        self.no_of_legs = no_of_legs
        self.can_walk = can_walk

    def make_sound(self):
        print("Animal: making sound")

    def show_love(self):
        print("Animal: showing love")


class Dog(Animal):
    def __init__(self):
        print("calling Dog's constructor")

    def make_sound(self):
        print("I am barking")

    def show_love(self):
        print("I am licking your feet")



