# Duck Typing = Another way to achiebe polymorphism besides inheritance
#               Object must have the minimum necessary attributes/methods
#               "If ir loop like a duck and quacks like a duck, it must be a duck"


class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("WOOF!")
             
class Cat(Animal):
    def speak(self):
        print("MEOW!")
        
# the class below has no info related to the animal class, but if we create a method with name like the other classes, 
# it'll perform like other classes. The same occurs to the class varible
class Car:
    alive = False
    def speak(self): 
        print("HONK!")

#so, our car has the minimum necessary to be a animal, so for python, our car is a animal
        
animals = [Dog(), Cat(), Car()]



for animal in animals:
    animal.speak()
    print(animal.alive)