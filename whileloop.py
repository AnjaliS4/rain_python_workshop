#game using while loop 
import random # imported a library
random_number = random.randint(1, 100)
#print(random_number)
while True:
    user_guess = int(input("Enter your guess"))
    if user_guess == random_number: 
        print ("You win")
        break
    elif user_guess < random_number:
        print("too low")
    else:
        print("too high")

        
