###########   Lektion 1

######################  LISTOR  ##############################
# Man kan blanda olika datatyper i en lista str, int, float

"""

name = ['Michel', 'kalle', 'Kalle anka','Malin']  # str list
age = [41, 18, 100]  # int lista

print(name, age)
print()
print('name: {0} age: {1}'.format(name[2], age[2]))  # Indexera vilken du vill skriva ut

name[2] = ('Skoglund')
print('name: {0} age: {1}'.format(name[2], age[0]))  # Indexera vilken du vill skriva ut

print(len(name)) # 4 element name list
print(len(age)) #3 element i age list
print()
uppgifter = [name, age]
print(uppgifter)
print()

"""

#############  JEFF LISTA, under lektiontid

"""
jeff = ['Yellow', 'Green', 'Blue']
bilar = ['Volvo', 'Toyota', 'Skoda', 'volkswagen', 'Nissan']

jeffBilar = [jeff, bilar]

print(jeffBilar[0][0])
bilar.append('Jaguar')  # lägger till en bil
print()
print(jeffBilar)
bilar.remove(bilar[0])  # tar bort bil index 0
print()
print(jeffBilar)
print()
for i in range(5):
    print(jeffBilar[0])
print()
i = 0
while i < 5:
    i += 1
    print(jeffBilar)
"""
#####################################################################

"""
jeff = ['yellow', 'green', 'blue']
bilar = ['volvo', 'toyota', 'skoda', 'volkswagen', 'nissan']
jeffbilar = jeff + bilar
SearchVar = input('Vad letar du efter: '.lower())
for item in jeffbilar:
    if item == SearchVar:
        print('True ' ' -Jag hittade ditt ord')
        break
    elif item != SearchVar:
        print('false ' '-Din sökning gav inget')
        
        """

##################  Leta ett ord med for loop
# ## tuple = parenteser


## print(jeffbilar[2])

"""

jeff = ['yellow', 'green', 'blue']
bilar = ['volvo', 'toyota', 'skoda', 'volkswagen', 'nissan']
jeffbilar = jeff + bilar

SearchVar = (input('Vad söker du?: ').lower())

for item in jeffbilar:
    if item == SearchVar:
        print('Hittat din sökning\nDin sökning var {0}'.format(SearchVar))
        break
if item != SearchVar:
        print('Hittar INTE din sökning\nDin sökning var {0}'.format (SearchVar))
        
       """

####################### Logga in först, Mata in ett tal och välj räknesätt, vad som ska ske med talet

""""
countNbr = 0
name = 'Michel'
loggIn = input('Skriv ditt namna: ')

if name == loggIn:
    print('Välkommen {0}'.format(name))
else:
    print('Hej {0}, Du har inte tillgång till detta konto, kontakta {1}'.format(loggIn, name))
    countNbr = 1

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

"""

############### Skapa en dictionary
# Dictionary med måsvingar

"""
minabilar = {'jeff': 'volvo',
             'peter': 'toyota'}

print(minabilar)
print(minabilar.keys())

"""
################    Dictionary olika funktioner

"""
print()
person = {'name': 'Karin',  ## Dictionary det som står före colon är key till det som kommer efter
          'yrke': 'konsult',
          'adress': 'Solna'}

print(person)  # Skriver ut hela dictonary
print()
print(person['name'])  # skriver ut vad nyckel name innehåller
print()
person['name'] = 'Michel'  # Byter ut värdet i name key
print(person)
print()
print(person.keys()) # skriver ut vilka som är keys
print()
print(person.values()) # skriver ut vilka som är värde/element
print()
print(person.get()) # ??????????????????

"""
