class UsuarioModel:

    def __init__(self, db):
        self.collection = db["usuarios"]

    def crear_usuarios_iniciales(self):
        if self.collection.count_documents({}) == 0:
            usuarios_base = [
                {"username": "admin", "password": "admin", "rol": "administrador"},
                {"username": "vendedor", "password": "vendedor", "rol": "vendedor"}
            ]
            self.collection.insert_many(usuarios_base)

    def autenticar(self, username, password):
        return self.collection.find_one({
            "username": username,
            "password": password
        }, {"_id": 0})
