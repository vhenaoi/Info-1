

import pymongo

client = pymongo.MongoClient("mongodb+srv://veronicahenaoi:veronica1215@c1.pcpqmmq.mongodb.net/?retryWrites=true&w=majority")

mydb = client["infodata"]
mycol = mydb["coldata"]

#mydict = { "nombre": "Veronica", "direccion": 5 }
#
#x = mycol.insert_one(mydict)
#print(x.inserted_id)

#for x in mycol.find({  "direccion": 1 }):
#    print(x['nombre'],x['direccion'])

#myquery = { "nombre": "Veronica", "direccion": 5}
#newvalues = { "$set": { "marcota":"Bianca"} }
#
#mycol.update_one(myquery, newvalues)

for x in mycol.find():
  print(x)