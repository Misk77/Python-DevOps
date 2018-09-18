########################    RECAP


############ Läxan: skriva ut alla element utan ' och  []

"""
aList = [[1, 'jonas', 2], [3, 4, 'kalle'], ['apa', 23.3, 345]]

for item in aList[0] + aList[1] + aList[2]:
    print(item, end=" ")

print()
"""

#####

"""
for item in aList[0] + aList[1] + aList[2]:
    print(' ')
    for item in aList[0] + aList[1] + aList[2]:
        print(item, end=" ")

"""

#####
"""
my_list = [26, 40, 'solna']
aList = [[1, 'jonas', 2], [3, 4, 'kalle'], ['apa', 23.3, 345]]

print('\n' + str(my_list ), '\n\n\n')

"""
######
"""
print()
aList = [[1, 'jonas', 2], [3, 4, 'kalle'], ['apa', 23.3, 345]]

for item in aList[0] + aList[1] + aList[2]:
    print(item, end=" ")
"""
####
"""
print()

# for item in aList:  lättast/enklast

for item in aList[0] + aList[1] + aList[2]:
    print(' ')
    for item in aList[0] + aList[1] + aList[2]:
        print(item, end=" ")

print()
"""
###########
"""
print()

bList = [1, 'jonas', 2, 3, 4, 'kalle', 23.3]
for i in range(len(bList)):
    print(bList[i], end='')
print()

####### 2d listor
print()
aList = [[1, 'jonas'], ['apa', 23.3, ]]

for r in aList:
    for k in r:
        print(k, ' ', end='')
print()
for r in aList:
    for k in r:
        print(k)
"""
######### Fler rads kommentarer
"""
print()

str = 
Flera
rader
sträng
gjord
med
trippel
citationtecken
"""

"""
print(str)
# str2 = """  # Enkel sträng med \"dubbla citationtecken\" tecken"""
# print(str2)
"""
"""

"""
### kon kate ner ing
"""
"""
print()
strK1 = "kont"
strk2 = 'kate'
strk3 = 'ner'
strk4 = 'ing'
print(strK1 + strk2 + strk3 + strk4)
strHela = strK1, strk2, strk3, strk4
print(strHela)
strHela2 = strK1 + strk2 + strk3 + strk4
print(strHela2)
"""
#### Villkorsats
"""
x = 7
y = 2
z = 8
if x == y == z:
    print('Alla har samma värde')

"""
### 
""""
a = 5
b = 7
c = 12

if a < b or b < c:
    print('a är mindre än b ELLER b är mindre än c')
"""
####### legera: ändra det som är falskt till tru med not efter if
"""
print()
x = 3
y = 4

if x < 3:
    print('X är tre')
elif x != y:
    print('x är inte lika med y')
elif x == y:
    print('X är lik amed y')
else:
    print('Something wrong')

print('Outside if ')
"""
############
"""
print()

for i in range(21):
    if i == 12:
        print(' number i loopen', i)
        break

print('Hittat ett sant villkor')

print('lämnat villkorssatsen')
"""
#############
"""
print()

name = (input('Vad heter du?: '))
print('Välkommen {0}!'.format(name))

name = 'Michel'
loggIn = input('Skriv ditt namn: ')

if name == loggIn:
    print('Välkommen {0}'.format(name))
elif loggIn != name:
    print('Hej {0}, Du har inte tillgång till detta konto, kontakta {1}'.format(loggIn, name))

#  1000-40 i procent
x=1000
y=40
k = (1000 * 0.40)
l = 1000 - 40
m = 960 / 100
print(m)

print(x*(y/100))

"""

#  LÅN på banken

# betalning via faktura koll
# ålder,inkomst ev kreditanmälningar gå igenom  villkor för att bli beviljad
"""
print()
age = int(input('Ange din ålder: '))
annualIncome = int(input('ange din årsinkomst'))

if age >= 18 and annualIncome > 12000:
    print('fakturabetalning beviljad.')
else:
    print('Tyvärr kan vi ej bevilja fakturabetalning.')

    # betalning via faktura koll
    # ålder,inkomst ev kreditanmälningar direkt ge svar vid något villkor som ej godkänt
    print()
"""
### råkat strulat till detta!! KOLLA FELET!!
while True:
    age = int(input('Ange din ålder: '))
    annualIncome = int(input('ange din årsinkomst'))

    if age < 18:
        print('Avslag')
    elif age >= 18:
        annualIncome = int(input('ange din årsinkomst: '))
    if annualIncome < 12000:
        print('Avslag')
    elif annualIncome >= 12000:
        anmarkning = (input('Har du betalningsanmärkning (1 = Ja / 2 = N?): '))
    if anmarkning == 'j':
        print('Avslag')
    elif anmarkning == 'n':
        print('Beviljad fakturabetalning')

###

"""
loan = float(input('Ange lån du vill ta: '))
ranta = float(input('Ränta är?: '))
nyPris = float((loan * ranta))

print('\nDu låna {0}'.format(loan))
print('\nDu har räntat {0}'.format(ranta))
print('\nDin totala återbetalning  blir: {0}'.format(nyPris))
"""

#######
"""
# totalBetalning = nyPris * loan

# print('Kontroll', totalBetalning)
"""
### Göra en ny med while True
