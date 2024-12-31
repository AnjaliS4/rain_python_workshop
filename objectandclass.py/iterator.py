# Example 1: Iterator
"""
class MyIterator:
    def __init__(self, data):
        self.data = data 
        self.index = 0

    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        print(f"Getting index : {self.index}")
        value = self.data[self.index]
        self.index += 1
        return value 
    
    
# Example 2:using iterator 
my_list = [1, 2, 3, 4, 5] # objects so should be outside class 
my_iter = MyIterator(my_list)

for num in my_iter:
    print(num) # Output: 1 2 3 4 5




## ABSTRACTION ###

from abc import ABC, abstractmethod                                 
class Vechicle(ABC):
    #@abstractmethod
    def drive(self):
        print("Vehicle is driving")
        #pass
    def new_fn(self):
        print("My new fn")


class car(Vechicle):
    pass
    # def drive(self):
    # return "car is driving"

# using abstraction 
car = car()
print(car.drive()) #Output: car is driving 

#veh = Vechicle()
#print(veh.drive()) #Access abstract method 
"""


#### Encapsulation ##### 

class BankAccount: 
    def __init__(self, name):
        self._balance = 0 
        self.name = name 

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance
    
    def __str__(self):
        return f"Name: {self.name} and Balance: Hidden"
    
### using encapsulation 
ruman = BankAccount("Ruman")
ruman.deposit(100)
print(ruman)
print(ruman.get_balance()) #Output
ruman.withdraw(50) #Output: 50
ruman.deposit(400) #output: 450
ruman.withdraw(100) #output:350
print(ruman.get_balance())