from entidades.Producto import Producto
from entidades.Ordenes import Ordenes
from entidades.Clientes import Cliente
from connector import BaseDeDatos
from clearConsola import clear

class MenuVentas:
    def __init__(self, db: BaseDeDatos) -> None:
        self.db = db
    def mostrar_menu(self):
        while True:
            print("\n")
            print("-------------------- Menu ventas online --------------------")
            print("                   Seleccione una opcion:               ")
            print("                     1. Menu clientes")
            print("                     2. Menu productos")
            print("                     3. Menu ordenes")
            print("                     0. Salir")
            print("\n")
            opcion = input("Opción: ")
            print("\n")
            clear()
            if opcion == '1':
                self.menu_clientes()
            elif opcion == '2':
                self.menu_productos()
            elif opcion == '3':
                self.menu_ordenes()
            elif opcion == '0':
                print("Saliendo del sistema...")
                break
            else:
                clear()
                print("Opción inválida. Intente de nuevo.")

    def menu_clientes(self):
        cliente_db = Cliente(self.db)
        while True:
            print("\n")
            print("-------------------- Menu Clientes --------------------")
            print("                Seleccione una opcion:                  ")
            print("\n")
            print("                 1. Ver clientes")
            print("                 2. Agregar cliente")
            print("                 3. Editar cliente")
            print("                 4. Eliminar cliente")
            print("                 5. Buscar cliente por ID")
            print("                 0. Volver al menu principal")
            print("\n")
            opcion = input("Opción: ")
            print("\n")
            clear()
            if opcion == '1':
                cliente_db.ver_clientes()

            elif opcion == '2':
                try:
                    cliente_db.registrar_cliente()

                except Exception as e:
                    print("Error al agregar el cliente:", e)
                
            elif opcion == '3':
                try:
                    cliente_db.ver_clientes()
                    print("----------------------------------")
                    id_cliente = int(input("Id del cliente a editar: "))
                    if not isinstance(id_cliente, int) or id_cliente < 1:
                        raise ValueError("El id debe ser un número positivo")
                
                    cliente_db.editar_cliente(id_cliente)

                except Exception as e:
                    print("Error al editar el cliente:", e)

            elif opcion == '4':
                try:
                    cliente_db.ver_clientes()
                    id_cliente = int(input("Id del cliente a eliminar: "))
                    if not isinstance(id_cliente, int) or id_cliente < 1:
                        raise ValueError("El id debe ser un número positivo")
                    
                    cliente_db.eliminar_cliente(id_cliente)

                except Exception as e:
                    print("Error al eliminar el cliente:", e)

            elif opcion == '5':
                try:
                    id_cliente = int(input("Id del cliente a buscar: "))
                    if not isinstance(id_cliente, int) or id_cliente < 1:
                        raise ValueError("El id debe ser un número positivo")
                
                    cliente_db.buscar_cliente_por_id(id_cliente)

                except Exception as e:
                    print("Error al buscar el cliente:", e)

            elif opcion == '0':
                print("Volviendo al menu principal...")
                break

            else:
                print("Opción inválida. Intente de nuevo.")
                    

    def menu_productos(self):
         producto_db = Producto(self.db)

         while True:
            print("\n")
            print("-------------------- Menu Productos --------------------")
            print("                Seleccione una opcion:                  ")
            print("\n")
            print("                 1. Ver productos")
            print("                 2. Agregar producto")
            print("                 3. Editar producto")
            print("                 4. Eliminar producto")
            print("                 5. Ver producto por nombre")
            print("                 6. Ver categorias")
            print("                 0. Volver al menu principal")
            print("\n")
            opcion = input("Opción: ")
            print("\n")
            clear()
            if opcion == '1':
                producto_db.ver_productos()

            elif opcion == '2':
                try:
                    producto_db.registrar_producto()

                except Exception as e:
                    print("Error al agregar el producto:", e)

            elif opcion == '3':
                try:
                    producto_db.ver_productos()
                    id_producto = int(input("Id del producto a editar: "))
                    if not isinstance(id_producto, int):
                        raise ValueError("El id debe ser un numero")
                    
                    producto_db.editar_producto(id_producto)

                except Exception as e:
                    print("Error al editar el producto:", e)

            elif opcion == '4':
                try:
                    producto_db.ver_productos()
                    id_producto = int(input("Id del producto a eliminar: "))
                    if not isinstance(id_producto, int) or id_producto < 1:
                        raise ValueError("El id debe ser un número positivo")
                    
                    producto_db.eliminar_producto(id_producto)

                except Exception as e:
                    print("Error al eliminar el producto:", e)
                
            elif opcion == '5':
                try:
                    nombre_producto = input("Nombre del producto a buscar: ")
                    if not isinstance(nombre_producto, str) or nombre_producto.isspace() or nombre_producto == "":
                        raise ValueError("Ingrese un nombre válido")
                    
                    producto_db.buscar_producto_por_nombre(nombre_producto)
                except Exception as e:
                    print("Error al buscar el producto:", e)

            elif opcion == '6':
                try:
                    producto_db.ver_categorias()
                except Exception as e:
                    print("Error al ver las categorías:", e)

            elif opcion == '0':
                print("Volviendo al menu principal...")
                break

            else:
                print("Opción inválida. Intente de nuevo.")

    def menu_ordenes(self):
        ordenes_db = Ordenes(self.db)

        while True:
            print("\n")
            print("-------------------- Menu Ordenes --------------------")
            print("                Seleccione una opcion:                  ")
            print("\n")
            print("                 1. Ver todas las ordenes")
            print("                 2. Agregar orden")
            print("                 3. Ver ordenes por id_cliente ")
            print("                 4. Productos más vendidos")
            print("                 0. Volver al menu principal")
            print("\n")
            opcion = input("Opción: ")
            print("\n")
            clear()
            if opcion == '1':
                ordenes_db.ver_ordenes_totales()
            elif opcion == '2':
                try:
                    ordenes_db.registrar_orden()
                except Exception as e:
                    print("Error al agregar la orden:", e)
            elif opcion == '3':
                id_cliente = int(input("Ingrese id del cliente: "))
                if not isinstance(id_cliente, int):
                    raise ValueError("El id debe ser un número")
                ordenes_db.ver_ordenes_por_cliente(id_cliente)
            elif opcion == '4':
                try:
                    ordenes_db.buscar_productos_mas_vendidos()
                except Exception as e:
                    print("Error al ver los productos más vendidos:", e)
            elif opcion == '0':
                print("Volviendo al menu principal...")
                break