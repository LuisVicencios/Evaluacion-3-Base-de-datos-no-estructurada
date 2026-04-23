import pymongo as pm

def conector_bd():
    cliente = pm.MongoClient("localhost:27017")
    db = cliente["pythonMongo"]
    return db

def main():
    db = conector_bd()
    prueba01_coleccion = db["Prueba01"]

    # usuario = {
    #     "nombre": "Juanito",
    #     "apellido" : "Perez",
    #     "edad" : 30
    # }

    # resultado = prueba01_coleccion.insert_one (usuario)
    # print(resultado.inserted_id)

    # resultado = prueba01_coleccion.find()
    # print(resultado[0])
    # for documento in resultado:
    #     print(documento)

    # resultado = prueba01_coleccion.find_one()
    # print(resultado)

    resultado = prueba01_coleccion.update_one(
        {"nombre": "Juanito"},
        {"$set": { "email": "juanito@hola.com" }}
        )
    print (resultado.modified_count)
    

main()



