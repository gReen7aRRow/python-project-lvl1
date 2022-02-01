#!/usr/bin/env python3

from random import randint, choice
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(
        'Hello, ' + str(name) + '! '
        '\nWhat is the result of the expression?')
    x = 0
    while x < 3:
        number1 = randint(0, 50)
        number2 = randint(0, 50)
        mark = [' - ', ' + ', ' * ']
        operation = choice(mark)
        print('Question: ' + str(number1) + str(operation) + str(number2))
        answer = int(input('Your answer: '))
        if operation == ' - ':
            correct_answer = number1 - number2
        elif operation == ' + ':
            correct_answer = number1 + number2
        elif operation == ' * ':
            correct_answer = number1 * number2
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
