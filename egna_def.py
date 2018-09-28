# coding=utf8
# -*- coding: utf-8 -*-


def area_rektangel(base, height):
    try:
        print()
        print('Ange basen och höjden i triangeln, så beräknar vi arean')
        base = float(input('Ange basen: '))
        height = float(input('Ange höjden: '))
        Area = float(base * height) / 2
        print('Arean på triangeln är {}'.format(Area))
    except ValueError as e:
        print('Ange i siffror ej text: {}'.format(e))


def rabatt():
    try:
        pris = float(input('Ange produktens summa: '))
        rabatt = float(input('Ange rabatten i procent form: '))
        medRabatt = pris * rabatt
        rabatteratPris = pris - medRabatt
        print('Du skrev in pris: {0} och rabatten: {1}. Ditt rabatterande pris blir: {2} '.format(pris, rabatt,
                                                                                                  rabatteratPris))
    except ValueError as e:
        print('Ange i siffror ej text: {}'.format(e))


def tankad():
    try:
        volym = float(input('Ange tankad volym: '))
        pris = float(input('Ange liter priset: '))
        betala = volym * pris

    except ValueError as e:
        print('Ange i siffror ej text: {}'.format(e))

    print("""\n
    +---------------------------------+
    |           KVITTO                |
    |                                 |
    |  Tankad volym {0} liter       | 
    |   Pris per liter {1} kronor    |
    |  Betala kronor {2}           |
    |                                 |
    |    Tack för besöket och         |
    |    välkommen åter!              |                            |
    +---------------------------------+""".format(volym, pris, betala))


def bmi_culc():
    try:
        lenght = int(input('Ange din längd: '))
        weight = int(input('Ange din vikt: '))
        lenght /= 100
        bmi = weight / (lenght * lenght)
        print()
        if bmi < 18.5:
            print('Ditt bmi är: {:.2f}'.format(bmi))
            print('Du har undervikt')
        elif bmi >= 18.5 or bmi < 25:
            print('Ditt bmi är: {:.2f}'.format(bmi))
            print('Du har normalvikt')
        elif bmi >= 25 or bmi < 30:
            print('Ditt bmi är: {}'.format(bmi))
            print('Du har övervikt')
        elif bmi > 30:
            print('Ditt bmi är: {}'.format(bmi))
            print('Du har tyvärr fetma')
        else:
            print('Något blev fel')
    except ValueError as e:
        print('Ange i siffror ej text: {}'.format(e))


def skottyear():
    try:

        year = int(input('Ange årtal: '))

        if year % 4 == 0:
            print('Du skrev in årtalet: {}'.format(year))
            print('Det är skottår')
        elif year == 1700 or year == 1800 or year == 1900:
            print('Du skrev in årtalet: {}'.format(year))
            print('Årtalet är 1800 eller 1900 och var ej skottår')
        else:
            print('Du skrev in årtalet: {}'.format(year))
            print('Det var inte skottår')
    except ValueError as e:
        print('Ange i siffror ej text: {}'.format(e))


def sum_mv():
    while True:
        try:
            antal = int(input('Ange hur mång atal du vill skriva in: '))
            summa = 0
            for i in range(1, antal + 1):
                tal = float(input('Ange tal: ' + str(i) + ': '))
                summa += tal
            print('Summan av dom inmatade talen är {:.2f}'.format(summa))
            print('Medelvärdet av talen är {:.2f}'.format(summa / antal))
            forst = input('Vill du forsätta eller avsluta [j/n]')
            if forst == 'n':
                break
        except ValueError as e:
            print('Ange i siffror ej text: {}'.format(e))

print('Okej, hejdå')


def reverse():
    try:
        s = input('Skriv något')
        lgd = len(s)
        print('Du skrev in {} tecken'.format(lgd))
        print(s)
        i = lgd - 1
        print('Baklänges blir det: ')
        while i >= 0:
            print(s[i], end='')
            i -= 1
    except ValueError as e:
        print('Ange i siffror ej text: {}'.format(e))


def listantal():
    try:
        tal = []
        for i in range(1, 11):
            tal.append(float(input('Ange tal ' + str(i) + ': ')))

        print('inmatade tal')
        for x in tal:
            print(x)

        minsta = tal[0]
        for i in tal:
            if i < minsta:
                minsta = i
        print('Minsta talet: ', minsta)
        print('Minsta talet: ', min(tal))  # inbyggd function för att hitta minsta talet
        print('Största talet: ', max(tal))  # inbyggd function för att hitta största talet
    except ValueError as e:
        print('Ange i siffror ej text: {}'.format(e))

def calculation():
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
