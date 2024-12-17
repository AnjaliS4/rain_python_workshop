#Unit converter 
# 1. Temperature converter
# 2. length converter
# 3. currency coverter
"""
temp_choice = input("Enter your choice: ")
celsius = float(input("Enter the temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}C = {fahrenheit}F")

length_choice = input("Enter your choice: ")
meter = float(input("Enter the length in meter: "))
feet = meter * 3.281
print(f"{meter}m = {feet}ft")

length_choice = input("Enter your choice: ")

currency_choice = input("Enter your choice: ")
nepali_rupee = float(input("Enter the amount in nepali rupee: "))
us_dollar = nepali_rupee * 0.0085
print(f"{nepali_rupee}NPR = {us_dollar}USD")

if temp_choice == "1":
    print(f"{celsius}C = {fahrenheit}F")
    length_choice == "2"
    print(f"{meter}m = {feet}ft")
elif currency_choice == "3":
    print(f"{nepali_rupee}NPR = {us_dollar}USD")

else:
    print ("invalid choice")
"""
from types import resolve_bases
user_choice = input("""
                     Enter your choice:
                     1. Temperature converter
                     2. length converter
                     3. currency converter 
                    the below code is not complete revise it once 
                     """)
if user_choice == "1": 
    user_input = float (input("Enter Miles"))
    result = user_input * 0.621371
    print(f"{user_input} KM = {result} Miles")
elif user_choice == "2":
    user_input = float(input("Enter Miles: "))
    result = user_input * 1.60934
    print(f"{user_input} Miles is equal to {result} KM")

elif user_choice == "3":
    user_input = float(input("Enter Centimeter: "))
    result = user_input * 0.393701
    print(f"{user_input} Centimeter is equal to {result} Inches")

elif user_choice == "4":
    user_input = float(input("Enter Inches: "))
    result = user_input * 2.54
    print(f"{user_input} Inches is equal to {result} Centimeter")
else: 
    print("Invalid input")
