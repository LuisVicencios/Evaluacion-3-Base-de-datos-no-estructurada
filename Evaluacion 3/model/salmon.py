class SalmonModel:

    def __init__(self, db):
        self.collection = db["salmones"]

    def inicializar_inventario(self):
        if self.collection.count_documents({}) == 0:
            salmones_iniciales = [
                {"tipo": "Atlantico", "precio_compra": 8000, "precio_venta": 12000, "stock": 10},
                {"tipo": "Nordico", "precio_compra": 10000, "precio_venta": 15000, "stock": 10},
                {"tipo": "Pacifico", "precio_compra": 5000, "precio_venta": 7000, "stock": 10}
            ]
            self.collection.insert_many(salmones_iniciales)

    def obtener_todos(self):
        return list(self.collection.find({}, {"_id": 0}))

    def actualizar_stock(self, tipo, cantidad):
        self.collection.update_one(
            {"tipo": tipo},
            {"$inc": {"stock": cantidad}}
        )

    def actualizar_precios(self, tipo, compra, venta):
        self.collection.update_one(
            {"tipo": tipo},
            {"$set": {
                "precio_compra": compra,
                "precio_venta": venta
            }}
        )



