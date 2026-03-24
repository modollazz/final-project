import random


def get_question_and_answer(questions: list, answers: list, asked: list) -> list:
    # TODO corner case
    r = random.randint(0, len(questions) - 1)
    while r in asked:
        r = random.randint(0, len(questions) - 1)

    asked.append(r)

    result = [questions[r], answers[r]]

    return result

if __name__ == '__main__':
    print('good luck on the quiz!')

    questions = [
        'What pop singer shaved their hair off due to a mental breakdown in 2007?',
        'What song made Justin Bieber famous?'
        'How many members are in Destiny\'s Child?'
        'In what year, did the King of Pop Michael Jackson die in?'
        'Which female singer owns the makeup brand Fenty Beauty?'
        'What is the name of the artist that showed up to the MTV Awards in a meat dress?'
        'Which Harlem rapper do Rihanna have three kids with?'
        'What is the name of the show Drake was in before becoming a rapper?'
        'Who performed at the SuperBowl in 2025?'
        'What movie was the music video "Fancy" by Iggy Azelea inspired by?'
    ] 

    answers = [
        'britney spears',
        'baby'
        '3'
        '2009'
        'rihanna'
        'lady gaga'
        'asap rocky'
        'degrassi'
        'kendrick lamar'
        'clueless'
    ]

    asked = []

    i = 0
    while i < len(questions):

        q_and_a = get_question_and_answer(questions, answers, asked)

        response = input(q_and_a[0] + ' ')

        if response == q_and_a[1]:
            print('correct!')
        else:
            print('incorrect ...')

        i += 1 
