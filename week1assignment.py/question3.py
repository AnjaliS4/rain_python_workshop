#create a program to calculate simple interest or compound interest 

user_choices = input("""
                     1. Simple Interest 
                     2. Compund Interest
                     """)
if user_choices == "1":
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period: "))
    simple_interest = (principal * rate * time) / 100
    print(f"The simple interest is {simple_interest}")
elif user_choices == "2":
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period: "))
    compound_interest = principal * (1 + rate / 100) ** time - principal
    print(f"The compound interest is {compound_interest}")
else:
    print("Invalid choice")