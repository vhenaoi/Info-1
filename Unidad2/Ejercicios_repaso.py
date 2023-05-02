'''1. Cree una función que pida un número por teclado 
y que cree un diccionario cuyas claves sean desde el 
número 1 hasta el número indicado, y los valores sean
los cuadrados de las claves.'''

def cuadrado():
    #numero = int(input('Ingrese un número: '))
    numero = 1
    diccionario = {}
    for i in range(1,numero+1):
        diccionario[i]=i**2
    return diccionario

dir = cuadrado()
print(dir)

'''
2. Cree una función de Python para ordenar 
(ascendente y descendente) un diccionario 
por valor no por clave.
'''
def ordenar(diccionario):
    print('Ordenar')
    dir_asc=sorted(diccionario.values())
    dir_des=list(reversed(sorted(diccionario.values())))
    return dir_asc, dir_des

dir = {'a':25,'c':1,'z':90,'x':12}

asc,des=ordenar(dir)
print('Ascendente: ',asc,' Descendente: ',des)

'''
3. Combinar dos diccionarios agregando valores para claves comunes.
'''
d1 = {'a': 10, 'b': 20, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':40}

d1.update(d2)
print(d1)

'''
4. Escriba un programa Python para convertir una lista en un diccionario.
'''
def listtodir(l):
    return dict(l)

l = [('clave1',1),('clave2',2)]
diccionario1=listtodir(l)
print(diccionario1)

'''
5.  Cree una función que permita cambiar un diccionario por una lista:
Ejemplo: 
Diccionario: {'Ciencia': [88, 89, 62, 95], 'Idioma': [77, 78, 84, 80]} 
Lista:  [{ 'Ciencia': 88, 'Idioma': 77}, {'Ciencia': 89, 'Idioma': 78}, 
{'Ciencia': 62, 'Idioma': 84}, {'Ciencia': 95, 'Idioma ': 80}]
'''
Diccionario = {'Ciencia': [88, 89, 62, 95], 'Idioma': [77, 78, 84, 80]} 

def dirtolist(Diccionario):
    vacia = []
    d={}
    clave = list(Diccionario.keys())
    valor = list(Diccionario.values())
    for c in clave:
        for v in valor:
            d[clave[c]] = valor[0][v]
    vacia.append(d)

    
    return vacia

lista = dirtolist(Diccionario)
print(lista)

