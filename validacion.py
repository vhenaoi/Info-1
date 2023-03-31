def validar(valor,tipo):
    while True:
        try:
            if tipo == int:
                valor = tipo(valor)
                return valor
            elif tipo == str:
                if valor.isalpha():
                    return valor
                else:
                    print("Error, no ingreso el valor solicitado tipo "+ str(tipo))
                    valor = input("Ingrese el valor nuevamente: ")
            else:
                return tipo(valor)
        except:
            print("Error, no ingreso el valor solicitado tipo "+ str(tipo))
            valor = input("Ingrese el valor nuevamente: ")

while True:
    x = input("Ingrese un número: ")
    x = validar(x,int)
    y = input("Ingrese una letra: ")
    y = validar(y,str)
    z = input("Ingrese una booleano: ")
    z = validar(y,bool)
