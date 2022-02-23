from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers. '


def get_question_and_answer():
    a = randint(1, 50)
    x = b = randint(1, a)
    correct_answer, question = gcd(a, b, x)
    return correct_answer, question


def gcd(a, b, x):
    question = str(a) + ' ' + str(b)
    while b > 0:
        if a % x == b % x == 0:
            break
        else:
            x -= 1
    return x, question
