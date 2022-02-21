#!/usr/bin/env python3

from random import randint

DESCRIPTION = 'What number is missing in the progression? '


def get_question_and_answer():
    case = ''
    length = randint(5, 10)
    step = randint(3, 10)
    number = randint(5, 20)
    space = randint(5, length)
    for i in range(1, length + 1):
        if i == space:
            enigma = '..'
            case = case + str(enigma) + ' '
            correct_answer = int(number)
            number += step
        else:
            case = case + str(number) + ' '
            number += step
    return correct_answer, case
