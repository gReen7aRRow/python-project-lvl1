#!/usr/bin/env python3

from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers. '


def get_question_and_answer():
    number1 = randint(1, 50)
    correct_answer = number2 = randint(1, number1)
    case = str(number1) + ' ' + str(number2)
    while correct_answer > 0:
        if number1 % correct_answer == number2 % correct_answer == 0:
            break
        else:
            correct_answer -= 1
    return correct_answer, case
