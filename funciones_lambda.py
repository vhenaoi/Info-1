#Parte practica Parcial 
#Carlos Solano

general =[]

num1paciente = 0
num2paciente = 0



while True:
    print("Instituto Nacional de Cancerología\n")

    menu=input("Por favor ingrese una opción:\n  1. Ingresar un paciente\n  2. Salir\n Ingrese una opcion: ")

    while num2paciente <= 2:

        if menu == "1":
            print("\nHa ingresado (1): Ingresar un paciente")
            print("\nPor favor ingrese la información que se le va a solicitar a continuación: ")

            nombre =input("Por favor ingrese su nombre completo: ")
            id = int(input("Por favor ingrese su documento id: "))
            idpaciente = input("Por favor ingrese identificador del paciente: ")
            edad =int(input("Por favor ingrese su edad: "))
            peso = int(input("Por favor ingrese su peso: "))
            fecha = input("Por favor ingrese la fecha(DD/MM/AAAA): ")
            protector = input("\nUsted utiliza protector solar:\n 1-Siempre\n 2-Con poca frecuencia\n 3-Nunca\n Escoga una opcion: ")
            
            if protector == "1":
                protector = "Siempre"
            elif protector == "2":
                protector = "Con poca frecuencia"
            elif protector == "3":
                protector = "Nunca"

            cancer = input("\n¿Su nucleo familiar ha desarrollado cancer de piel?\n 1-Si\n 2-No\n Escoga una opcion: ")

            if cancer == "1":
                cancer = "Si"
            elif cancer == "2":
                cancer = "No"
            
            coloracion = input("¿Ha presentado cambios de coloracion en la piel?\n 1-Si\n 2-No\n Escoga una opcion: ")


            if coloracion == "1":
                coloracion = "Si"
            elif coloracion == "2":
                coloracion = "No"

            lunares = input("¿Ha tenido lunares que han cambiado con el tiempo?\n 1-Si\n 2-No\n Escoga una opcion: ")

        

            if lunares == "1":
                lunares = "Si"
            elif lunares == "2":
                lunares = "No"

            pielaño = input("¿Ha tenido cambios en la piel durante el ultimo año?\n 1-Si\n 2-No\n Escoga una opcion: ")

    

            if pielaño == "1":
                pielaño = "Si"
            elif pielaño == "2":
                pielaño = "No"

            heridas = input("¿Ha presentado heridas que son recurrentes no cicatrizantes que sangren con facilidad?\n 1-Si\n 2-No\n Escoga una opcion: ")



            if heridas == "1":
                heridas = "Si"
            elif heridas == "2":
                heridas = "No"


            idpacientee = "Sub-"+"%04d" % (int(idpaciente))

            paciente = [nombre,id,idpacientee,edad,peso,fecha,protector,cancer,coloracion,lunares,pielaño,heridas]
            general.append(paciente)

            num2paciente+=1
        
                

        elif menu == "2":
            print("\nHa ingresado (2): Salir")
            print(general)
            print("Muchas gracias por su consulta, vuelva pronto!!!") 
            break

        if num2paciente == 2:
            print("Ya ha ingresado 2 pacientes")
            print("Desea seguir ingresar mas:")
            print("\n1 - SI"),print("\n2 - No\n")
            ingrepaciente = input("Escoga una opcion: ")
            
            if ingrepaciente == "1":
                num1paciente = 1
                continue

            if ingrepaciente == "2":
                print("Estos fueron los pacientes registrados:")
                print(general)
                print("Muchas gracias, un gusto atenderte!")
                
                break 
            
        if num1paciente == 1:
            print("Ya ha ingresado otro paciente")
            print("Desea seguir ingresar mas:")
            print("\n1 - SI"),print("\n2 - No\n")
            ingrepaciente = input("Escoga una opcion: ")

            if ingrepaciente == "1":
                num1paciente = 1
                continue

            if ingrepaciente == "2":
                print("Estos fueron los registrados registrados:")
                print(general)
                print("Muchas gracias, un gusto atenderte!")
                break       
    break
