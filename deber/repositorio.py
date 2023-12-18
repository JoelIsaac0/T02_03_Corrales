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

    