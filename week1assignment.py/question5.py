#check if a number is even/odd, determine of a number is prime and find whethere a number is a multiple of another number
"""
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
if num1 % 2 == 0:
    print("The number is even.")
else:
    print("the number is odd")

if num1 % num2 == 0:
    print("the number is divisible")
else:
    print("the number is not divisible")

"""
user_number = int(input("Enter number"))

if user_number % 2 ==0:
    print(f"{user_number} is even")
else:
    print(f"{user_number} is odd")

#check prime number 
for i in range(2, user_number):
    if user_number % i == 0:
        print(f"{user_number} is not prime")
        break 
else:
    print(f"{user_number} is prime")

# check if the number is a square number 
for i in range(1, user_number):
    if i * i == user_number:
        print(f"{user_number} is a square number")
        break
else:
    print(f"{user_number} is not a square number")