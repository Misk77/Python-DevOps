###### OOP - Object oriented Programmin
## Lektion 1

class Person:
    def __init__(self, name, age, country):
        self.all = name, age, country

    def playersall(self):  ## Gör en sträng av self.all
        return '{}'.format(self.all)


print('skriv in Player 1:')
person1 = Person(input('Vad heter du:\n'), int(input('Ange ålder:\n')), input('Ange Land:\n'))
print('skriv in Player 2:')
person2 = Person(input('Vad heter du:\n'), int(input('Ange ålder:\n')), input('Ange Land:\n'))
print('\nPlayers in the game are:\n')
print('Player 1')
for item in person1.all:
    print(item)
print()
print('Player 2')
for item in person2.all:
    print(item)

print('----------')

## skriv ut spara, KOLLA UPP KANSKE EJ HELT OKEJ
with open('players.txt', 'a+') as f:
    f.write(person1.playersall() + '\n' + person2.playersall())

print('--------------------')

for item in per():
    print(item,end='')

"""
# addTwo function
def addTwo(a, b):
    added = a + b
    return added


#### Skriv talen som går in i function addTwo
nbr1 = int(input('Ange tal: '))
nbr2 = int(input('Ange tal: '))
x = addTwo(nbr1, nbr2)

print(x)
"""
