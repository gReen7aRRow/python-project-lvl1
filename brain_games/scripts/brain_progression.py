#!/usr/bin/env python3

from random import randint
from time import sleep


def main():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
        sleep(1)
    print('Hello, ' + str(name) + '!')
    sleep(1)
    print('What number is missing in the progression?')
    x = 0
    while x < 3:
        progression = []
        length = randint(5, 10)
        step = randint(7, 15)
        number = randint(5, 20)
        space = randint(3, length)
        for i in range(1, length + 1):
            if i == space:
                enigma = '..'
                progression.append(enigma)
                correct_answer = int(number)
                number += step
            else:
                progression.append(number)
                number += step
        print('Question: ' + str(progression))
        answer = int(input('Your answer: '))
        sleep(1)
        if answer == correct_answer:
            print('Correct!')
            x += 1
            sleep(1)
        else:
            print(
                '\'' + str(answer) + '\'' + ' is wrong answer ;(. '
                'Correct answer was ' + '\'' + str(correct_answer) + '\'. '
                '\nLet\'s try again, ' + str(name) + '!')
            x = 0
    print('Congratulations, ' + str(name) + '!')


if __name__ == '__main__':
    main()
