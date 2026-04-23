
from config.db_config import conector_bd
from model.usuarios import UsuarioModel


def main():
    db = conector_bd()

    if db is None:
        print(" Error: No se pudo conectar a la base de datos")
        return
    else:
        print(" Conexión exitosa a la base de datos MongoDB")


main()