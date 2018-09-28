# -*- coding: utf-8 -*-
# coding=utf8
import egna_def

a, b = 0, 0
while True:
    print()
    inp = input("""Ange vad du vill göra: 
              \n[1]-Räkna ut area på rektanel
              \n[2]-Ta reda på rabatterad pris
              \n[3]-Räkna ut bensin priset
              \n[4]- Räkna ut ditt bmi
              \n[5]-Ta reda på vilket år som är skottår
              \n[6]-Ta redan på summan och medelvärde av olika tal
              \n[7]-Ta reda på vad ett ord blir baklänges
              \n[8]-Vill du skriva in 10 tal  i en lista och se största resp minsta talet
              \n[9]-beräkning med ett tal""")
    if inp == '1':
        egna_def.area_rektangel(a, b)
    if inp == '2':
        egna_def.rabatt()
    if inp == '3':
        egna_def.tankad()
    if inp == '4':
        egna_def.bmi_culc()
    if inp == '5':
        egna_def.skottyear()
    if inp == '6':
        egna_def.sum_mv()
    if inp == '7':
        egna_def.reverse()
    if inp == '8':
        egna_def.listantal()
    if inp == '9':
        egna_def.calculation()
