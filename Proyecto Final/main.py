from connector import BaseDeDatos
from entidades.Producto import Producto
from menu_principal import MenuVentas


def main():
    MenuVentas(db)

if __name__ == "__main__":
    db = BaseDeDatos("localhost", 3306, "root", "1422", "ventasonline")
    db.conectar()
    menu_ventas = MenuVentas(db)
    menu_ventas.mostrar_menu()
    