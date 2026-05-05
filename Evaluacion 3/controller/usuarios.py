import getpass

class VendedorController:
    def __init__(self, salmon_model, venta_model, vendedor_view):
        self.salmon_model = salmon_model
        self.venta_model = venta_model
        self.view = vendedor_view

    def iniciar(self):
        while True:
            opcion = self.view.mostrar_menu()

            if opcion == "1":
                self.realizar_venta()
            elif opcion == "2":
                self.view.mostrar_exito("Cerrando sesion de vendedor")
                break
            else:
                self.view.mostrar_error("Opcion no valida. Intente nuevamente.")

    def realizar_venta(self):
        salmones = self.salmon_model.obtener_todos()
        pedido = self.view.ingresar_venta(salmones)

        if not pedido:
            self.view.mostrar_error("Venta cancelada o vacia")
            return

        total = 0
        
        for item in pedido:
            salmon = next(s for s in salmones if s["tipo"] == item["tipo"])
            if item["kilos"] > salmon["stock"]:
                self.view.mostrar_error(f"Stock insuficiente para {item['tipo']}. Quedan {salmon['stock']} kg.")
                return 

        for item in pedido:
            salmon = next(s for s in salmones if s["tipo"] == item["tipo"])
            total += item["kilos"] * salmon["precio_venta"]
            self.salmon_model.actualizar_stock(item["tipo"], -item["kilos"])

        self.venta_model.registrar_venta(pedido, total)
        
        self.view.mostrar_exito(f"Venta registrada correctamente. Total a cobrar: ${total}")

class AdminController:
    def __init__(self, salmon_model, venta_model, admin_view):
        self.salmon_model = salmon_model
        self.venta_model = venta_model
        self.view = admin_view

    def iniciar(self):
        while True:
            opcion = self.view.mostrar_menu()

            if opcion == "1":
                self.actualizar_stock()
            elif opcion == "2":
                self.actualizar_precios()
            elif opcion == "3":
                self.ver_historial()
            elif opcion == "4":
                self.reporte_coste_ganancia()
            elif opcion == "5":
                self.reporte_mas_vendido()
            elif opcion == "6":
                self.view.mostrar_mensaje("Cerrando sesion de administrador")
                break
            else:
                self.view.mostrar_mensaje("Opcion no valida.")

    def actualizar_stock(self):
        tipo, cantidad = self.view.pedir_datos_actualizacion()
        if tipo.capitalize() in ["Atlantico", "Nordico", "Pacifico"]:
            self.salmon_model.actualizar_stock(tipo.capitalize(), cantidad)
            self.view.mostrar_mensaje(f"Stock de {tipo.capitalize()} actualizado correctamente.")
        else:
            self.view.mostrar_mensaje("Error: Tipo de salmon no valido.")

    def actualizar_precios(self):
        tipo, compra, venta = self.view.pedir_datos_precios()
        if tipo.capitalize() in ["Atlantico", "Nordico", "Pacifico"]:
            self.salmon_model.actualizar_precios(tipo.capitalize(), compra, venta)
            self.view.mostrar_mensaje(f"Precios de {tipo.capitalize()} actualizados correctamente.")
        else:
            self.view.mostrar_mensaje("Error: Tipo de salmon no valido.")

    def ver_historial(self):
        ventas = self.venta_model.obtener_todas()
        if not ventas:
            self.view.mostrar_mensaje("No hay ventas registradas.")
            return
            
        print("HISTORIAL DE VENTAS")
        for v in ventas:
            print(f"Fecha: {v['fecha'].strftime('%Y-%m-%d %H:%M:%S')} | Total: ${v['total']}")
            for item in v['detalle']:
                print(f"   - {item['kilos']} kg de {item['tipo']}")

    def reporte_coste_ganancia(self):
        salmones = self.salmon_model.obtener_todos()
        datos_reporte = []

        for s in salmones:
            coste = s['precio_compra']
            venta = s['precio_venta']
            ganancia = venta - coste
            margen = (ganancia / venta) * 100 if venta > 0 else 0 

            datos_reporte.append({
                "tipo": s["tipo"],
                "coste": coste,
                "venta": venta,
                "ganancia": ganancia,
                "margen": margen
            })
        self.view.mostrar_reporte_coste_ganancia(datos_reporte)

    def reporte_mas_vendido(self):
        ultimas = self.venta_model.ultimas_ventas(5)
        
        if not ultimas:
            self.view.mostrar_mensaje("No hay suficientes ventas para generar el reporte.")
            return

        conteo_kilos = {"Atlantico": 0, "Nordico": 0, "Pacifico": 0}

        for venta in ultimas:
            for item in venta["detalle"]:
                conteo_kilos[item["tipo"]] += item["kilos"]

        salmon_top = max(conteo_kilos, key=conteo_kilos.get)
        kilos_top = conteo_kilos[salmon_top]

        print("REPORTE: SALMON MAS VENDIDO")
        if kilos_top == 0:
             print("Las ultimas 5 ventas estan vacias o con 0 kilos.")
        else:
             print(f"El salmon más vendido es el {salmon_top} con un total de {kilos_top} kilos.")


class AutenticadorController:
    def __init__(self, usuario_model):
        self.usuario_model = usuario_model

    def iniciar_sesion(self):
        while True:
            print("Bienvenido a Acme Smoked Fish")

            username = input("Usuario: ")
            password = getpass.getpass("Contraseña: ") 
            usuario = self.usuario_model.autenticar(username, password)

            if usuario:
                return usuario 
            else:
                print("\n[ERROR] Credenciales inválidas.")
                opcion = input("¿Desea reintentar? (S/N): ").upper()
                if opcion == 'N':
                    print("Saliendo del sistema")
                    return None