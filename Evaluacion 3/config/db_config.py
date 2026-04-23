import pymongo as pm

def conector_bd():
    cliente = pm.MongoClient("localhost:27017")
    db = cliente["pythonMongo"]
    return db

def main():
    db = conector_bd()

main()