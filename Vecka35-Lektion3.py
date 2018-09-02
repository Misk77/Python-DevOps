import random
import sys
import os

## Under Lektionstid :
#


####  RECAP:
# end = " " tar bort radbrytning


"""
i = 0  # räknar antal varv

while (random.randrange(0, 101) != 20):  # randomnbr mellan 1-100, så länge den ej slumpar 20
    i += 1

    print('Antal varv: {0}, RandomNbr: {1} '.format(i, random.randrange(0, 101)))  # Skriver ut antal varv och randomNbr
    """
print()

############   for satsen   #################
#  range() tar

##############################    multiplikationtabell    """"""""""""""""""""""""""""""""""""""""""""""""

"""
x = (int)(input('Vilken multiplikationtabell du vill se: '))

for i in range(11):
    value = x * i
    print("{} * {} = {}".format(x, i, value))

"""

##############################    exponent    """"""""""""""""""""""""""""""""""""""""""""""""

""""
x = (int)(input('Vilken exponenttabell du vill se: '))

for i in range(11):
    value = x ** i
    print("{} * {} = {}".format(x, i, value))
    
"""

#################  Matris ,
"""
x = 0
y = 0
while y < 4:
    y += 1
    for x in range(0, 4):
        print("\n|---------------|")
        print(("|"), end="")
        for y in range(0, 4):
            print((" * "), end="|")
   
print("\n|---------------|")

"""

################# Reversed range  reversed(range(0, 11))
"""
for x in reversed(range(0, 11)):
    x **= x
"""
##################### Matriss ####################

"""
for x in range(0, 4):
        print("\n|---------------|")
        print(("|"), end="")
        for y in range(0, 4):
            print((" * "), end="|")
            

"""

## ALT 2
"""
for r in range(0, 4):
    print()
    for k in range(0, 9):
        print(('*'),end='')
        
        """

####### X ska bli Y

"""
x = 10
y = 20

z = x # skapa tom variabel som tar x värdet
x = y # x får y värdet 
y = z # y får z värdet som har gamla x värdet

print(x, y)

"""

####### X ska bli Y *** ONELINERS


#### Byta värdet med python inbygga byta värde mellan variabler

"""
x,y = y,x  # uttryck som anropar funktionen som byter värde på variablen

print(x, y)
"""

############

"""

for x in range(0, 4):
    print("\n|---------------|")
    print(("|"), end="")
    for y in range(0, 4):
        print((" * ", y**4), end="|")
print("\n|---------------|")

"""
##################

"""
for x in range(0, 4):
    print("\n", "")
    for y in range(0, 4):
        print((" {0} ".format((y ** 4), end=" ")))
print("\n|---------------|")
"""

#####  STRING Genomgång i klassrummet

"""
print('vad heter du? ')
name = sys.stdin.readline()
print("Välkommen {0}!".format(name))

name = (input('Vad heter du?: '))
print('Välkommen {0}!'.format(name))

name = 'Michel'
loggIn = input('Skriv ditt namn: ')

if name == loggIn:
    print('Välkommen {0}'.format(name))
elif loggIn != name:
    print('Hej {0}, Du har inte tillgång till detta konto, kontakta {1}'.format(loggIn, name))

"""
#################################  Gjorda uppgifter     #################################


#######   while -SATSER   ÖVNINGAR

##########   Öv 1.
###############  While loopen kör antal varv
"""

-    Skapa en variabel och tilldela den ett initialt värde.
-    Använd variabeln för att skriv en
      while sats som upprepas  ett antal gånger.


x = 0
while x < 3:
    x += 1
    print(x)

"""

######  Öv 3.

"""

-	Skriv en evighets while sats 


while y < 4:
y += 1
for x in range(0, 4):
    print("\n|---------------|")
    print(("|"), end="")
    for y in range(0, 4):
        print((" * "), end="|")

print("\n|---------------|")

"""

###########################     STRÄNGAR     #############################################


#####         Öv 1
#####        - Skapa på olika sätt en variabel som

# Om Du måste använda " eller ' mellan samma citationstecken då måste Du använda en \  # tecken framför tecknet

"""
str =("\" och \\")
print(str)

"""

#####         Öv 2
#####  -	Skapa en sträng med lämpligt innehåll där även citationstecken är en del av strängen

"""
string = ("'Nacka' ligger i sthlm")
print(string)

"""

#####         Öv 3
##### - Skapa en sträng med lämpligt innehåll där även det bakåtlutande tecknet (\ ) är en del av innehållet i strängen.

"""
print('Nu ska vi skriva Backslash \\ i texten')
"""

#####         Öv 4
##### -  -	Skapa en sträng som innehåller flera rader

"""
print("Skriver\nUt på \n lera rader med \n\\n")

"""

#####         Öv 5
##### - 	Skapa två olika strängar. Slå ihop stängarna till en sträng

"""

förnamn = "Michel"
efternamn = "Skoglund"

print(förnamn, efternamn)
print("Kalle " + "Anka")

"""


