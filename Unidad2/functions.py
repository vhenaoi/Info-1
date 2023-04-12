def input_numero(prompt):
    while True:   # Bucle infinito, se sale con break
        cadena = input(prompt)
        if cadena.isdigit():  # Salimos si es un número
            break
        # En caso contrario repetimos el bucle, con un mensaje de error
        else:
            print("Debe introducir un número")
    # Al salir del bucle retornamos el número, ya convertido a entero
    return int(cadena)

def no_contiene_numeros(prompt):
    while True:
        cadena = input(prompt)
        
        if cadena.isalpha():
            break
        else:
            print("Debe introducir solo letras")

def validar(valor,tipo):
    while True:
        try:
            if tipo == int:
                if valor.isdigit():
                    return tipo(valor)
                else:
                    print("Error, deben ingresar números")
                    valor = input("Ingrese el valor nuevamente: ")
            elif tipo == str:
                if valor.isalpha():
                    return tipo(valor)
                else:
                    print("Error, debe ingresar solo texto ")
                    valor = input("Ingrese el valor nuevamente: ")
            else:
                return tipo(valor)
        except:
            print("Error, no ingreso el valor solicitado tipo "+ str(tipo))
            valor = input("Ingrese el valor nuevamente: ")

def solicitar_data_comprador():
        nombre=input('Ingrese su nombre: ')
        nombre = validar(nombre,str)
        apellido=input('Ingrese su apellido: ')
        apellido = validar(apellido,str)
        id=input('Ingrese su documento de identificación: ')
        id = validar(id,int)
        telefono=input('Ingrese el número télefonico: ')
        telefono = validar(telefono,int)
        direccion=input('Ingrese la dirección: ')
        return nombre,apellido,id,telefono,direccion
            