#!/usr/bin/env python3

import prompt


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("".join(['Hello, ', str(name), '! ']))
    print(game.DESCRIPTION)
    x = 0
    while x < 3:
        correct_answer, case = game.get_question_and_answer()
        print("".join(['Question: ', str(case)]))
        answer = input('Your answer: ')
        if str(answer) == str(correct_answer):
            print('Correct!')
            x += 1
        else:
            print(
                "".join([
                        '\'', str(answer), '\'', ' is wrong answer ;(. '
                        'Correct answer was ', '\'', str(correct_answer),
                        '\'. \nLet\'s try again, ', str(name) + '!']))
            break
        if x == 3:
            print("".join(['Congratulations, ', str(name), '!']))
            break
