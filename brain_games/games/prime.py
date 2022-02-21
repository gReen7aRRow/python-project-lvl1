#!/usr/bin/env python3

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no". '


def get_question_and_answer():
    case = randint(3, 50)
    y = case - 1
    correct_answer = 'yes'
    while y > 1:
        if case % y == 0:
            correct_answer = 'no'
            break
        else:
            y -= 1
    return correct_answer, case
