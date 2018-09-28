###
# -*- coding: utf-8 -*-
### ringar
# forward , fd (sträcka)
# back , bk  (sträcka)
# penup , pu
# hideturtle , hd ()
# showturtle , st ()
# left , lt (grader
# right , rt (grader)
# goto(x,y)
# pencolor(ritfärg)
# bgcolor(bakgrundsfärg)
# spped(hastighet
# screensize(  , screensize(200,200)
# fönstrets storlek pixlar el procent
# color(pennfärg,bakgrundsfärg)
# start_fill()
# end_fill()
### Slutna figurer kan man fylla i, för samtidigtr fylla i
# ange fyllnads och bakgrundsfärg, color(penn,bakgrun)
# före och efter ritning av den fyllda figuren ska man
# använda start och end
#####

from turtle import *

setup(width=800,height=600)
setworldcoordinates(-200,-150,200,150)
speed(0)
ht()
colormode(255)
bgcolor(0,0,0)
pencolor(255,255,255)
pensize(3)

for i in range(40):
    lt(9)
    circle(70)


done()
