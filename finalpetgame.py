class VirtualPet:
    def __init__(self, name):
        self.name = name 
        self.happiness = 100
        self.energy = 100
        self.hunger_level = 100
    
    def feed(self):
        self.hunger_level += 10
        return f"{self.name}'s hunger level has increased!"
    
    def play(self):
        self.happiness += 20
        self.energy -= 10
        return f"{self.name} was really happy to play with you :)"
pet_name = input("Name your virtual pet: ")
pet = VirtualPet(pet_name)

print(f"Welcome to the Virtual Pet game! Meet {pet_name}")
print(f"{pet_name} is excited to see you. ")

while True: 
    action = input(f"what would you like to do with {pet_name}? (feed/play/quit)")
    if action == "feed":
        print(pet.feed())
    elif action == "play":
        print(pet.play())
    elif action == "quit":
        print(f"Thanks for playing with {pet_name}")
        break
    else:
        print("Invalid command. choose 'feed', 'play' or 'quit'")