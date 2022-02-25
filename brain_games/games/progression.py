from random import randint

DESCRIPTION = 'What number is missing in the progression? '


def get_question_and_answer():
    long = randint(7, 12)
    step = randint(3, 10)
    first_number = randint(5, 20)
    correct_answer, progression = generate_progression(
        long, step, first_number)
    question = str(progression)
    return correct_answer, question


def generate_progression(long, step, first_number):
    progression = []
    for i in range(1, long + 1):
        progression.append(first_number)
        first_number += step
    enigma = randint(5, long - 1)
    correct_answer = progression[enigma]
    progression[enigma] = '..'
    return correct_answer, progression
