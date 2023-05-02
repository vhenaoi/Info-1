materiales = []
material = {}
while True:
   m = input("La prueba de hemocompatibilidad fue aprobada? [Sí/No]: ")
   if m == "Sí":
    material["prueba_hemocompatibilidad"]="Sí"
    break
   elif m == "No":
    material["prueba_hemocompatibilidad"]="No"
    break
   else:
     print("ERROR, vuelva a ingresar los datos")
materiales.append(material)
print(materiales)