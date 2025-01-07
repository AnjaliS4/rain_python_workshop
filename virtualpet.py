import random
import threading
import time

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.super_happy_turns = 0

    def feed(self):
        self.hunger = min(100, self.hunger + 15)
        return f"You fed {self.name}. Hunger level increased to {self.hunger}!"

    def play(self):
        if self.energy < 20:
            return f"{self.name} is too tired to play! Try letting them rest."
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 10)
        return f"You played with {self.name}. Happiness is now {self.happiness}, but energy dropped to {self.energy}."

    def rest(self):
        self.energy = min(100, self.energy + 20)
        self.hunger = max(0, self.hunger - 10)
        return f"{self.name} rested. Energy is now {self.energy}, but hunger dropped to {self.hunger}."

    def random_event(self):
        event_type = random.choice(["toy", "snack", "nap"])
        if event_type == "toy":
            self.happiness = min(100, self.happiness + 10)
            return f"Random Event: {self.name} found a toy! Happiness increased to {self.happiness}."
        elif event_type == "snack":
            self.hunger = max(0, self.hunger - 10)
            return f"Random Event: {self.name} found a snack! Hunger decreased to {self.hunger}."
        elif event_type == "nap":
            self.energy = min(100, self.energy + 10)
            return f"Random Event: {self.name} took a quick nap! Energy increased to {self.energy}."

    def status(self):
        return f"\n{self.name}'s Stats - Hunger: {self.hunger}, Happiness: {self.happiness}, Energy: {self.energy}\n"

    def check_win_loss(self):
        if self.hunger <= 0 or self.happiness <= 0 or self.energy <= 0:
            return "sick"
        if self.hunger > 80 and self.happiness > 80 and self.energy > 80:
            self.super_happy_turns += 1
            if self.super_happy_turns == 3:
                return "win"
        else:
            self.super_happy_turns = 0
        return "continue"

def get_user_input(prompt, timeout):
    user_input = [None]  # Use a list to hold the input value since lists are mutable

    def input_thread():
        user_input[0] = input(prompt)

    thread = threading.Thread(target=input_thread)
    thread.daemon = True  # Ensure thread closes when main program ends
    thread.start()
    thread.join(timeout)  # Wait for the specified timeout

    if thread.is_alive():
        return None  # Timeout occurred
    return user_input[0]

# Main game loop
pet_name = input("Name your virtual pet: ")
pet = VirtualPet(pet_name)

print(f"\nWelcome to the Virtual Pet game! Meet {pet_name}.")

while True:
    print(pet.status())
    print("You have 10 seconds to choose an action!")

    action = get_user_input(f"What would you like to do with {pet_name}? (feed/play/rest/random/quit): ", 10)

    if action is None:  # Timeout case
        print("\nTime's up! You didn't act in time. Your pet decided to rest.")
        print(pet.rest())
    elif action == "feed":
        print(pet.feed())
    elif action == "play":
        print(pet.play())
    elif action == "rest":
        print(pet.rest())
    elif action == "random":
        print(pet.random_event())
    elif action == "quit":
        print(f"Thanks for playing with {pet_name}!")
        print(pet.status())
        break 
    else:
        print("Invalid input. Please choose  'feed', 'play', 'rest', 'random', or 'quit'.")

    # Check win/loss status
    status = pet.check_win_loss()
    if status == "sick":
        print(f"\nOh no! {pet_name} got sick. Game Over!")
        print(pet.status())
        break
    elif status == "win":
        print(f"\nCongratulations! {pet_name} is super happy and energetic! You win!")
        print(pet.status())
        break
