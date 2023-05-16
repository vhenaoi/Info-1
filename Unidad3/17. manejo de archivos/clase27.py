arch= open('archivo.txt','r')

caracter= arch.read(1)
contador=0
while caracter !='':
    contador +=1
    caracter=arch.read(1)

arch.close()