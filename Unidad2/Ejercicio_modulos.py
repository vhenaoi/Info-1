### Ejercicio ###
'''Utilizando el teorema de seno y el coseno, 
diseñar un algoritmo que pregunte por la información a ingresar 
(Lado-Ángulo-Lado o Ángulo-Lado-Ángulo), calcule e imprima los demás lados 
y ángulos de un triángulo cualquiera.
'''

import math
import numpy as np
from mifuncion import seno,coseno
from funciones.lafuncion import laclase,holaclase


while True:
    opcion=int(input('1. Lado-Ángulo-Lado \n2. Ángulo-Lado-Ángulo \n3. Salir \nOpnción: '))
    if opcion == 1:
        a = float(input('Lado a: '))
        C = int(input('Ángulo C: '))
        b = float(input('Lado b: '))
        c = (a**2) + (b**2) - 2*a*b*coseno(C)
        A = math.asin((a*seno(C))/c)
        B = 180-A-C
        print(f'Los lados del triangulo son a: {round(a,2)}, b: {round(b,2)}, c: {round(c,2)} y los ángulos son A: {round(A,2)}, B: {round(B,2)}, C: {round(C,2)}')
    elif opcion == 2:
        A = int(input('Ángulo A: '))
        a = float(input('Lado a: '))
        C = int(input('Ángulo C: '))
        c = (a*seno(C))/seno(A)
        B = 180-A-C
        b = (a**2) + (c**2) - 2*a*c*coseno(B)
        print(f'Los lados del triangulo son a: {round(a,2)}, b: {round(b,2)}, c: {round(c,2)} y los ángulos son A: {round(A,2)}, B: {round(B,2)}, C: {round(C,2)}')
    elif opcion == 3:
        break



        
