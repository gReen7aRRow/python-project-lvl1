import prompt


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!' .format(name))
    print(game.DESCRIPTION)
    for x in range(0, 3):
        correct_answer, question = game.get_question_and_answer()
        print('Question: {}' .format(question))
        answer = input('Your answer: ')
        if str(answer) == str(correct_answer):
            print('Correct!')
        else:
            print('\'{0}\' is wrong answer ;(. Correct answer was \'{1}\'.'
                  '\nLet\'s try again, {2}!'
                  .format(answer, correct_answer, name))
            return
    print('Congratulations, {}!' .format(name))
