###### OOP - Object oriented Programmin
## Lektion 1

class Person:
    def __init__(self, name, age, country):
        self.all = name, age, country


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



# addTwo function
def addTwo(a, b):
    added = a + b
    return added


#### Skriv talen som går in i function addTwo
nbr1 = int(input('Ange tal: '))
nbr2 = int(input('Ange tal: '))
x = addTwo(nbr1, nbr2)

print(x)

# Instans: skapa verkliget object av class
"""
Person1 = Person()
print(Person1)

Person2 = Person()
print(Person2)
print('-------Person1---------')
# Instans
Person1.name = 'Michel'
print(Person1.name)
Person1.age = 42
print(Person1.age)
Person1.country = 'Sweden'
print(Person1.country)
print('----------------')
print(Person1.name, Person1.age, Person1.country)

print('-------Person2---------')

Person2.name = 'Stina'
print(Person2.name)
Person2.age = 13
print(Person2.age)
Person2.country = 'Krigslida'
print(Person2.country)
print('----------------')
print(Person2.name, Person2.age, Person2.country)

"""
#### Michel funtion
"""

def Michel(name, age):
    print(name)
    print(age)


name = input('Vad heter du: ')
age = int(input('Ange ålder'))
print(Michel(name, age))
"""
