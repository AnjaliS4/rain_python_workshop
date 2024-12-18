# batteries game 

batteries = [50, 30, 4, 45, 12, 18, 30]

minimum_battery_power = 20
usable_battery_power = 0
usable_battery_count = 0

for battery in batteries:
    if battery > minimum_battery_power:
        usable_battery_power += battery 
        usable_battery_count += 1

print(usable_battery_power, usable_battery_count)


# Alien message translator using [::-1] to read the string backward 
alien_message = "neila na ma I .uoy era woh namuH iH"


print (f"""
Alien message = {alien_message}
Now, Human message = {alien_message [::-1]}
  """)


# 
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

available_crews = 3 
each_crew_food = len(available_foods) // available_crews

remaining_food_count = len(available_foods) % available_crews
print(f"Each crew get {each_crew_food} food and Remaining food count = {remaining_food_count}")