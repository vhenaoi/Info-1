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

while True:
    x = input("Ingrese un número: ")
    x = validar(x,int)
    y = input("Ingrese una letra: ")
    y = validar(y,str)
    z = input("Ingrese una booleano: ")
    z = validar(y,bool)
