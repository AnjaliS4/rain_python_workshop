import os
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.consecutive_high_stats = 0

    def feed(self):
        self.hunger = min(self.hunger + 20, 100)
        print(f"{self.name} feels less hungry! Hunger is now {self.hunger}.")

    def play(self):
        if self.energy >= 10:
            self.happiness = min(self.happiness + 15, 100)
            self.energy -= 10
            print(f"{self.name} had fun playing! Happiness is now {self.happiness}, and energy is now {self.energy}.")
        else:
            print(f"{self.name} is too tired to play. Try letting them rest.")

    def rest(self):
        self.energy = min(self.energy + 20, 100)
        self.hunger = max(self.hunger - 5, 0)
        print(f"{self.name} feels rested! Energy is now {self.energy}, and hunger is now {self.hunger}.")

    def status(self):
        print(f"\n{self.name}'s Stats:\nHunger: {self.hunger}\nHappiness: {self.happiness}\nEnergy: {self.energy}\n")

    def check_game_status(self):
        if self.hunger <= 0 or self.happiness <= 0 or self.energy <= 0:
            print(f"{self.name} has gotten sick. Game over.")
            return False

        if self.hunger > 80 and self.happiness > 80 and self.energy > 80:
            self.consecutive_high_stats += 1
        else:
            self.consecutive_high_stats = 0

        if self.consecutive_high_stats >= 3:
            print(f"{self.name} has become super happy and energetic! You win!")
            return False

        return True

    def random_event(self):
        events = [
            ("finds a toy", "happiness", 10),
            ("finds a snack", "hunger", 10),
            ("takes a surprise nap", "energy", 10)
        ]
        event = random.choice(events)
        setattr(self, event[1], min(getattr(self, event[1]) + event[2], 100))
        print(f"{self.name} {event[0]}! {event[1].capitalize()} increases by {event[2]}.")

    def save_game(self):
        with open("pet_save.txt", "w") as file:
            file.write(f"{self.name},{self.hunger},{self.happiness},{self.energy},{self.consecutive_high_stats}")
        print("Game saved!")

    @staticmethod
    def load_game():
        if not os.path.exists("pet_save.txt"):
            print("No save file found.")
            return None

        with open("pet_save.txt", "r") as file:
            data = file.read().split(",")
            name = data[0]
            hunger, happiness, energy, consecutive_high_stats = map(int, data[1:])
            pet = VirtualPet(name)
            pet.hunger = hunger
            pet.happiness = happiness
            pet.energy = energy
            pet.consecutive_high_stats = consecutive_high_stats
            print("Game loaded!")
            return pet


def main():
    print("Welcome to the Virtual Pet Game!")
    choice = input("Do you want to load a saved game? (yes/no): ").strip().lower()

    if choice == "yes":
        pet = VirtualPet.load_game()
        if not pet:
            return
    else:
        name = input("What will you name your pet? ").strip()
        pet = VirtualPet(name)

    while True:
        pet.status()

        print("Choose an action:")
        print("1. Feed")
        print("2. Play")
        print("3. Rest")
        print("4. Save and Exit")

        try:
            action = int(input("Enter your choice (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if action == 1:
            pet.feed()
        elif action == 2:
            pet.play()
        elif action == 3:
            pet.rest()
        elif action == 4:
            pet.save_game()
            break
        else:
            print("Invalid choice. Try again.")
            continue

        if random.random() < 0.3:  # 30% chance of random event
            pet.random_event()

        if not pet.check_game_status():
            break


if __name__ == "__main__":
    main()


    LOOK AT THE TREASURE HUNT GAME AND TRY TO SOLVE IT 
    make CV and finish all pythod pending work today 