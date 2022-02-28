from random import randint

DESCRIPTION = 'What number is missing in the progression? '


def get_question_and_answer():
    long = randint(7, 12)
    step = randint(3, 10)
    element = randint(5, 20)
    enigma = randint(5, long - 1)
    progression = generate_progression(long, step, element)
    correct_answer = element + step * enigma
    question = progression.replace(str(correct_answer), '..')
    return correct_answer, question


def generate_progression(long, step, element):
    progression = element
    for i in range(1, long + 1):
        element += step
        progression = " ".join([str(progression), str(element)])
    return progression
