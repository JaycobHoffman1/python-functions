shopping_list = []

# Task 1: Write a function that lets the user add items to a list.

def add_to_list(lst):
    print('Add items:')

    while True:
        item = input('Enter an item (type "done" when finished adding items): ')

        if item.lower() == 'done':
            break
        else:
            lst.append(item)

            if lst.count(item) > 1:
                print('Looks like you\'ve already added that item!')
                lst.remove(item)
            else:
                print('Item added!')


# Task 2: Include a feature to remove items from the list.

def remove_from_list(lst):
        if len(lst) == 0:
            print('The list is empty! Nothing to remove!')
        else:
            print('Remove Items:')

            while True:
                item = input('Enter an item you wish to remove (type "done" when finished removing items): ')

                if item.lower() == 'done':
                    break
                elif item not in shopping_list:
                    print('That item isn\'t in your list!')
                else:
                    lst.remove(item)
                    print('Item removed!')


# Task 3: Add a function that prints out the entire list in a formatted way.

def print_list(lst):
    if len(lst) == 0:
        print('Nothing to print! Add items to the list to print it.')
    else:
        print('Print shopping list:')

        name = input('Enter your name: ')
        print(f'{name}\'s Shopping List: ')

        for item in lst:
            print(item)


# The code below allows each function to execute based on user input.

print('Hello! Welcome to the shopping list creator!')

while True:
    user_input = input('What would you like to do? [A]dd items to your list, [R]emove items from your list, [P]rint your shopping list, or [Q]uit the program?: ').upper()

    if user_input == 'A':
        add_to_list(shopping_list)
    elif user_input == 'R':
        remove_from_list(shopping_list)
    elif user_input == 'P':
        print_list(shopping_list)
    elif user_input == 'Q':
        print('Quitting program. Thank you for using the shopping list creator!')
        break
    else:
        print(f'"{user_input}" is not a valid input. Please try again.')