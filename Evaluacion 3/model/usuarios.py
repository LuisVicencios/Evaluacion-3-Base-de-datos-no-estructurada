import bcrypt

class UsuarioModel:

    def __init__(self, db):
        self.collection = db["usuarios"]

    def crear_usuarios_iniciales(self):
        if self.collection.count_documents({}) == 0:
            pass_admin = bcrypt.hashpw("123".encode('utf-8'), bcrypt.gensalt())
            pass_vendedor = bcrypt.hashpw("456".encode('utf-8'), bcrypt.gensalt())
            usuarios_base = [
                {"username": "admin", "password": "admin", "rol": "administrador"},
                {"username": "vendedor", "password": "vendedor", "rol": "vendedor"}
            ]
            self.collection.insert_many(usuarios_base)

    def autenticar(self, username, password):
        usuario = self.collection.find_one({"username": username})
        
        if usuario:
            if bcrypt.checkpw(password.encode('utf-8'), usuario["password"]):
                return usuario
        return None
