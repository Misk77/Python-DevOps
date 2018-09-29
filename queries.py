from Question import Question

### Frågorna i lista
question_prompts = [
    'What is the longest performing rock band in history?\n(a)Pink Floyd\n(b)Aerosmith\n(c)Rolling Stones\n',
    'When did Mick Jagger and Keith Richards form the Rolling Stones?\n(a)1950\n(b)1962\n(c)1974\n',
    'What was the name of the road that the Beatles famously crossed on their album cover?\n(a)Strawberry Fields Road\n(b)Liverpool Road\n(c)Abbey Road\n',
    'What are the Beatles\' names?\n(a)Ringo, George, Paul, John\n(b)Ringo, Geoff, Paul, James\n(c)Ringo, Jim, Paul, John\n',
    'Which one of AC/DC\'s albums is the 5th largest-selling album ever?\n(a) Highway to Hell\n(b)Back in Black\n(c) T.N.T.\n',
    'True or False: AC/DC is in the Rock and Roll Hall of Fame.?\n(a)True\n(b)False\n(c)Only some original members are in the Hall of Fame.\n',
    'Why did Led Zeppelin break up in 1980??\n(a)Conflict between band members\n(b)Jimmy Page wanted out of the band\n(c)The death of John Bonham\n',
    'When Jimmy Page formed the group in 1968, what was Led Zeppelin originally called?\n(a)The Lightning Bolts\n(b)The New Yardbirds\n(c)The Classic Curse\n',
    'What is the name of the final album released under the Pink Floyd name??\n(a)The Dark Side of the Moon\n(b)Wish You Were Here\n(c)The Endless River\n',
    'Since leaving Pink Floyd, what does Roger Waters do?\n(a)Act in off-broadway shows\n(b)Sing opera\n(c)Direct movies\n',
    'Who was the only member of Guns \'N\' Roses to get a high school diploma?\n(a)Slash\n(b)Axl\n(c)Izzy\n',
    'What is Slash\'s (Guns \'N\' Roses) real name\n(a)Saul Hudson\n(b)Samuel Hammond\n(c)Sean Hunter\n',

]

## ställer frågan och kolla rätt svar, frågorna och rätt svar

questionsHardrock = [
    Question(question_prompts[0], 'c'),
    Question(question_prompts[1], 'b'),
    Question(question_prompts[2], 'c'),
    Question(question_prompts[3], 'a'),
    Question(question_prompts[4], 'b'),
    Question(question_prompts[5], 'a'),
    Question(question_prompts[6], 'b'),
    Question(question_prompts[7], 'b'),
    Question(question_prompts[8], 'c'),
    Question(question_prompts[9], 'b'),
    Question(question_prompts[10], 'c'),
    Question(question_prompts[11], 'a'),

]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + ' correct')


inp = int(input('Wich quiz you wanna do?\n'
                '[1]- Hardrock quiz\n'
                '[2] - Avsluta\n'))
if inp == 1:
    run_quiz(questionsHardrock)
if inp == 2:
    exit()
