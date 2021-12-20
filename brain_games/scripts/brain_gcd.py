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
    print('Find the greatest common divisor of given numbers.')
    x = 0
    while x < 3:
        number1 = randint(1, 50)
        number2 = randint(1, 50)
        print('Question: ' + str(number1) + ' ' + str(number2))
        answer = int(input('Your answer: '))
        sleep(1)
        if number1 > number2:
            correct_answer = number2
            while correct_answer > 0:
                if number1 % correct_answer == number2 % correct_answer:
                    if number1 % correct_answer == 0:
                        break
                    else:
                        correct_answer -= 1
                else:
                    correct_answer -= 1
        else:
            correct_answer = number1
            while correct_answer > 0:
                if number1 % correct_answer == number2 % correct_answer:
                    if number1 % correct_answer == 0:
                        break
                    else:
                        correct_answer -= 1
                else:
                    correct_answer -= 1
        if answer == correct_answer:
            print('Correct!')
            x += 1
            sleep(1)
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
