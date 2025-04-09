# class varibles = Shared among all instances of a class
#                  Defined outside the constructor
#                  Allow you to share data among all objects created from thar class
        
        
class Student:
    class_year = 2024
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1 # if we want to change a class varible when a object is created, 
                                  # we use Class.classvarible inside de constructor


student1 = Student("Jhon", 22)
student2 = Student("Spongebob", 30)
student3 = Student("Squidward", 26)
student4 = Student("Sandy", 27)
students = [student1, student2, student3, student4]

# print(student1.name)
# print(student2.age)
print(student2.class_year) #class varibles can be accessed by any objetcs of the class

print(Student.class_year) # GOOD PRACTICE !! : if your want to get more agility e get more trusty, you use Class.classvarible, 
                          # once they are the in any object of the class
        
print(Student.num_students) #it'll return 4, because 4 objects was created in that class


print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print('-------------------------')
print("--- Students infos ---")
for student in students:
    print(f"Name: {student.name}; Age: {student.age}.")
    

