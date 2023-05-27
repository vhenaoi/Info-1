

import pymongo

client = pymongo.MongoClient("mongodb+srv://veronicahenaoi:verohenao@cluster0.pfgit9k.mongodb.net/?retryWrites=true&w=majority")

mydb = client["Basededatos"]
mycol = mydb["micoleccion"]

mydict = { "nombre": "Luisa", "direccion": 5 }

x = mycol.insert_one(mydict)
#print(x.inserted_id)

#for x in mycol.find({  "direccion": 5 }):
#    print(f"El nombre es: {x['nombre']} y su dirección es: {x['direccion']}")

#myquery = { "nombre": "Veronica", "direccion": 5}
#newvalues = { "$set": { "marcota":"Bianca"} }

#myquery = { "nombre": "Veronica"}
#newvalues = { "$set": {"direccion": 1} }
#
#mycol.update_one(myquery, newvalues)

for x in mycol.find():
  print(x)