# calculate the area and peremeter of shapes 
"""
length = float(input("enter the length:"))
breadth= float(input("enter the breadth:"))
areaofrectangle = length * breadth
perimeterofrectangle = 2 * (length + breadth)
print("area of rectangle is", areaofrectangle)
print("perimeter of rectangle is", perimeterofrectangle)
"""
# by using user_choice
while True: 
    user_choice = input("""
                        Enter your choice:
                        1. Area of rectangle
                        2. Area of triangle
                        3.Area of circle 
                        4. Perimeter of rectangle
                        5. Perimeter of triangle
                        6. Perimeter of circle
                        """)
    if user_choice == "1":
        length = float(input("Enter the length: "))
        breadth = float(input("Enter the breadth: "))
        areaofrectangle = length * breadth
        print(f"The area of rectangle is {areaofrectangle}")
    elif user_choice == "2":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        areaoftriangle = 0.5 * base * height
        print(f"The area of triangle is {areaoftriangle}")
    elif user_choice == "3":
        radius = float(input("Enter the radius: "))          
        areaofcircle = 3.14 * radius * radius
        print(f"The area of circle is {areaofcircle}")
    elif user_choice == "4":
        length = float(input("Enter the length: "))
        breadth = float(input("Enter the breadth:"))
        perimeterofrectangle = float(2(length + breadth))
        print(f"the perimeter of rectangle is {perimeterofrectangle}")
    else:
        print("Invalid choice")
    user_choice = input ("""
                        Do you want to contibe? yes or no
                        """)
    if user_choice.lower().strip() == "no":
        print("Thankyou for using this calculator for your geometry calculations hope we were helpful")
        break 

