import random 
import datetime 
import os
import time

INVENTORY_FILE = "inventory.txt"
LEADERBOARD_FILE = "leaderboard.txt"


def save_to_file(filename, data, mode="a"):
    """Save data to file."""
    with open(filename, mode) as file:  # the with keyword is going to close the file itself so we have to write the code to close 
        file.write(data + "\n")

def explore_location():
    """ Explore a random location and find treasures."""
    location = ["Mysterious cave", "Haunted forest", "Deserted Beach", "Ancient ruins"]
    treasure = ["Golden Crown", "Silver Sword", "Diamond Necklace", "Ancient Artifact"]

    location = random.choice(location)
    treasure = random.choice(treasure)

    print(f"\nExploring {location}...")
    time.sleep(2)
    print(f"You found a {treasure}!")

    save_to_file(INVENTORY_FILE, treasure)
    return treasure
    
def load_from_file(filename):
    """load data from a file"""
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [line.strip() for line in file]



def display_inventory():
    """Display the leaderboard."""
    leaderboard = load_from_file(LEADERBOARD_FILE)
    if leaderboard:
        print("\nLeaderboard:")
        for entry in leaderboard:
            print(entry)
    else:
        print("\nNo entries in the leaderboard yet")


def update_leaderboard(player_name, score):
    """Update the leaderboard"""
    save_to_file(LEADERBOARD_FILE, f"{player_name}: {score}")
   

def treasure_hunt():
    print("Welcome to treasure hunt")
    player_name = input("Enter your name: ").strip()

    #load inventory if it exists 
    score = 0 
    if os.path.exists(INVENTORY_FILE):
        print("\nResuming your adventure...")
    else:
        print("\nResuming a nre adventure...")
        open(INVENTORY_FILE, "w").close()  # create an empty inventory file 


        
        while True:
            print("\nWhat would you like to do?")
            print("1. Explore a new location")
            print("2. View inventory")
            print("3. Quit and save progress")
            choice = input("Enter your choice (1/2/3): ").strip()

            if choice == "1":
                treasure = explore_location()
                score += 1
                print(f"You added {treasure} to your inventory")
            elif choice == "2":
                print(f"\nThnaks for playing, {player_name}!")
                print(f"You collected {score} treasure.")
                update_leaderboard(player_name, score)
                break 
            else: 
                print("Invalid choice. Please try again")


def display_leaderboard():
    """Display the leaderboard."""
    leaderboard = load_from_file(LEADERBOARD_FILE)
    if leaderboard:
        print("\nLeaderboard:")
        for entry in leaderboard:
            print(entry)
    else:
        print("\nNo entries in the leaderboard yet.")

def view_leaderboard():
    print("\n== Leaderboard ==")
    display_leaderboard()

def main():
    while True:
        print("/n== Treasure HUnt Menu ==") 
        print("1. Start/Resume Game")
        print("2. View Leaderboard")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            treasure_hunt()
        elif choice == "2":
            view_leaderboard()
        elif choice == "3":
            print("Goodbye!")
            break 
        else: 
            print("Invalid choice. PLease try again")


if __name__ == "__main__":
    main()