#!/usr/bin/env python3

from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, ' + str(name) + '!')
    print('Find the greatest common divisor of given numbers.')
    x = 0
    while x < 3:
        number1 = randint(1, 50)
        number2 = randint(1, 50)
        print('Question: ' + str(number1) + ' ' + str(number2))
        answer = int(input('Your answer: '))
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
        else:
            print(
                '\'' + str(answer) + '\'' + ' is wrong answer ;(. '
                'Correct answer was ' + '\'' + str(correct_answer) + '\'. '
                '\nLet\'s try again, ' + str(name) + '!')
            break
        if x < 3:
            pass
        elif x == 3:
            print('Congratulations, ' + str(name) + '!')
            break


if __name__ == '__main__':
    main()
