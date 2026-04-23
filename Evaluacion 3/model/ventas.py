from datetime import datetime

class VentaModel:

    def __init__(self, db):
        self.collection = db["ventas"]

    def registrar_venta(self, detalle, total):
        venta = {
            "fecha": datetime.now(),
            "detalle": detalle,
            "total": total
        }
        self.collection.insert_one(venta)

    def obtener_todas(self):
        return list(self.collection.find({}, {"_id": 0}))

    def ultimas_ventas(self, limite=5):
        return list(
            self.collection.find({}, {"_id": 0})
            .sort("fecha", -1)
            .limit(limite)
        )
