# 3 astronuts have taken a certain amount of food to the moon, their batteru is finished and now they have to fill the battery
# first: find out how many batteries are needed for the charge to be 100/ count to be 100? 
# second: while u were filling the batter alien sent you a message 
# third alien captured u now u have to divide food between the 

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


    
    #check batteries over hundred 
def get_charged_batteries():
     batteries = [50, 30, 4, 45, 12, 18, 30] ## battery basket 
     minimum_battery_power = 20 ## battery use minimum 20 percent charge 
     usuable_battery_power = 0 
     usuable_battery_count = 0
     for battery in batteries: ### check every battery 
          if battery > minimum_battery_power: ## check if battery is over the charge 20 percent to use 
            usuable_battery_power += battery # if yes use power added 
            usuable_battery_count = usuable_battery_count +1 # if yes use battery count ass 
            if usuable_battery_power >= 100:
                return usuable_battery_power, usuable_battery_count
setup_mission()

print("WELCOME TO THE MARS!!!!!")
print("Your battery is dead please charge the battery")
battery_power, battery_count = get_charged_batteries() ### calling the function after it has been created 
print("Hurray!!!! Your battery is charged")

def decrypt_alien_message(alien_message):
    human_message = alien_message[::-1] ## reverse string 
    return human_message

print("Oops... ALien has arrived saying")
print("rednerrus")

decrypted_text = decrypt_alien_message("rednerrus")

print(f"Alien is saying: {decrypted_text}")
print("Alien has captured all astronauts")

print("if astronaut wants to escape they have divide each foos and give remaining foods")

def food_divide_equally(foods, crew_member):
    equally_foods = len(foods) // crew_member
    remaining_foods = len(foods) % crew_member
    return equally_foods, remaining_foods

    equally_divided, remaining_food = food_divide_equally(food, crew_number)
    print(f"You have{equally_divided} foods divided and remaing = {remaining_food}")
    print("Okay... Now you can go back to Earth")

    print("Mission Completed")




    

    
#Start the game/ call the function 
alien_attack_game()
