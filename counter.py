"""
from collections import Counter

text = #you are supposed to have a comment comma here 
python is an amazing programming language, python is fun to learn and powerful to use 

words = text.lower(). split()
word_count = Counter(words)

print("Word Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")
print (len (text))

from queue import Queue

# create a task queue
task_queue = Queue()

# add tasks to the queue 
tasks = ["Task 1: Clean the room", "Task2: Write Python code", "Task 3: Read a book"]
for task in tasks:
    task_queue.put(task)

# process tasks 
print("Processing tasks:")
while not task_queue.empty():
    print(task_queue.get())
"""
    

from collections import deque
import random 

#Initialize deck of cards 
deck = deque ([f"{value} of {suit}" for value in
              ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "king", "Ace"]
              for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]])

#shuffle the deck
random.shuffle(deck)

#PLayers and their hands
player1 = []
player2 = []

# Draw 3 cards for each player
for _ in range(3):
    player1.append(deck.popleft())
    player2.append(deck.popleft())

# display players' hands
print("Player 1's hand:")
print(player1)
print("\nPLayer 2's hand:")
print(player2)