#!/usr/bin/env python3

from random import randint, choice


def main():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, ' + str(name) + '!')
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
            correct_answer = number1 - number2
            if answer == correct_answer:
                print('Correct!')
                x += 1
            else:
                print(
                    '\'' + str(answer) + '\'' + ' is wrong answer ;(. '
                    'Correct answer was ' + '\'' + str(correct_answer) + '\'. '
                    '\n Let\'s try again, ' + str(name) + '!')
                x = 0
        elif operation == '+':
            print('Question: ' + str(number1) + ' + ' + str(number2))
            answer = int(input('Your answer: '))
            correct_answer = number1 + number2
            if answer == correct_answer:
                print('Correct!')
                x += 1
            else:
                print(
                    '\'' + str(answer) + '\'' + ' is wrong answer ;(. '
                    'Correct answer was ' + '\'' + str(correct_answer) + '\'. '
                    '\n Let\'s try again, ' + str(name) + '!')
                x = 0
        elif operation == '*':
            print('Question: ' + str(number1) + ' * ' + str(number2))
            answer = int(input('Your answer: '))
            correct_answer = number1 * number2
            if answer == correct_answer:
                print('Correct!')
                x += 1
            else:
                print(
                    '\'' + str(answer) + '\'' + ' is wrong answer ;(. '
                    'Correct answer was ' + '\'' + str(correct_answer) + '\'. '
                    '\n Let\'s try again, ' + str(name) + '!')
                x = 0
    print('Congratulations, ' + str(name) + '!')


if __name__ == '__main__':
    main()
