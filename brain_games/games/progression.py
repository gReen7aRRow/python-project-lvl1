from random import randint

DESCRIPTION = 'What number is missing in the progression? '


def get_question_and_answer():
    long = randint(7, 12)
    step = randint(3, 10)
    element = randint(5, 20)
    enigma = randint(5, long - 1)
    correct_answer, question = generate_progression(
        long, step, element, enigma)
    return correct_answer, question


def generate_progression(long, step, element, enigma):
    progression = ''
    for i in range(1, long + 1):
        if i == enigma:
            progression = " ".join([progression, '..'])
            correct_answer = element
            element += step
        else:
            progression = " ".join([progression, str(element)])
            element += step
    return correct_answer, progression
