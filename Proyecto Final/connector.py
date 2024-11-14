import mysql.connector

class BaseDeDatos:
    def __init__(self, host,port, user, password, database):
        self.config = {
            "host": host,
            "port": port,
            "user": user,
            "password": password,
            "database": database
        }
        self.conexion = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(**self.config)
            self.cursor = self.conexion.cursor()
            print("Conectado a la base de datos")
        except mysql.connector.Error as error:
            print(f"Error al conectar a la base de datos: {error}")

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
    
    def ejecutar(self, query, valores=None):
        self.cursor.execute(query, valores or ())
        self.conexion.commit()

    def obtener_datos(self, query, valores=None):
        self.cursor.execute(query, valores or ())
        return self.cursor.fetchall()


