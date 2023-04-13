# vocales='aeiou'
# sep_vocales=','.join(list(vocales)) # Utilizar una lista, y los separa-> string
# print(sep_vocales,type(sep_vocales))

# print(sep_vocales.split(','))# utiliza una string y los separa -> list


#Ejemplo diccionarios

# estudiantes={'name':{'elementos':[[8,['carlos','manuela']],'7']},'edad':[18,18,18]}
# print(estudiantes['name']['elementos'])

# pares={int:'True'}
# print(pares.get(int))

# numeros=[1,2,3,4]
# print(dict('num',numeros))

fruits = ["Apple", "Pear", "Peach", "Banana"]
numeros=[1,2,3,4]
data={}
for i,f in enumerate(fruits):
    print(i,f)
    data[f]=numeros[i]
#fruit_dictionary = { f : numeros[i] for i,f in enumerate(fruits) }
print(data)