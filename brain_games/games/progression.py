from random import randint

DESCRIPTION = 'What number is missing in the progression? '


def get_question_and_answer():
    correct_answer, question = generate_progression()
    return correct_answer, str(question)


def generate_progression():
    progression = ''
    length = randint(10, 15)
    step = randint(3, 10)
    number = randint(5, 20)
    space = randint(5, length)
    for i in range(1, length + 1):
        if i == space:
            enigma = '..'
            progression = " ".join([progression, enigma])
            correct_answer = int(number)
            number += step
        else:
            progression = " ".join([progression, str(number)])
            number += step
    return correct_answer, progression
