# Task 1: Develop a list of questions and answers.

questions = ['What is 10 + 10? ', 'What is 8 - 3? ', 'What is 5 x 5? ', 'What is 20 ÷ 2? ', 'What is 100 * 0? ', 'What is 30 * 1? ']
answers = [20, 5, 25, 10, 0, 30]


# Task 2: Write a function that quizzes the user and takes their answers.

score_list = []

def quiz(lst1, lst2):
    for i in range(len(lst1)):
        answer = int(input(questions[i]))
        score_list.append(answer == lst2[i])


# Task 3: Score the quiz and give the user feedback on their performance.

def score_quiz(lst):
    score = lst.count(True) / len(lst) * 100
    print(f'Your score is {int(score) if score == int(score) else round(score, 2)}%.', end = ' ')

    if score >= 90:
        print('Excellent job!')
    elif 90 > score >= 80:
        print('Good job!')
    elif 80 > score >= 70:
        print('Fair!')
    elif 70 > score >= 60:
        print('You passed, but try better next time.')
    else:
        print('Oops! Better luck next time.')

    lst.clear()


# The code below allows each function to execute based on user input.

def play_game():
    quiz(questions, answers)
    score_quiz(score_list)

print('Welcome to the quiz game! Let\'s begin!')
play_game()

while True:
    try_again = input('Would you like to try again? Type \'Y\' for yes or \'N\' for no: ').upper()

    if try_again == 'N':
        print('Okay! Thanks for playing!')
        break
    elif try_again != 'Y' and try_again.upper() != 'N':
        print(f'"{try_again}" is not a valid input.')
    else:
        play_game() 