# 3 astronuts have taken a certain amount of food to the moon, their batteru is finished and now they have to fill the battery
# first: find out how many batteries are needed for the charge to be 100/ count to be 100? 
# second: while u were filling the batter alien sent you a message 
# third alien captured u now u have to divide food between the 


def change_batter():
    print("you need to have the battery at 100")
    available_batteries = [50, 30, 4, 45, 12, 18, 30]
    
def setup_mission():
    print("Setting up for the mission ")
    available_foods = [ 
    "apple",
    "bananna",
    "watermelon",
    "grapes",
    "pineapple",
    "cherry",
    "berries",
    "cupcake",
    "pestries",
    "pizza",
    "burger",
    ]
    available_crews = int(input("Enter available crews"))
    return available_crews, available_foods
    print("Setup completed....")

def alien_attack_game():
    print("Welcome to the Alien Attack game")
    print("Starting mission...")

    # step 1: Setup the mission 
    crews_number, foods = setup_mission()
    print(f"You have {crews_number} astronuts and food available = {foods}")
    

    setup_mission()

    print("WELCOME TO THE MARS!!!!!")
    print("Your battery is dead please charge the battery")
    print("Mission Completed")

    
#Start the game/ call the function 
alien_attack_game()
