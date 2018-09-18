import random
import os
import sys








#################################  Gjorda uppgifter     #################################

# Övning 2
# Detta är en kommentar
print('Hello World')
name = (input('Hej vad heter du?: '))  # Tar in ditt namn
print('Hello {} '.format(name))  # Skriver ut text plus namnet

"""Ov 3. 
- Lägg in en rader eller flerarader kommentarer 
i ditt program. Kontrollera att ditt program  
exekverar felfritt. """

print()
print('Vi kan byta rad med backslash också så\nså här  \\n  Nu\nbyter\ni rad')

print('Hej \" \" @Michel')
print()
print("""Hej Michel
Nu byter vi rad
igen""")
print()
print('Nackademin i solna')
print('\"Nackademin i solna\"')
print("\"nackademin \"i solna")
"""Detta är en kommentar som inte kommer göra någonting i programmet"""
print((1 + 2 - 10) * 4)
print(5 ** 10)

"""Öv 5. 
- Skapa en variabel som lagrar
 ditt för och efternamn Skriv ut variabelns innehåll ut på skärmen """
print()
name = 'Michel'
lastName = 'Skoglund'
print(name, lastName)
print(name + lastName)
print('{0} {1}'.format(lastName, name))
print('{1} {0}'.format(lastName, name))
print('{0} {1}'.format(name, lastName))
print('{1} {0}'.format(name, lastName))

"""ÖV 6.
 - Lägg upp några matematiska beräkningar 
med användning av olika  aritmetiska operatorer """
print((1 + 2 - 10) * 4)
print(10 * 100 - 3)  # vänster till höger, prioteringregeln
print(10 * (100 - 3))  # vänster till höger, prioteringregeln med parentes regeln
print(10 * (100 - 70))  # som ovan fast tydligare vad som händer
print()

"""Öv7. 
- Skapa en variabel och tilldela den att värde. 
Öka eller minska variabelns värde På olika sätt. 
Skriv ut resultat på skärmen och kontroller att det stämmer överens """
print()

x = 7
x += x
print(x)
print()
y = 10
x = 100
c = x + y
print(c)

x *= 10
print(x)
x -=5
print(x)
x %=10
print(x)

