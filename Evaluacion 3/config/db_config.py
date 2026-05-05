import pymongo as pm

class ConexionDB:
    def __init__(self):
        self.host = "localhost:27017"
        self.nombre_bd = "pythonMongo" 

    def conector_db(self):
        try:
            cliente = pm.MongoClient(self.host, serverSelectionTimeoutMS=2000)
            db = cliente[self.nombre_bd]
            
            cliente.server_info() 
            
            return db
            
        except pm.errors.ServerSelectionTimeoutError:
            return None