"""
class Person: ## blueprint 
    def __init__(self, name, age): ## dunder method or magic : self call, __init__: runs when object create 
        self.name = name
        self. age = age

        ## def __init__(self):
        # pass 
        # pass 
    ruman = Person("Ruman", 27)

    print(ruman.name)
    print(ruman.age)

class PhoneFactory: 
     model: None 
     color: None
     is_android: None
     
     def __init__(self, model, color, is_android):
        self.model = model
        self.color = color
        self.is_android = is_android
        print("phone created")
     def __str__(self):

        return f"{self.model} - {self.color}"
     def check_os(self):
          if self.is_android:
            print("Android")
          else:
            print("ios")    

# apple_phone_ 1 = PhoneFactory ()
# apple_phone_1. model = "iPhone 12"
# apple_phone_1. color = "black"
# apple_phone_1. is_android = False
# print (apple_phone_1)
# samsung_phone_1 = PhoneFactory ()
# samsung_phone_1. model = "Galaxy S21"
# samsung _phone_1. color = I"black"
# samsung_phone_1. is android = True
# print (samsung_phone_1)

oppo phone_ 1 = PhoneFactory ("A53", "black", True)

## samsung_phone_1 = PhoneFactory()
## samsung_phone1.model = "Galaxy S21"

"""
## to do list using python class and object 
##craud operation 
class TodoList:
    def __init__(self, filename="todo_list.txt" ):
        self.filename = filename
        self.task = []

    def add_task(self, task): ##create
        self.task.append(task)
        print(f"Task'{task}' added to the list ")

    def remove_task(self, task): ## Delete
        if task in self.tasks: 
            self.tasks.remove(task)
            print(f"Task'{task}' removed from the list ")
        else:
            print(f"Task'{task}' not found in the list ")

    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print(f"Task updated to '{new_task}'")
        else:
            print(f"Task '{old_task} not found in the list.")
    def show_tasks(self): #get
        if self.tasks:
            print("Your to-do list:")
            for index, task in enumerate(self.tasks):
                print(f"{index +1}. {task}")
        else:
            print("Your todo list is empty.")
    
    def save_to_file(filename, data, mode="a"):
        with open(filename, mode) as file:
            file.write(data + "\n")



todo_list = TodoList()

todo_list.add_task("Buy groceries")
todo_list.add_task("Finish the report")
todo_list.add_task("call mom ")

todo_list.show_tasks()
todo_list.remove_task("Finish the report")
todo_list.update_task("Buy grocerie", "Go for a walk")
todo_list.show_tasks()
  


  ADD FILE TO THESE CODES 