# Polymorphism = Greek work that means to "have many forms or faces"

#               TWO WAYS TO ACHIEVE POLYMORPHISM
#               1. Inheritance = An object could be treated of the same type as a parent class
#               2. "Duck typing" = Object must have necessary attributes/methods

# Below theres a example of inheritance as polymorphism.
# Circle can be a Circle and a Shape, Square can be a Square and a Shape and Triangle as well.
# They both has 2 faces or 2 forms

from abc import ABC, abstractclassmethod

class Shape:
    
    @abstractclassmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side 
    

class Triangle(Shape): 
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return (self.base * self.height) / 2

class Pizza(Circle):    #this pizza class can be considered as pizza, as circle and as a shape, 
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius) #if we did not used the super method, we'd a error in the for loop
        

shapes = [Circle(4), Square(5), Triangle(2,5), Pizza("Pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()} cm²")