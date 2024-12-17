#input a number, double it, add 10, halve it, subract original, output = 5
# using use_choice--> can only choose the number by the programmer  / using input 
"""
first_number = 
if user_choice == "+":
    print("Addition =", first_number + 10)
elif user_choice == "*":
    print("Multiplication =", first_number * 2 )
elif user_choice == "/":
    print("Division =", first_number / 2)
elif user_choice== "-": 
     print("Subtraction =", second_number- first_number)
else:
    print("Invalid choice")
   
user_number = int(input("Enter your first number: "))
double_number = first_number * 2
print(f"Your double number is {double_number}")
add_number = double_number + 10

addition_number =
hal
subract_number = 
 """
while True: 
    first_number = int(input("Enter your first number: ")) # User input number in integer
    double_number = first_number * 2 # double
    print(f"Your double number is {double_number}") #print result
    addition_number = double_number + 10 # add 10 or we can also write double_bumber += 10 which means double_number = double_number + 10
    print(F"Add 10 = {addition_number}")

    half_number = addition_number / 2 #divide 2
    print(f"Half number = {half_number}") #print result

    subtraction_number = half_number - first_number
    print(f"Subtraction number = {subtraction_number}") #print result

    user_choice = input ("""
                        Do you want to contibe? Yes or NO 
                        """)
    if user_choice.lower() == "no":
        break 