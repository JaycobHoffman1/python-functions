# Task 1: Create functions for each arithmetic operation.

def add(num1, num2):
    if num1 + num2 == int(num1 + num2):
        return int(num1 + num2)
    else:
        return num1 + num2
    
def subtract(num1, num2):
    if num1 - num2 == int(num1 - num2):
        return int(num1 - num2)
    else:
        return num1 - num2
    
def multiply(num1, num2):
    if num1 * num2 == int(num1 * num2):
        return int(num1 * num2)
    else:
        return num1 * num2
    
def divide(num1, num2):
    if num2 == 0:
        return 'Error: Cannot divide by 0.'
    else:
        if num1 / num2 == int(num1 / num2):
            return int(num1 / num2)
        else:
            return num1 / num2


# Task 2: Implement user input to receive numbers and an operation choice.

to_num = lambda num: int(num) if  '.' not in num else float(num)

user_num1 = to_num(input('Enter a number: '))
operator = input('Enter an arithmetic operator (+, -, *, or /): ')
user_num2 = to_num(input('Enter another number: '))

if operator == '+':
    print(f'{user_num1} {operator} {user_num2} = {add(user_num1, user_num2)}')
elif operator == '-':
    print(f'{user_num1} {operator} {user_num2} = {subtract(user_num1, user_num2)}')
elif operator == '*':
    print(f'{user_num1} {operator} {user_num2} = {multiply(user_num1, user_num2)}')
elif operator == '/':
    print(f'{user_num1} {operator} {user_num2} = {divide(user_num1, user_num2)}')
else:
    print(f'"{operator}" is not a valid operator. Please try again.')


# Task 3: Ensure your program can handle division by zero and other potential errors.

print('Task 3: Ensure your program can handle division by zero and other potential errors. (see comment on line 55)')

'''
The "divide()" function includes an "if" statement checking to see whether the divisor (num2) is equal to 0. 
If it is, the function will return the message, "Error: Cannot divide by 0."
I demonstrate this by invoking the "divide()" function while passing the numbers "10" and "0" as parameters. 
The function returns the message. However, if I invoke the "divide()" function while passing the numbers "10" and "5" as parameters, 
the function divides the numbers normally.')
'''

print(divide(10, 0))
print(divide(10, 5))