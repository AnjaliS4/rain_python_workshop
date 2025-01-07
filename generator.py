
def natural_numbers():
    n = 1
    while True:
        yield n 
        n += 1 

gen = natural_numbers()
for _ in range(10): # print the first 10 natural numbers 
    print(next(gen))
   
    


    ##### comprehension #######
    
treasures = ["Gold", "Silver", "Gem", "Gold"]
upper_treasure = []
for treasure in treasures:
    upper_treasure.append(treasure.upper())

# by using comprehension 
capitalized_treasures = [treasure.upper() for treasure in treasures]
print(capitalized_treasures)
 

##### recursion ###

def factorial(n):
    if n==0:
        return 1 # base case 
    return n * factorial(n-1)
print(factorial(5)) # output:120 