#Deque  
# first question: Task manager with Deque 
from collections import deque
import random 

#Initialize deck of cards 
task_manager = deque(f"{value}" for value in
["Task: clean the room", "task 2 : Finish Uni assignment", "task3: finish reading The Alchemist"])
#tasks =  (["Task 1: clean the room", "Task 2: finish uni assignment", "Task3: Finish reading Alchemist"])
#for task in tasks:
    #task_manager.append(task)

task_manager.append("Go to the market")
task_manager.append("Finish revising for test")

print(f"task added {task_manager}")


print (task_manager)

print("Processing tasks:")

# rotate task 
task_manager.rotate(4)

print (task_manager)
 
# remove task

task_manager.popleft()
print(f"first task removed: {task_manager}")

if len(task_manager) == 0: 
    Print("There are no tasks to perform ")
else: 
    print("there are tasks that you need to get done!!!!")


