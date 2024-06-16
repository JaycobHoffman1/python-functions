activities = []
duration = []

# Task 1: Develop a function to log different fitness activities and their duration.

def log_activities_and_duration():
    while True:
        input_activity = input('Enter an activity (type "done" when finished entering activities): ').lower()

        if input_activity == 'done':
            break
        else:
            activities.append(input_activity)
            
            input_duration = int(input('Enter how long you did this activity for (in minutes): '))
            duration.append(input_duration)


# Task 2: Write a simple function that estimates calories burned based on the activity and duration.

get_calories_burned = lambda d: int(d * 3.5) if d * 3.5 == int(d * 3.5) else d * 3.5


# Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.

def get_summary(lst1, lst2):
    total_calories_burned = []

    for i in range(len(lst1)):
        calories_burned = get_calories_burned(lst2[i])
        print(f'Activity: {lst1[i][0].upper()}{lst1[i][1:]}\nCalories Burned: {calories_burned}')
        total_calories_burned.append(calories_burned)

    print(f'Total calories burned: {int(sum(total_calories_burned)) if sum(total_calories_burned) == int(sum(total_calories_burned)) else sum(total_calories_burned)}')


# The code below allows each function to execute in the specified order.

print('Welcome to the fitness tracker! To start, let\'s make a list of the fitness activities you did today!')
log_activities_and_duration()

print('Today\'s fitness summary:')
get_summary(activities, duration)