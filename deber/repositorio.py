import psycopg2
from modelo import Usuario, CuentaAhorros
import random

class Repositorio:
    def __init__(self):
        self.conexion = psycopg2.connect(
            database="usuario",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
        self.cursor = self.conexion.cursor()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()

    def agregar_usuario(self, nombre, apellido, correo, cedula, celular):
        insertar_usuario_query = """
        INSERT INTO usuarios (nombre, apellido, correo, cedula, celular)
        VALUES (%s, %s, %s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insertar_usuario_query, (nombre, apellido, correo, cedula, celular))
        usuario_id = self.cursor.fetchone()[0]
        self.conexion.commit()
        return usuario_id