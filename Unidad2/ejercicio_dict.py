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
from functions import solicitar_data_comprador, validar

total = 0
comprador=[]
articulos=[]
cont_comp=0
while True:
    if cont_comp==3:
        ordenados = sorted(articulos, key=lambda art: art[1])
        print("Estos son los articulos que esta apunto de comprar")
        print(str(ordenados[0])+"\n"+str(ordenados[1])+"\n"+str(ordenados[2]))
        for art in range(len(ordenados)):
            total += ordenados[art][-1]
        print("El total de la compra es de:" +str(total))
        menu=input('1. Salir 2. Ingresar compra: ')
        menu = validar(menu,int)
        if menu==1:
            break
        if menu==2:
            cont_comp-=1
            pass
    nombre,apellido,id,telefono,direccion = solicitar_data_comprador()
    comprador=[nombre,apellido,id,direccion,telefono]
    
    while cont_comp<=2:
        try:
            articulo=input('Seleccione el articulo a comprar\n1.Resonador\n2.Angiografía\n3.Radiografía\n-')
            articulo = validar(articulo,int)
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
                        3:['Artis', 'Q', 2800],
                        4: ['Artis', 'icono', 1500]
                    }
                elif articulo==3:
                    articulo_dict={
                        1:['YSIO', 'FAST', 1300],
                        2: ['MULTIX', 'myExam', 1220],
                        3:['Multix', 'Select', 2050]
                    }
                

                print('Seleccione las caracteristicas del producto')
                for k,v in articulo_dict.items():
                    print('Llave',k,'Valor',v)
                opcion=input('Indique su selección ')
                opcion = validar(opcion,int)
                if opcion in articulo_dict.keys():
                    articulos.append(articulo_dict[opcion])
                    print("El comprador "+str(comprador[0])+" "+str(comprador[1])+" con CC: "+str(comprador[2])+" acaba de agregar al carrito el producto "+str(articulo_dict[opcion][0])+" "+str(articulo_dict[opcion][1]))
                    cont_comp+=1  

        except: 
            print('ingrese valor valido')
            continue
    
    