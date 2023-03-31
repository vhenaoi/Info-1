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
            