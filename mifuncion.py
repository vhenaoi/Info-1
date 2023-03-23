import numpy as np
import math 

def saludo():
    print('Hola')

def factorial(n):
    fact = 1
    for y in range(1, n + 1):
        fact *= y
    return fact

def seno(x):
    sum = 0
    for k in range(100):
        func = ((-1)**k)*(x**(2*k+1))/(factorial(2*k+1))
        sum += func
    return sum

def coseno(x):
    sum = 0
    for k in range(100):
        func = ((-1)**k)*(x**(2*k))/(factorial(2*k))
        sum += func
    return sum
