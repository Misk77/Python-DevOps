####################### LEKTION 1

#######  Filhantering I/O
#
"""
my_file = open('textfil.txt', 'w')

my_file.write('Hej kalle anka\nThis is my textdokument made from python console\n')
my_file.write('\nGitarrer: \nGibson\nIbanez\nFender\n')
my_file.write('\nGitarrister:\nSLASH\nMark Knopfler\nJoe satriani')
my_file = open('textfil.txt', 'r+')

print(my_file.name)
print(my_file.mode)
print(my_file.read())
print()
my_file.close()
print(my_file.closed)
my_file = open('textfil.txt', 'r+')
print(my_file.read())
print(my_file.mode)
print(my_file.tell())
print('\nLägger till text efter allt är gjort')
print(my_file.read())
print(my_file.seek(100))
print(my_file.read())
my_file = open('textfil.txt', 'a')

my_file.write('\nSkriver in och  lägger in ny text  med append \'a\'')
my_file = open('textfil.txt', 'r+')
print(my_file.read())
"""
"""
with open('rader.txt', 'a') as my_file2:
    textinput = input('skriv till filen:\n ')
    my_file2.write('\n' + textinput)
    
    with open('rader.txt', 'r+') as my_file2:
        print(my_file2.read())
for f in open("fillista.txt", "r"):
    copy2(string.strip(my_file2), my_file)
"""
print()
print('--------DONE------')

"""
 textinput = input('skriv till filen: ')

with open('textfil.txt', 'r+') as my_file2:
   print(my_file2.read())
"""
##### Kopiera en fil
# open'Orginalfilen', gör den readable med variabel rf
# skapa en till fil i open(), som blir kopia open('kopia','w') som ska vara writeable
# sedan tar allt i orginal variabel och kopiera med line med for hjälp
# kopia variabel som är write wf,write och fyll med line från rf variabel

try:
    with open('rader.txt', 'a') as rf:
        textinput = input('skriv till filen: ')
        rf.write('\n' + textinput)
        with open('rader.txt', 'r+') as rf2:
            print(rf2.read())
        with open('Kopia.txt', 'w') as wf:
            for line in rf2:
                wf.write(line)
except IOError as e:
    print(rf2, '{}'.format(e))
