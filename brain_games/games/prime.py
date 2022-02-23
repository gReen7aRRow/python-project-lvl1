from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no". '


def get_question_and_answer():
    question = number = randint(3, 50)
    if is_prime(number) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question


def is_prime(number):
    y = number - 1
    while y > 1:
        if number % y == 0:
            return False
        else:
            y -= 1
    return True
