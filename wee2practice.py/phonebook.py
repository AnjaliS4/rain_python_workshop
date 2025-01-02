#1 make phonebook()__. run this in loop and ask to exist 
        # name, phonenumber--> parameters 
#2 enter name: Anjlai __. this gives your phone number is ..... 
# the steps required: make dictonary for storing the value 
"""
Phonebook = {
  "Anjali": "12345", # should not have give first but asked the user to enter 
  "Avipsha": "6789",
  "Sabikshya": "1011"
}
print(Phonebook)

def Phonebook():
    print("Whose number do you want")
    

Phonebook()
"""
## the final code 
def store_contact(name, number, contacts={}):
    contacts[name.lower()] = number
    return contacts

def phone_book():
    contacts ={}
    while True: 
        name = input("Enter name") # use of dictionary in this loop 
        number = input ("Enter number")
        contacts = store_contact(name, number, contacts)
        user_choice = input("""
        Do you want to exist?
        1. Yes 
        2. No 
        """)
        if user_choice == "1":
            return contacts

my_contacts_book = phone_book()

def get_phone_number(name, contacts):
    return contacts.get(name.lower())

user_name = input ("Enter name to find phone number")
print(get_phone_number(user_name, my_contacts_book))












