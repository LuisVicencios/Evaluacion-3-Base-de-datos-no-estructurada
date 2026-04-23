class SalmonModel:

    def __init__(self, collection):
        self.collection = collection

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



