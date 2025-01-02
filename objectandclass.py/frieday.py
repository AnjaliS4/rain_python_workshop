
# The __innit__() Function --> is the constructor for using class and object
# magical __> if the function doesnt need to be called 
class person: 
    def __init__(self, name, age): 
        self.name = name
        self.age = age

p1 = person("Anjali", 18)
print(p1.name)
print(p1.age)

#to create a child class 
class Student(Person):
    pass 
x = Student("Aachal", 19)
x.printname()