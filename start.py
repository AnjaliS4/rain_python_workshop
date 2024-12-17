print("Hello World")

if 5 > 2: 
    print("5 is greater than 2")
    print("2 is smaller than 5")

x = 5
y = "hello world"
print(x)
print(y)
print(id(x))
print(id(y))
print (type(x)) #checking the type of the variable 
print (type(y))
# my notes for this python class 
comment ="""
this is a mail 
hello i am writing comments 
on multiple lines for my code 
- a multiple line string 
"""
print(comment)
d= 7.5 
print (type(d))
e = int(d)
print(e)
a = 3
b = "2" 
if a > int(b):
    print("a is greater")
myObject = 5 #camel case 
MyObject = 5 #pascal case 
myobject = 5 #snake case 
x,y,z = "Orange", "Banana", "Mango"
print(x)
print(y)
print(z)
a = True 
b = False 
print(a and b)
print(a or b)
print(not b)

boy_age = 19
boy_country ="Nepal"

if boy_age > 18 and boy_country == "Nepal":
    print("Boy can give licence exam in nepal")
first_number = int(input("Enter your first number: "))
second_number= int(input("Enter your second number: "))

print("Addition =", first_number + second_number)
print ("Subtraction=", first_number - second_number)
print ("multiplication=", first_number * second_number)
print ("division=", first_number / second_number)
print ("modulus=", first_number % second_number)
print ("exponential=", first_number ** second_number)
print ("floor division=", first_number// second_number)
"""
first_number = int(input("Enter your first number: "))
second_number= int(input("Enter your second number: "))

print("Addition =", first_number + second_number)
print ("Subtraction=", first_number - second_number)
print ("multiplication=", first_number * second_number)
print ("division=", first_number / second_number)
print ("modulus=", first_number % second_number)
print ("exponential=", first_number ** second_number)
print ("floor division=", first_number// second_number)



first_number = float(input("Enter your first number: "))
second_number= float(input("Enter your second number: "))

user_choice = input("""
                    Enter your choice:
                    1. + for Addition
                    2. - for Subtraction
                    """)
if user_choice == "+":
    print("Addition =", first_number + second_number)
elif user_choice == "-":
    print("Subtraction =", first_number - second_number)
else:
    print("Invalid choice")

"""

"""
first_number = int(input("Enter your first number: "))
second_number= int(input("Enter your second number: "))
user_choice = input(""" 
                   #Enter your choice:
                   #1.* to double the number 
                   #2. + for Add to the number
                   #3. / to halve the number 
                   #4. - to subract the original 
                
