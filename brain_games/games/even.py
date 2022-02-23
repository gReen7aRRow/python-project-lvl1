from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no". '


def get_question_and_answer():
    question = number = randint(1, 20)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
