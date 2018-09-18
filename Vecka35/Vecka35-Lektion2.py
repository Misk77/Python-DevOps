import random
import sys
import os

## Under Lektionstid :
#

""" Under Lektionstid

"""
"""
print("'Nackademin' i Solna")

"""

#
#
"""
print()
x = 100
if x == 100:
    print('X är 100, det stämmer')
else:
    print('X Är inte i 100, stämmer inte') """


"""
name = 'Michel'
loggIn = input('Skriv ditt namna: ')

if name == loggIn:
    print('Välkommen {0}'.format(name))
elif loggIn != name:
    print('Hej {0}, Du har inte tillgång till detta konto, kontakta {1}'.format(loggIn, name)) """


"""
input()
x = 10
if x == 30:
    print('X är 30')
elif x < 30 or x > 30:
    print('X är mindre eller större än 30') """

######
""""
print()
#  Function har parenteser efter sig
#  random.randrange()  , funktionen

###############################################################
####    Stanna på 20
################################################################

i = 0 # räknar antal varv

while (random.randrange(0, 101) != 20): # randomnbr mellan 1-100, så länge den ej slumpar 20
    i += 1

    print('Antal varv: {0}, RandomNbr: {1} '.format(i, random.randrange(0, 101))) # Skriver ut antal varv och randomnbr

"""



###############################################################
####     SLumpa gissa talet
################################################################3
"""
    randomNbr = random.randrange(0, 101)

    print()

while randomNbr != userNbr:
    userNbr = (int)(input('Gissa på ett tal: '))
    if userNbr != randomNbr and randomNbr <= randomNbr:
        print('Talet är lågt, gissa igen: ')
    elif userNbr != randomNbr and randomNbr >= randomNbr:
        print('Talet är högt, gissa igen: ')
    elif userNbr == randomNbr:
        print('Grattis du gissade rätt,  talet är: {1}'.format(randomNbr))"""

print()

#################################  Gjorda uppgifter     #################################

"""Öv 1.
- Skapa en variabel som du tilldela ett initialt värde.
- Använd en logisk(jämförelse) operator för att kontrollera olika handlingar mot variabeln
- Gör en utskrift på skärmen för att kontrollera att handlingar  fungerar korrekt.
Använd gärna även parenteser i dina uttryck
 """

# Exempel 1
"""
print()

print()
x = 2
if x == 7:
    print('X är sju')
else:
    print('X är inte sju')  """

# Exempel 2 med str ifall namnet är fel fråga ?
"""
print()

name = ('Michel') # bestämd var med värdet Michel

user = (input('Vem är du?: ')) # fråga användaren vem hon är sedan skriver ut alternativ
if user == name:
    print('Hej {}' .format(name))
elif user != name:
    print('Vem är du? vart är Michel?')"""

"""Öv 2. - Utöka din kod för att samtidigt kontrollera flera 
villkor och utföra koden  som finns i 
villkoret som stämmer överens med det du kontrollerar. """

# Exempel 1 , är vattnet varm så badar vi, annars alternativ
"""
print()
temp = (int(input('Hur många grader är vattnet: ')))

if temp >= 25:
    print('Vi badar')
elif temp >= 10 and temp <= 24:
    print('*Är du säker, inte så varmt i vattnet...')
elif temp < 10:
    print('Vi kommer INTE bada!') """

""" Öv3.  
- Kombinera dina villkor i ett 
uttryck med 
logiska operatorer and, or, not """

# Exempel 1 , kolla om man får ta körkort
"""
print()
age = (int(input('Ange din ålder: ')))

if age < 18 :
    print('Du får vänta med körkortet')
elif age >= 18 and age < 100:
    print('Du får ta körkort')
elif age >= 100:
    print('Du får köra bil om du har körkort, men kanske inte så lämpligt?') """

# for satser
"""Öv 4. 
- Skriv en for som upprepar en handling i tio gånger.
 - Gör en utskrift på skärmen för att kontrollera.  
 """
"""
print()
for i in range(10):  # räka upp till 4, mindre än 5
    print(i) """

# for sats inuti forsats

""" Öv 5. 
Skriv en for sats inuti en annan för att utföra olika handlingar. 
Gör en utskrift på skärmen för att kontrollera.  
 """

"""
for i in range(10):
    print('Nu skriver I'), (i)
    for x in range(10):
        print('Nu skriver X'), (x) """
