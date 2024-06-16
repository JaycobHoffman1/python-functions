import random as r

grades = [r.randint(50, 100) for i in range(10)]

# Task 1: Code a function to calculate the average grade.

get_average = lambda lst: sum(lst) // len(lst)


# Task 2: Implement a function to find the highest and lowest grade.

def get_highest_lowest(lst):
    return max(lst), min(lst)


# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).

def get_letter_grades(lst):
    for ele in lst:
        if ele >= 90:
            print(f'{ele}: A')
        elif 90 > ele >= 80:
            print(f'{ele}: B')
        elif 80 > ele >= 70:
            print(f'{ele}: C')
        elif 70 > ele >= 60:
            print(f'{ele}: D')
        else:
            print(f'{ele}: F')


# The code below allows each function to execute based on user input.

print('Welcome to the grade analyzer!')

print('Grades:')
for grade in grades:
    print(grade)

while True:
    user_input = input('What would you like to do? Get the [A]verage grade, get the [H]ighest and lowest grades, get the [L]etter grades, or [Q]uit the program?: ').upper()

    if user_input == 'A':
        print(f'The average grade is {get_average(grades)}.')
    elif user_input == 'H':
        print(f'The highest grade is {get_highest_lowest(grades)[0]}, and the lowest grade is {get_highest_lowest(grades)[1]}.')
    elif user_input == 'L':
        print('Here are the letter grades:')
        get_letter_grades(grades)
    elif user_input == 'Q':
        print('Quitting program. Thank you for using the grade analyzer!')
        break
    else:
        print(f'"{user_input}" is not a valid input. Please try again.')