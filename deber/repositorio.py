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

    def crear_cuenta_ahorros(self, usuario_id, saldo_inicial=0):
        numero_cuenta = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        insertar_cuenta_query = """
        INSERT INTO cuentas_ahorros (usuario_id, numero_cuenta, saldo)
        VALUES (%s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insertar_cuenta_query, (usuario_id, numero_cuenta, saldo_inicial))
        cuenta_id = self.cursor.fetchone()[0]
        self.conexion.commit()
        return cuenta_id

    def depositar_en_cuenta(self, numero_cuenta_destino, monto):
        verificar_cuenta_query = "SELECT id FROM cuentas_ahorros WHERE numero_cuenta = %s;"
        self.cursor.execute(verificar_cuenta_query, (numero_cuenta_destino,))
        cuenta_existente = self.cursor.fetchone()

        if cuenta_existente:
            depositar_query = """
            UPDATE cuentas_ahorros
            SET saldo = saldo + %s
            WHERE numero_cuenta = %s;
            """
            self.cursor.execute(depositar_query, (monto, numero_cuenta_destino))
            self.conexion.commit()
            print(f"Depósito de {monto} realizado en la cuenta {numero_cuenta_destino}")
        else:
            print(f"No existe una cuenta con el número {numero_cuenta_destino}")

    def retirar_de_cuenta(self, numero_cuenta_origen, monto):
        verificar_cuenta_query = "SELECT id, saldo FROM cuentas_ahorros WHERE numero_cuenta = %s;"
        self.cursor.execute(verificar_cuenta_query, (numero_cuenta_origen,))
        cuenta_existente = self.cursor.fetchone()

        if cuenta_existente:
            cuenta_id, saldo_actual = cuenta_existente
            if saldo_actual >= monto:
                retirar_query = """
                UPDATE cuentas_ahorros
                SET saldo = saldo - %s
                WHERE numero_cuenta = %s;
                """
                self.cursor.execute(retirar_query, (monto, numero_cuenta_origen))
                self.conexion.commit()
                print(f"Retiro de {monto} realizado de la cuenta {numero_cuenta_origen}")
            else:
                print("Saldo insuficiente para realizar el retiro")
        else:
            print(f"No existe una cuenta con el número {numero_cuenta_origen}")



    def eliminar_cuenta_y_usuario(self, numero_cuenta):
        verificar_cuenta_query = "SELECT id, usuario_id FROM cuentas_ahorros WHERE numero_cuenta = %s;"
        self.cursor.execute(verificar_cuenta_query, (numero_cuenta,))
        cuenta_existente = self.cursor.fetchone()

        if cuenta_existente:
            cuenta_id, usuario_id = cuenta_existente
            eliminar_cuenta_query = "DELETE FROM cuentas_ahorros WHERE id = %s;"
            self.cursor.execute(eliminar_cuenta_query, (cuenta_id,))

            eliminar_usuario_query = "DELETE FROM usuarios WHERE id = %s;"
            self.cursor.execute(eliminar_usuario_query, (usuario_id,))

            self.conexion.commit()
            print(f"La cuenta {numero_cuenta} y su usuario asociado han sido eliminados.")
        else:
            print(f"No existe una cuenta con el número {numero_cuenta}")
