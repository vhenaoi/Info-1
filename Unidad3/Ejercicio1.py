while True:
    print('Menú:\n1. Ingresar información de paciente\n2. Ver información en archivo\n3. Salir')
    opcion = int(input('Seleccione una opcion: '))
    contador = 0
    if opcion == 1:
        contador += 1
        nombre=input('Ingrese el nombre: ')
        apellido = input('Ingrese el apellido: ')
        edad = input('Ingrese la edad: ')
        arch = open("Ejercicio1.txt","a")
        arch.write(str(contador)+'|'+nombre+'|'+apellido+'|'+edad+'|'+'\n')
        arch.close()
    if opcion == 2:
        arch = open("Ejercicio1.txt","r")
        print(arch.read())
    if opcion == 3:
        break

