# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}") 


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled) # I can specify which attributes i'll call from the parent class
        self.radius = radius
        
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius} cm²") # METHOD OVERWRITTING: 
                                                                        # create the same method that exists in parent class inside children class
                                                                        # in this case, the method that will run is the children class method
                                                                        #if this children method hadn't been created, the output would be the parent method
        super().describe() #now we're joining the two methods and extending functionality
        
        
class Square(Shape):
    def __init__(self, color,is_filled, width):
        super().__init__(color, is_filled) 
        self.width = width
    

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width} cm²") 
        super().describe() #now we're joining the two methods and extending functionality

        
        

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    
    def area(self):
        area = (self.width * self.height) / 2
        print(f"The area is {area} m²")
                
    def describe(self):
        super().describe() #now we're joining the two methods and extending functionality   
        print(f"It is a triangle with an area of {self.area()} cm²") 
        
            
        
circle1 = Circle(color = "Red", is_filled= True, radius= 3.5)
square1 = Square(color = "Red", is_filled= True, width= 2)
triangle1 = Triangle(color= "Blue", is_filled= False, width= 5, height=2)

print(circle1.describe())  # will return the children method created in circle class (children class)
print(square1.describe())  
print(triangle1.describe())
