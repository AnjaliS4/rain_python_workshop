for x in "banana":
    print(x)

a = "hello world !"
print("length ===", len(a))

txt ="The best things in life are free!"
print("free" in txt)

b = "Hello,      World!"
print(b[2:5])
print(b[:5])
print(b. strip())
print(b.replace("H","J"))
z =b.split(",")
print(z)
name = input ("Enter your name: ")
print("You have enterted your name: " + name) # string concatenation
print("You have enterted your name: {name}") # format string
print("You have enterted your name = %s" % (name)) # Modulus string 
user_choice = input("""
                    Enter your choice: 
                    1. + for Addition
                    2. - for Subtraction 
                    """")
if user_choice == "+":
