"""
def greet(first_name, last_name):
    print(f"Namaste {first_name} {last_name}")
    print(f"How are you {first_name} ")

greet("Anjali", "Simkhada")

# 1- perform a task 
#2- return a value 

def get_greeting(name):
    return f"Hi {name}"

def increment(number, by):
    return number + by
    

print(increment(number=2, by=1))



class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@compay.com'

    def fullname(self):
        return f"{self.first}, {self.last}"
        


emp_1 = Employee("Ram", "Rai", 50000)
emp_2 = Employee("tom", "lama", 60000)



# print(emp_1)
# print(emp_2)
print(emp_1.fullname())


emp_1.first = 'Ram'
emp_1.last = 'Rai'
emp_1.email = 'ram.rai@company.com'
emp_1.pay = 50000

emp_2.first = 'tom'
emp_2.last = 'lama'
emp_2.email = 'tom.lama@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

""" 
name = input("enter your name ")
age = int(input("enter your age"))
print("Hello," + name, + age)
print(f"hi my name is {name}, and i am {age} years old")