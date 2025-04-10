# multiple inheritance = inherit from more than one parent class 
#                       C(A,B) - this class will be able to access the attirubutes and methods of A,B classes.

# mutilevel inheritance = inherit from a parent which inherits from another parent C(B) <- B(A) <- A

# GrandParent
class Animal():
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating...")
    
    def sleep(self):
        print(f"{self.name} is sleeping...")    
    
# Parents
class Prey(Animal): #presa
    def flee(self):
        print(f"{self.name} is fleeing")
        
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


#Childrens
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): # we can consider Fish as Prey or Predator
    pass


rabbit = Rabbit("Bugs") # When you create a object, you need to pass the attributes setted in the inheritance class
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.eat()