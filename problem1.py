# 1. The Calculator App

# Task 1: Create functions for each arithmetic operation.
def add(first, second):
    return first + second
#end add

def subtract(first, second):
    return first - second
#end subtract

def multiply(first, second):
    return first * second
#end multiply

def divide(first, second):
    while second == 0:
        print("Cannot divide by zero. Please try again.")
        second = int(input("Enter the second number: "))
    #end while
    return first / second
#end divide


# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Must enter a number. Please try again.")
        #end try
    #end while
#end get_valid_number

while True:
    operation = input("What operation do you want to perform? ([A]dd, [S]ubtract, [M]ultiply, [D]ivide): ").upper()
    if operation not in ['A', 'S', 'M', 'D']:
        print("Invalid operation. Please try again.")
    else:
        break
    #end if
#end while


first_number = get_valid_number("Enter the first number: ")
second_number = get_valid_number("Enter the second number: ")
result = None

if operation == 'A':
    result = add(first_number, second_number)
elif operation == 'S':
    result = subtract(first_number, second_number)
elif operation == 'M':
    result = multiply(first_number, second_number)
elif operation == 'D':
    result = divide(first_number, second_number)
#end if

print(f"The result is: {result}.")