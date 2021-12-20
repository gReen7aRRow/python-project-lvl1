#!/usr/bin/env python3

from random import randint, choice
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
    print('What is the result of the expression?')
    x = 0
    while x < 3:
        number1 = randint(0, 50)
        number2 = randint(0, 50)
        mark = ['-', '+', '*']
        operation = choice(mark)
        if operation == '-':
            print('Question: ' + str(number1) + ' - ' + str(number2))
            answer = int(input('Your answer: '))
            sleep(1)
            correct_answer = number1 - number2
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
        elif operation == '+':
            print('Question: ' + str(number1) + ' + ' + str(number2))
            answer = int(input('Your answer: '))
            sleep(1)
            correct_answer = number1 + number2
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
        elif operation == '*':
            print('Question: ' + str(number1) + ' * ' + str(number2))
            answer = int(input('Your answer: '))
            sleep(1)
            correct_answer = number1 * number2
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
