'''
Diseñe un script en Python que permita capturar 
los datos de un comprador y facture el total de la compra, 
la información del comprador y su compra serán almacenarlos en una lista,
la información a ingresar será:

Nombre y apellido
Número de identificación
Dirección
Teléfono
'''
from functions import input_numero
from functions import no_contiene_numeros

comprador=[]
cont_comp=0
while cont_comp<=3:
    nombre=no_contiene_numeros('Ingrese su nombre')
    apellido=no_contiene_numeros('Ingrese su apellido: ')
    id=input_numero('Ingrese su documento de identificación: ')
    telefono=input_numero('Ingrese el número télefonico: ')
    direccion=input('Ingrese la dirección :')
    comprador=[nombre,apellido,id,direccion,telefono]
    articulo=input_numero('Seleccione el articulo a comprar\n1.Resonador\n2.Angiografía\n3.Radiografía')

    if articulo== 1 or articulo==2 or articulo==3:
        if articulo==1:
            articulo_dict={
                1: ['MAGNETOM', 'Sola', 1.5, 1000],
                2: ['MAGNETOM', 'Altea', 1.5, 1200],
                3: ['MAGNETOM', 'Amira', 1.5, 1300],
                4: ['MAGNETOM', 'Sempra', 1.5, 2000]
                }
        elif articulo ==2:
            articulo_dict={
                1: ['Artis', 'zee', 1000],
                2:['Artis', 'one', 1100],
                3:['Artis', 'Q'],
                4: ['Artis', 'icono', 1500]
            }
        elif articulo==3:
            articulo_dict={
                1:['YSIO', 'FAST', 1300],
                2: ['MULTIX', 'myExam', 1220],
                3:['Multix', 'Select', 2050]
            }
    else: 
        print('ingrese una opcion existente')
        continue

    print('Seleccione las caracteristicas del producto')
    for k,v in articulo_dict.items():
        print('Llave',k,'Valor',v)
    opcion=int(input('Indique su selección '))
    if opcion in articulo_dict.keys():
        comprador.append(resonador[opcion])
