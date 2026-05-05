class AdminView:
    def mostrar_menu(self):
        print("MENU ADMINISTRADOR")
        print("1. Actualizar stock de salmones")
        print("2. Actualizar precios (Compra/Venta)")
        print("3. Ver historial de ventas")
        print("4. Reporte: Relacion Coste-Ganancia")
        print("5. Reporte: Salmon mas vendido (5 ultimos.)")
        print("6. Cerrar sesion")
        return input("\nSeleccione una opción: ")

    def mostrar_mensaje(self, mensaje):
        print(f"\n[INFO] {mensaje}")

    def pedir_datos_actualizacion(self):
        print("ACTUALIZAR STOCK")
        print("1. Atlantico")
        print("2. Nordico")
        print("3. Pacifico")
        
        opciones = {"1": "Atlantico", "2": "Nordico", "3": "Pacifico"}
        seleccion = input("Seleccione el producto (1-3): ").strip()

        if seleccion not in opciones:
            print("[ERROR] Opcion no valida.")
            return None, 0

        tipo = opciones[seleccion]
        try:
            cantidad = float(input(f"Cantidad de kilos para {tipo} (use negativos para quitar): "))
            return tipo, cantidad
        except ValueError:
            print("[ERROR] Debe ingresar un numero valido.")
            return None, 0

    def pedir_datos_precios(self):
        print("ACTUALIZAR PRECIOS")
        print("1. Atlantico")
        print("2. Nordico")
        print("3. Pacifico")

        opciones = {"1": "Atlantico", "2": "Nordico", "3": "Pacifico"}
        seleccion = input("Seleccione el producto a modificar (1-3): ").strip()

        if seleccion not in opciones:
            print("[ERROR] Opcion no valida.")
            return None, 0, 0

        tipo = opciones[seleccion]
        try:
            compra = int(input(f"Nuevo precio de COSTE para {tipo}: $"))
            venta = int(input(f"Nuevo precio de VENTA para {tipo}: $"))
            return tipo, compra, venta
        except ValueError:
            print("[ERROR] Los precios deben ser valores numericos enteros.")
            return None, 0, 0
        
    def mostrar_reporte_coste_ganancia(self, datos_reporte):
        print(" REPORTE: COSTE Y GANANCIA")
        
        for d in datos_reporte:
            print(f"\nSalmon {d['tipo']}:")
            print(f"  Precio de coste: ${d['coste']}")
            print(f"  Precio de venta: ${d['venta']}")
            print(f"  Ganancia por kilo: ${d['ganancia']}")
            print(f"  Margen de utilidad: {round(d['margen'], 1)}%")
        
    
class VendedorView:
    def mostrar_menu(self):
        print("MENU VENDEDOR ")
        print("1. Realizar nueva venta")
        print("2. Cerrar sesion")
        return input("Seleccione una opcion: ")

    def ingresar_venta(self, salmones_disponibles):
        pedido = []
        opciones = {
            "1": "Atlantico",
            "2": "Nordico",
            "3": "Pacifico"
        }

        print("NUEVA VENTA ")
        print("Seleccione el producto:")
        print("1. Atlantico")
        print("2. Nordico")
        print("3. Pacifico")
        print("(Presione Enter sin marcar numero para finalizar el pedido)")

        while len(pedido) < 3:
            seleccion = input(f"\nSelección producto {len(pedido) + 1}: ").strip()

            if seleccion == "":
                break

            if seleccion not in opciones:
                self.mostrar_error("Opcion no valida. Ingrese 1, 2 o 3.")
                continue

            tipo_elegido = opciones[seleccion]

            if any(item["tipo"] == tipo_elegido for item in pedido):
                self.mostrar_error(f"El salmon {tipo_elegido} ya esta en la lista.")
                continue

            try:
                kilos = float(input(f"Cuantos kilos de {tipo_elegido}?: "))
                if kilos <= 0:
                    self.mostrar_error("La cantidad debe ser mayor a 0.")
                    continue
                
                pedido.append({"tipo": tipo_elegido, "kilos": kilos})
            except ValueError:
                self.mostrar_error("Debe ingresar un numero valido para los kilos.")

        return pedido

    def mostrar_error(self, mensaje):
        print(f"\n[ERROR] {mensaje}")

    def mostrar_exito(self, mensaje):
        print(f"\n[ÉXITO] {mensaje}")