from random import randint

DESCRIPTION = 'What is the result of the expression? '


def get_question_and_answer():
    a = randint(0, 50)
    b = randint(0, 50)
    mark = [' - ', ' + ', ' * ']
    var = randint(0, 2)
    correct_answer = calc(a, b, mark, var)
    question = str(a) + str(mark[var]) + str(b)
    return correct_answer, question


def calc(a, b, mark, var):
    if mark[var] == ' - ':
        return a - b
    if mark[var] == ' + ':
        return a + b
    if mark[var] == ' * ':
        return a * b
