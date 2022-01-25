#!/usr/bin/env python3

from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print('Hello, ' + str(name) + '!')
    print('What number is missing in the progression?')
    x = 0
    while x < 3:
        progression = []
        length = randint(6, 10)
        step = randint(7, 15)
        number = randint(5, 20)
        space = randint(5, length)
        for i in range(1, length + 1):
            if i == space:
                enigma = '..'
                progression.append(enigma)
                correct_answer = int(number)
                number += step
            else:
                progression.append(number)
                number += step
        print('Question: ' + str(progression))
        answer = int(input('Your answer: '))
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
