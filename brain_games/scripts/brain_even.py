#!/usr/bin/env python3

from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, ' + str(name) + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    x = 0
    while x < 3:
        number = randint(1, 20)
        print('Question: ' + str(number))
        answer = input('Your answer: ')
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                x += 1
            else:
                print(
                    '"' + answer + '" is wrong answer ;(. '
                    'Correct answer was "yes". '
                    '\nLet\'s try again, ' + str(name))
                x = 0
        else:
            if answer == 'no':
                print('Correct!')
                x += 1
            else:
                print(
                    '"' + answer + '" is wrong answer ;(. '
                    'Correct answer was "no". '
                    '\nLet\'s try again, ' + str(name))
                x = 0
    print('Congratulations, ' + str(name) + '!')


if __name__ == '__main__':
    main()
