
while True:
    #check for palindrome
    user_input = input("Enter a word: ")
    if user_input == user_input[::-1]:
        print(f"{user_input} is a palindrome")
    else:
        print(f"{user_input} is not a palindrome")
        

