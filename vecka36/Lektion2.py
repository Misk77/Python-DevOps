######################### Lektion 2 vecka 2

""""
##### Skriva ut en hel  lista med for

# x = [0.2 2 3 9, 'jeff',28.768]

##### Skriva ut en lista med for upp till  9

x = [i for i in range(10)]
print(x)

"""

##### Skriva ut en lista med for upp till  9

"""
x = [i for i in range(10)if i >= 4]

print(x, )

"""
##### Skriva ut MODOLUS

###
"""
print('Modulus')

x = [(i % i) for i in range(1, 21)]

print(x)
"""
####### KLASSLISTA, UNDER LEKTIONEN

"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9.2,11]

print(x[-1:])
print(x[9:])
print(x[9])
print(x[-1:])
print(x[:-1])

"""
########  Multiplicera med elementet sig själv

"""

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9.10]

for x in range(10, ):
    x *= 2
    
print(x)
"""

"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
o = 0

while len(x) > o:
    x[o] = x * 2
    o += 1
    print([x])
"""
###### Listan rullar oändligt
"""
while x * 2:

    print(x)
"""

######  STRÄNG hantering

"""

largeStr = ('Kalle ANKA skulle GÅ till ANKEBORG men hade inga ankfötter som var dugliga för hans ändamål.')
secondStr = ('"Kalle" "gick" "hem" "istället"!!!!!')
isaplhaStr = ('! , 2,3,4')
int = (1, 2, 3, 4, 5, 6, 7, 8)
intList = [9, 10, 11, 12, 23]
print(largeStr[3])
print('-3: ', largeStr[-3])
print('Len: ', len(largeStr))
print('index', largeStr.index('till'))
print('Hela strängen: ', largeStr)
print('Lower: ', largeStr.lower())
print('capitalize: ', largeStr.capitalize())
print('swapcase: ', largeStr.swapcase())
print('casefold: ', largeStr.casefold())
print('center: ', largeStr.center(12))
print('isalpha: ', isaplhaStr.isalpha())
print('find: ', largeStr.find('kalle'))
# print(largeStr.replace())
# print(largeStr.split())
t = list(largeStr)
print('use list: ', t)
s = largeStr.split() # Dela upp strängen
print('split: ', s[10])  # ta fram delen av strängen/index som du vill se
delimiter = '"'
print(secondStr)
print('delimiter: ',secondStr.split(delimiter))
print(largeStr.join(secondStr))

"""
