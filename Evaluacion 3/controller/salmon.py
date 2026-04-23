class VendedorController:

    def __init__(self, salmon_model, venta_model, view):
        self.salmon_model = salmon_model
        self.venta_model = venta_model
        self.view = view

    def realizar_venta(self):
        salmones = self.salmon_model.obtener_todos()
        pedido = self.view.ingresar_venta(salmones)

        total = 0
        for item in pedido:
            salmon = next(s for s in salmones if s["tipo"] == item["tipo"])

            if item["kilos"] > salmon["stock"]:
                print("Stock insuficiente")
                return

            total += item["kilos"] * salmon["precio_venta"]
            self.salmon_model.actualizar_stock(item["tipo"], -item["kilos"])

        self.venta_model.registrar_venta(pedido, total)
        print(f"Venta realizada. Total: ${total}")
