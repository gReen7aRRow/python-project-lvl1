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
    print('Answer "yes" if the number is even, otherwise answer "no".')
    x = 0
    while x < 3:
        number = int(input('Write your number: '))
        print('Question: ' + str(number))
        answer = input('Your answer: ')
        sleep(1)
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                sleep(1)
                x += 1
            else:
                print(
                    '"' + answer + '" is wrong answer ;(. Correct answer was "yes". '
                    '\nLet\'s try again, ' + str(name))
                sleep(1)
                x = 0
        else:
            if answer == 'no':
                print('Correct!')
                sleep(1)
                x += 1
            else:
                print(
                    '"' + answer + '" is wrong answer ;(. Correct answer was "no". '
                    '\nLet\'s try again, ' + str(name))
                sleep(1)
                x = 0
    print('Congratulations,' + str(name) + '!')


if __name__ == '__main__':
    main()
