# 2. The Shopping List Maker

# Task 1: Write a function that lets the user add items to a list.
def add_item(shopping_list):
    item = input("Enter the item you want to add: ")
    shopping_list.append(item)
#end add_item


# Task 2: Task 2: Include a function to remove items from the list.
def remove_item(shopping_list):
    item = input("Enter the item you want to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print("Item not found.")
    #end if
#end remove_item


# Task 3: Add a function that prints out the entire list in a formatted way.
def print_list(shopping_list):
    print("Shopping List:")
    for item in shopping_list:
        print(f"- {item}")
    #end for
#end print_list

#================================================================

my_shopping_list = []
while True:
    action = input("What do you want to do? ([A]dd, [R]emove, [P]rint, [Q]uit): ").upper()
    if action == 'A':
        add_item(my_shopping_list)
    elif action == 'R':
        remove_item(my_shopping_list)
    elif action == 'P':
        print_list(my_shopping_list)
    elif action == 'Q':
        break
    else:
        print("Invalid action. Please try again.")
    #end if
#end while