import bcrypt

class UsuarioModel:

    def __init__(self, db):
        self.collection = db["usuarios"]

    def crear_usuarios_iniciales(self):
        if self.collection.count_documents({}) == 0:
            admin = bcrypt.hashpw("admin".encode('utf-8'), bcrypt.gensalt())
            vendedor = bcrypt.hashpw("vendedor".encode('utf-8'), bcrypt.gensalt())
            
            usuarios_base = [
                {"username": "admin", "password": admin, "rol": "administrador"},
                {"username": "vendedor", "password": vendedor, "rol": "vendedor"}
            ]
            self.collection.insert_many(usuarios_base)
    def autenticar(self, username, password):
        usuario = self.collection.find_one({"username": username})
        
        if usuario:
            clave_hasheada = usuario["password"]
            if type(clave_hasheada) == str:
                clave_hasheada = clave_hasheada.encode('utf-8')
            
            if bcrypt.checkpw(password.encode('utf-8'), clave_hasheada):
                return usuario
                
        return None
