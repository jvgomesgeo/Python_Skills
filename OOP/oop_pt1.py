# object = A "bundle" of related attributes (variables) and methods (functions)
#           Ex. phone, cup, book
#           You neead a class to create many objects
#
# class = (blueprint) used to design the structure and layout of an object

# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         for_sale = for_sale

from class_pt1 import Car
#i can import the classes from a file

car1 = Car("Ferrari", 2015, "Black", False)
car2 = Car("Mustang", 2023, "Red", False)
car3 = Car("Charger", 2022, "Green", True)
# print(car1.model)
# print(car2.model)
# print(car3.model)

#car1.drive()
car1.describe()
