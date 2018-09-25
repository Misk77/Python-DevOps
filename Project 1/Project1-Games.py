import random


class Person:
    def __init__(self, name, age, country):
        self.all = name, age, country

    def playersall(self):
        return '{}'.format(self.all)


antal = 0
user = int(input('Antal spelare'))
if antal < user:

    try:
        person1 = Person(input('Vad heter du:\n'), int(input('Ange ålder:\n')), input('Ange Land:\n'))
        print('skriv in Player 2:')
        person2 = Person(input('Vad heter du:\n'), int(input('Ange ålder:\n')), input('Ange Land:\n'))
    except IOError as e:
        print('Badness'.format(e))
    print('\nPlayers in the game are:\n')
    print('Player 1')
    for item in person1.all:
        print(item)
    print()
    print('Player 2')
    for item in person2.all:
        print(item)

    print('----------')

print()
while True:
    inp = input(
        'Press number for choose:\n[1] - addition\n[2] - olika uträkningar \n[3] - kasta tärning\n[4] - Gissa talet(1-50)\n[5] - Krona\\Klave\nTo exit write \'done\'\n')
    print()
    if 'done' == inp: break
    if 1 == float(inp):
        def addtwo(a, b):
            added = a + b
            return added


        tal1 = int(input('ange tal: '))
        tal2 = int(input('ange tal: '))

        print(addtwo(tal1, tal2))

    if 2 == float(inp):
        countNbr = 0

        try:
            while countNbr != 1:

                number = (int)(input('Mata in en siffra: '))

                countNbr = (int)(input(
                    "Vilken slags uträkning vill du göra?\n[1]-Avsluta\n[2]-Multplikation\n[3]Division\n[4]-Modulus\n[5]-Subtraktion\n[6]-Addition\n[7]-exponent\n"))
                if countNbr == 2:
                    print('Ditt tal muliplicerat med ditt tal blir: {}'.format(number * number))
                elif countNbr == 3:
                    print('Ditt tal Division med ditt tal blir: {}'.format(number / number))
                elif countNbr == 4:
                    print('Ditt tal Modulus med ditt tal blir: {}'.format(number % number))
                elif countNbr == 5:
                    print('Ditt tal Division med ditt tal blir: {}'.format(number - number))
                elif countNbr == 6:
                    print('Ditt tal Subtraktion med ditt tal blir: {}'.format(number + number))
                elif countNbr == 7:
                    print('Ditt tal exponent med ditt tal blir: {}'.format(number ** number))

        except:
            print("Det var inte en siffra, kolla upp vad en siffra är innan du fortsätter")

    if 3 == int(inp):
        class Tarning(object):
            def __init__(self, sidor=6):
                self.sidor = sidor
                self.kasta()
                self.__visar = 0

            def kasta(self):
                self.__visar = random.randrange(self.sidor) + 1

            def las(self):
                return self.__visar


        t = Tarning()
        t.kasta()
        print('Ditt kast blev: {}'.format(t.las()))

    if 4 == int(inp):
        try:
            x = random.randint(1, 51)
            gissa = 0
            while gissa != x:
                gissa = int((input('Gissa talet:\n')))
                if gissa == x:
                    break
                if gissa < x:
                    print('Talet är för lågt')
                if gissa > x:
                    print('Talet är för högt')
        except:
            print('Ange tal i siffror')

        print('Du gissade rätt!')

    guessRandomStuff = ['kalle', 1, 10, 'Bosse', 23.10, 'Guitar']
    coin = ['Krona', 'Klave']
    dice = [1, 2, 3, 4, 5, 6]

    print(random.choice(coin))

    ## skriv ut spara, KOLLA UPP KANSKE EJ HELT OKEJ
    with open('players.txt', 'a+') as f:
        f.write(person1.playersall() + '\n' + person2.playersall())

    print('--------------------')
