import os 
archivos=os.listdir(r'D:\Info-1\Unidad3\17. manejo de archivos')
archivos_txt=[]
for i in archivos:
    # if '.txt' in i:
    #     archivos_txt.append(i)
    # if i[-4:]=='.txt':
    #     archivos_txt.append(i)
    try:
        file=open(i)
        contenido=file.read()
        print(contenido)
    except:
        print('No puedo abrir el archivo {i}'.format(i=i))

print(archivos_txt)
