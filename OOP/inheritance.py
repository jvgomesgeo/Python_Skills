# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               Class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.isalive = True
        
    def eat(self):
        print(f"{self.name} is eating...")
                
    def sleep(self):
        print(f"{self.name} is sleeping")
        

class Dog(Animal): #the dog class will receive all atributtes and methods setted in Animal Class
    def speak(self): # We set new methods or atributtes in the children classes and they will have the parents and children methods e attributes
        print("WOOF!")
    


class Cat(Animal):

    def speak(self):
        print("MIAU !")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Luna")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.eat())

