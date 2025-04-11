# Static methods = A method that belongs to a class rather than any object from that class
#                   Usually used for general utility functions

# Instance methods  = Best operation on instances of the class (objects)
#Static methods   = Best for utility functions that do not need access to class data



class Employee:
    def __init__(self, name, job_position):
        self.name = name
        self.job_position = job_position
    
   
    def get_info(self):
        return f"{self.name} = {self.job_position}"

    def get_job_position(self):
        return self.job_position
    
    @staticmethod
    def is_valid_position(position): #a function that checks if the position is valid or not
        #this method is static because it does not need to access any instance or class data.
        valid_positions = ["Manager", "Developer", "Enginer", "Designer"]
        return position in valid_positions


employee1 = Employee("Jose", "Manager")
employee2 = Employee("Maria", "Developer")
employee3 = Employee("Pedro", "Cook")


#calling static methods, used in class objects
print(Employee.is_valid_position("Manager")) #True 
print(Employee.is_valid_position("Cook")) #False


#calling instance methods, used in instance objects

print(employee1.get_info()) #Jose = Manager
print(employee1.is_valid_position(employee1.get_job_position())) #True
print(employee3.get_info()) #Pedro = Cook
print(employee3.is_valid_position(employee3.get_job_position())) #False

