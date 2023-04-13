# Escriba un programa que le pida al usuario una palabra o frase y una letra. 
#El programa deberá imprimirla misma frase o palabra ingresada, pero ocultando la letra que ingresó el usuario con un asterisco.
# Nota: no se permite el uso de la función replace(), Solo instrucciones básicas.

# Datos de entrada
palabra=input('Ingrese una palabra o frase')
letra= input('Ingrese una letra')
cadena_vacia=''
cont=0
if cont<=len(letra):
    if palabra[cont]==letra:
        cadena_vacia+='*'
    else:
        cadena_vacia+=palabra[cont]
    cont+=1
print(cont)
print(cadena_vacia)