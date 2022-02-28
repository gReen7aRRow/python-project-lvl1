from random import randint

DESCRIPTION = 'What number is missing in the progression? '


def get_question_and_answer():
    long = randint(7, 12)
    step = randint(3, 10)
    element = randint(5, 20)
    enigma = randint(5, long - 1)
    progression = generate_progression(long, step, element)
    for index, item in enumerate(progression):
        if index == enigma:
            correct_answer = progression[index]
            progression[index] = '..'
            question = str(progression)
    return correct_answer, question


def generate_progression(long, step, element):
    progression = []
    for i in range(1, long + 1):
        progression.append(element)
        element += step
    return progression
