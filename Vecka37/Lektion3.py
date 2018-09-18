###################   LEKTION 3

##   RECAP exercise ranta

# 1000-1498 och 434-720
# med if-satser som är oberoende av varandra ,elif är beroende af if, då går det långsammare

"""
loan = float(input('Ange loan'))

if loan >= 1000 and loan <= 1498:
    nytt = loan * 0.63
    print('\nDu låna {0}'.format(loan))
if loan <= 999 and loan > 500:
    print('Du kan ej låna så lågt belopp')
"""
### Födelsekalas  mindre än 2 kalas, mer än 16 år
"""
age = int(input('Ange din ålder: '))

if age < 2 :
    print('Du får kalas')
elif age >= 16:
    
    print('tveksamt om du får kalas, ta mopeden och och iväg')
else:
    print('Ingen ide du komer då snart ändå')
"""

### OR villkor
""""
try:
    age = int(input('Ange din ålder: '))
    if age <= 2 or age > 60:
        print('Du får kalas')
    elif age >= 16 or age > 59:
        print('tveksamt om du får kalas, ta mopeden och och iväg istället')
    else:
        print('Ingen ide!! du kommer dö snart ändå\nBYE!')
except ValueError as e:
    print('Badness! {0}'.format(e))
"""

## STrängar , Formatering

### kon kate ner ing
## s operator - %s procenttecken och s

print()
strk1 = "kont"
strk2 = 'kate'
strk3 = 'ner'
strk4 = 'ing'
h = 'Strängar som använder %.f5'
print(strk1 + strk2 + strk3 + strk4)
print(strk1, strk2, strk3, strk4)
strHela = strk1, strk2, strk3, strk4
print(strHela)
strHela2 = strk1 + strk2 + strk3 + strk4
print(strHela2)

## s operator - %s procenttecken och s
## %c char tecken/utskrift(asci-tabelen)

print()
print("Hello %s, my name is %s" % ('john', 'mike'))
print('%s%s%s%s' % (strk1, strk2, strk3, strk4))
print('%.5s ' % (h))
print('{0}{1}{2}{3}'.format(strk1, strk2, strk3, strk4, ))
print()
x = 'j'
y = 'k'
print('%c ' % (67))
print('%s,%c,%c %s' % (strk1, x, y, strk2))
print()
z = 'Sa min gulliga fröken!'
print('%c är min favorit, %s ' % ('X', z))

# d DIGIT
# %d  ,  %f , samt lägger till antal decimaler du vill
print()
d = 23.2343
d2 = 23.988343
e = 1233323213123
f = 45435345.345345435453
f2 = 45435345.34534543545345
g = 0.14000
g2 = 0.14000
f3 = 0.1
com = 'computer'
name = 'Michel skoglund'
print('%d' % (d))
print('%d' % (d2))
print('%d' % (e))
print('%d' % (f))
print('%f' % (d2))
print('%f' % (f2))
print('%f' % (f2))
print('%.5f ' % (g2))
print('%.5f ' % (f))
print('%.5f ' % (f2))
print('%.5s ' % (h))
print('{:.2f}'.format(f2))
print('{:.5f}'.format(f2))
print('{:.5f}'.format(f3))
print()
print(name)
print(sorted(min(name)))
print(name)
print(sorted(max(name)))
print(name)
print(sorted((name.lower())))
print(name)
print(sorted((name.upper())))
print(name)
print(sorted((name.swapcase())))
print(name)
print(sorted((name.lower())))
print(name)
print(sorted((name.capitalize())))
print(name)
print(sorted((name.strip())))
print(name)
######  Hitta ett tecken 'tecken in variabel
strb = 'Nackademin'
print('a' in strb)
print('ade' in strb)
print(len(strb))
print(len(name))
print()

t = ['a,', 'b,', 'c,', 'd', 'e', 'f']
print(name[1:3])  # tar 1 och 2, stannar innan 3
print(name[:4])  # framåt till 3, stannar innan 4
print(name[4:])  # från 4 och framåt
print(name[:])  # hela listan, ?kopierad?
print()
print(name)
print(name.replace('Mich', 'apa'))  # change elements
print(name)
print(name.replace(name, 'Oliver'))
print(name.replace())
name.split