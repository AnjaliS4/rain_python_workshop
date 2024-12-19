def sum(*args):
    result = 0 
    for number in args:
        result += number
    return result 

def diff(a,b): 
    return a-b 

def mul(*args):
    result1 = 1
    for numbers in args:
        result1 = result1 * numbers 
    return result1

def div(a,b):
    return a/b

def exponential():
    pass 
def print_name(name="Ruman"):
    print(f"Hello {name}")

print(sum(1,2,3,4,5))
print(mul(1,2,3,4,5))
print_name()
print_name("Anjali")

def print_full_name(**kwargs):
    print(kwargs) # this is the same as print_full_name that is why it is printed before "my name is .."
    print(f"My full name is {kwargs['first_name']} {kwargs['last_name']}")

print_full_name(first_name="Anjali", last_name="Simkhada", middle_name="none")

def print_result(*args, **kwargs):
    print(args)
    print(kwargs)
    result = 0
    for number in args:
        result += number
    print(f"My full name is {kwargs['first_name']} {kwargs['last_name']} and total marks ={result}")

print_result(10,20,30,40,50, first_name="Anjali", last_name="Simkhada")