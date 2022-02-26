from random import randint

DESCRIPTION = 'What is the result of the expression? '


def get_question_and_answer():
    a = randint(0, 50)
    b = randint(0, 50)
    mark = [' - ', ' + ', ' * ']
    correct_answer, question = calc(a, b, mark)
    return correct_answer, question


def calc(a, b, mark):
    var = randint(0, 2)
    operation = [
        a - b, a + b,
        a * b]
    correct_answer = randint(0, 50)
    question = str(a) + str(mark[var]) + str(b)
    return correct_answer, question
