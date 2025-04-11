# Class methods = Allow operations related to the class itself
#                Take (cls) as the first parameter, which represents the class itself

# Instance Methods = Best for operations on instances of the class (objects)
# Static Methods = Best for utility functions that do not need access to class data
# Class Methods = Best for class-level data or require access to the class itself
class Student:
    
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count +=1 #increment the count of students when a new student is created
        Student.total_gpa += gpa
    
    #INSTANCE METHOD
    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"
    
    
    @classmethod
    def get_count(cls): #in instance method we use the self constructor, otehrwise in class methods we use the cls constructor
        return f"Total numbers os students {cls.count}"
    
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{round(cls.total_gpa/cls.count, 2)}"
        
    
stu1 = Student("Spongebob", 3.5)
stu2 = Student("Patrick", 2.3)
stu3 = Student("Sandy", 9.7)


print(Student.get_count())

print(Student.get_average_gpa())
