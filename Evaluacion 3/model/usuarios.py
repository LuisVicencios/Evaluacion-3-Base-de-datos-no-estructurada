class UsuarioModel:

    def __init__(self, db):
        self.collection = db["usuarios"]

    def autenticar(self, username, password):
        """
        Retorna el usuario si existe, si no None
        """
        return self.collection.find_one({
            "username": username,
            "password": password
        }, {"_id": 0})
