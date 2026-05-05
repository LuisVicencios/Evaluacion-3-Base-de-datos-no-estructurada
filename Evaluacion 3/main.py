from config.db_config import ConexionDB
from model.salmon import SalmonModel
from model.usuarios import UsuarioModel
from model.ventas import VentaModel
from view.Usuarios import AdminView, VendedorView 
from controller.Usuarios import VendedorController, AdminController, AutenticadorController

def main():
    conexion = ConexionDB()
    db = conexion.conector_db()

    if db is None:
        print("[ERROR] No se pudo conectar a MongoDB. Verifica el servicio.")
        return


    usuario_model = UsuarioModel(db)
    salmon_model = SalmonModel(db)
    venta_model = VentaModel(db)

    usuario_model.crear_usuarios_iniciales()
    salmon_model.inicializar_inventario() 

    salmon_model.inicializar_inventario()

    admin_view = AdminView() 
    vendedor_view = VendedorView()

    autenticador_ctrl = AutenticadorController(usuario_model)
    usuario_logueado = autenticador_ctrl.iniciar_sesion()

    if usuario_logueado:
        rol = usuario_logueado.get("rol", "").lower()
        print(f"\n--- Bienvenido {usuario_logueado['username']} (Rol: {rol}) ---")

        if rol == "administrador":
            ctrl_admin = AdminController(salmon_model, venta_model, admin_view)
            ctrl_admin.iniciar()
        
        elif rol == "vendedor":
            ctrl_vendedor = VendedorController(salmon_model, venta_model, vendedor_view)
            ctrl_vendedor.iniciar()
        
        else:
            print("Error: El usuario no tiene un rol valido asignado.")

if __name__ == "__main__":
    main()