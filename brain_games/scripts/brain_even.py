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
    while x <= 5:
        if x < 3:
            number = randint(1, 20)
            print('Question: ' + str(number))
            answer = input('Your answer: ')
            if number % 2 == 0:
                correct_answer = 'yes'
                if answer == correct_answer:
                    print('Correct!')
                    x += 1
                else:
                    print(
                        '"' + answer + '" is wrong answer ;(. '
                        'Correct answer was "' + correct_answer + '"'
                        '\nLet\'s try again, ' + str(name))
                    break
            else:
                correct_answer = 'no'
                if answer == correct_answer:
                    print('Correct!')
                    x += 1
                else:
                    print(
                        '"' + answer + '" is wrong answer ;(. '
                        'Correct answer was "' + correct_answer + '"'
                        '\nLet\'s try again, ' + str(name))
                    break
        if x < 3:
            pass
        elif x == 3:
            print('Congratulations, ' + str(name) + '!')
            break


if __name__ == '__main__':
    main()
