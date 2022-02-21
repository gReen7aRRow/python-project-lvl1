#!/usr/bin/env python3

from random import randint

DESCRIPTION = 'What is the result of the expression? '


def get_question_and_answer():
    number1 = randint(0, 50)
    number2 = randint(0, 50)
    var = randint(0, 2)
    mark = [' - ', ' + ', ' * ']
    operation = [
        number1 - number2, number1 + number2,
        number1 * number2]
    correct_answer = int(operation[var])
    case = str(number1) + str(mark[var]) + str(number2)
    return correct_answer, case
