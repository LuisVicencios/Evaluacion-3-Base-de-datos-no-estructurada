import pymongo as pm

def conector_bd():
    cliente = pm.MongoClient('localhost:27017')
    db = cliente["pythonMongo"]
    return db

def main():
    db = conector_bd()
    test1_coleccion = db['test1']

    # usuario = {
    #     "nombre": "Juanito",
    #     "apellido": "Perez",
    #     "edad": 30
    # }

    # resultado = test1_coleccion.insert_one(usuario)
    # print(resultado.inserted_id)

    # resultado = test1_coleccion.find()
    # print(resultado[0])
    
    # for r in resultado:
    #     print(r)

    # resultado = test1_coleccion.find_one()
    # print(resultado)
    
    resultado = test1_coleccion.update_one(
        { "nombre": "Juanito" },
        { "$set": { "email": "juanito@holaaaaaaa.com" } }
    )

    print(resultado.modified_count)

main()