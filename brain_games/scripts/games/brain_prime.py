#!/usr/bin/env python3

from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(
        'Hello, ' + str(name) + '! '
        '\nAnswer "yes" if given number is prime. Otherwise answer "no".')
    x = 0
    while x < 3:
        number = randint(3, 50)
        print('Question: ' + str(number))
        answer = input('Your answer: ')
        y = number - 1
        correct_answer = 'yes'
        while y > 1:
            if number % y == 0:
                correct_answer = 'no'
                break
            else:
                y -= 1
        if answer == correct_answer:
            print('Correct!')
            x += 1
        else:
            print(
                '\'' + str(answer) + '\'' + ' is wrong answer ;(. '
                'Correct answer was ' + '\'' + str(correct_answer) + '\'. '
                '\nLet\'s try again, ' + str(name) + '!')
            break
        if x == 3:
            print('Congratulations, ' + str(name) + '!')
            break


if __name__ == '__main__':
    main()
