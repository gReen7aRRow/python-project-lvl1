#!/usr/bin/env python3

from random import randint
import prompt


def game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(
        'Hello, ' + str(name) + '! '
        '\nAnswer "yes" if the number is even, otherwise answer "no".')
    for x in range(0, 3):
        number = randint(1, 20)
        print('Question: ' + str(number))
        answer = input('Your answer: ')
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                x += 1
            else:
                print(
                    '"no" is wrong answer ;(. Correct answer was "yes" '
                    '\nLet\'s try again, ' + str(name) + '!')
                break
        else:
            if answer == 'no':
                print('Correct!')
                x += 1
            else:
                print(
                    '"yes" is wrong answer ;(. Correct answer was "no" '
                    '\nLet\'s try again, ' + str(name) + '!')
                break
        if x == 3:
            print('Congratulations, ' + str(name) + '!')
            break
