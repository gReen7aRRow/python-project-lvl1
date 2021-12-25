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
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    x = 0
    while x < 3:
        number = randint(1, 50)
        if number == 1:
            correct_answer = 'yes'
        elif number == 2:
            correct_answer = 'yes'
        else:
            y = number - 1
            while y > 1:
                if number % y == 0:
                    correct_answer = 'no'
                    break
                else:
                    correct_answer = 'yes'
                    y -= 1
        print('Question: ' + str(number))
        answer = input('Your answer: ')
        sleep(1)
        if answer == correct_answer:
            print('Correct!')
            sleep(1)
            x += 1
        else:
            print(
                '\'' + str(answer) + '\'' + ' is wrong answer ;(. '
                'Correct answer was ' + '\'' + str(correct_answer) + '\'. '
                '\nLet\'s try again, ' + str(name) + '!')
            sleep(1)
            x = 0
    print('Congratulations, ' + str(name) + '!')


if __name__ == '__main__':
    main()
