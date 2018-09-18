# print(type(int(x2)))  # x2 = 'tio' ska bli int


##################### Lista
#####
"""
aList = [1, 'jonas', 2, 3, 4, 'kalle', 23.3]
print()
aList.remove(aList)
print(aList)
"""
"""
bList = [1, 'jonas', 2, 3, 4, 'kalle', 23.3, 8, 'NIO']
# print(len(bList))
"""

###############  For loop i input som frågar efter ett värde 4 gånger

"""
x = [input('Skriv ett värde: ') for i in range(4)]
"""

"""
x = [input('Skriv ett värde: ') for i in range(1)]
"""

"""
### ALT 1

aList = [[1, 'jonas', 2], [3, 4, 'kalle'], ['apa', 23.3, 345]]

for item in aList[0] + aList[1] + aList[2]:
    print(item, end=" ")
"""

##

"""
## ALT 2

for item in aList[0] + aList[1] + aList[2]:
    print(' ')
    for item in aList[0] + aList[1] + aList[2]:
        print(item, end=" ")

"""
"""
######
"""
"""
print()
aList = [[1, 'jonas', 2], [3, 4, 'kalle'], ['apa', 23.3, 345]]

for item in aList[0] + aList[1] + aList[2]:
    print(item, end=" ")

####
print()

# for item in aList:  lättast/enklast

for item in aList[0] + aList[1] + aList[2]:
    print(' ')
    for item in aList[0] + aList[1] + aList[2]:
        print(item, end=" ")

print()
###########
print()

bList = [1, 'jonas', 2, 3, 4, 'kalle', 23.3]
for i in range(len(bList)):
    print(bList[i], end='')
print()

####### 2d listor
"""
"""
print()
aList = [[1, 'jonas'], ['apa', 23.3, ]]

for r in aList:
    for k in r:
        print(k, ' ', end='')
print()
for r in aList:
    for k in r:
        print(k)

######### Fler rads kommentarer
"""

print()
str = """Flera
rader
sträng
gjord med trippel citationtecken
\"\"\""""
print(str)
str2 = """Enkel sträng med \"dubbla citationtecken\" tecken"""
print(str2)

### kon kate ner ing
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
a = 5
b = 7
c = 12

if a < b or b < c:
    print('a är mindre än b ELLER b är mindre än c')
"""
print()
a = 4
b = 5
c = 12

if a < b and b < c and c < a:
    print('TRUE')

"""   
else:
    print('False')
"""

print('Done')
