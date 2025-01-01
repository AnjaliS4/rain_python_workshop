import time 
import json 
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
        if self.energy >=10:
            self.happiness = min(self.happiness + 15, 100 )
            self.energy -= 10 
            print(f"{self.name} is too tired to play. Try letting them rest.")

    def rest(self):
        self.energy = min(self.energy + 20, 100)
        self.hunger = max(self.hunger -5, 0)
        print(f"{self.name} feels rested! Energy is now {self.energy}, and hunger is now {self.hunger}")

    def status(self):
        print(f"\n{self.name}'s Stats:\nHunger: {self.hunger}\nhappiness: {self.happiness}\nEnergy: {self.energy}\n")

    def check_game_status(self):
        if self.hunger <= 0 or self.happiness <= 0 or self.energy <= 0:
            print(f"{self.name} has gotten sick. Game over.")
            return False 
        
        if self.hunger > 80 and self.happiness > 80 and self.ebergy > 80:
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
            ("takes a suprise nap", "energy", 10)
        ]
        event = random.choice(events)
        setattr(self, event[1], min(getattr(self,event[1])+ event[2], 100))
        print(f"{self.name} {event[0]}! {event[1]. capitalize()} increase by {event[2]}.")

def save_game(self):
    with open("pet_save.json", "w") as files:
        json.dump(self._dict_. file)
    print("game saved!")