# object = A "bundle" of related attributes (variables) and methods (functions)
#           Ex. phone, cup, book
#           You neead a class to create many objects
#
# class = (blueprint) used to design the structure and layout of an object


class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    #Defining a method (function):
    def drive(self):
        print(f"You drive the car {self.color} {self.model}")

    def stop(self):
        print(f"You stop the car {self.color} {self.model}")

    def describe(self):
        print(f"The model of the car: {self.model}")
        print(f"The color of the car: {self.color}")
        print(f"The year of the car is {self.year}")
        print(f"The car is for sale? {self.for_sale}")