from collections import OrderedDict

# create an empty dictonary 
#loop forever
#try 
    #get user input 
    #check if items are already added in the dict 


# number of items 

# Create an ordered dictionary for the grocery list
grocery_list = OrderedDict()

# Function to add items to the list
def add_item(category, item, quantity=1):
    if category not in grocery_list:
        grocery_list[category] = OrderedDict()
    if item in grocery_list[category]:
        grocery_list[category][item] += quantity
    else:
        grocery_list[category][item] = quantity

# Function to remove an item from the list
def remove_item(category, item):
    if category in grocery_list and item in grocery_list[category]:
        del grocery_list[category][item]
        # Remove category if empty
        if not grocery_list[category]:
            del grocery_list[category]

# Function to display the grocery list
def display_list():
    print("\nGrocery List:")
    for category, items in grocery_list.items():
        print(f"{category}:")
        for item, quantity in items.items():
            print(f"  {item}: {quantity}")

# Example usage
add_item("Fruits", "Apples", 5)
add_item("Fruits", "Bananas", 3)
add_item("Vegetables", "Carrots", 4)
add_item("Dairy", "Milk", 2)
add_item("Fruits", "Apples", 2)  # Add more apples

remove_item("Vegetables", "Carrots")

display_list()
 