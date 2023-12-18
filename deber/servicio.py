from modelo import Usuario, CuentaAhorros
from repositorio import Repositorio
import re

class Servicio:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def registrar_usuario(self, nombre, apellido, correo, cedula, celular):
        if not nombre or not apellido or not correo or not cedula or not celular:
            print("Por favor ingrese todos sus datos para el registro")
            return None

        if not re.match(r'^[0-9]{10}$', cedula):
            print("La cédula debe contener 10 dígitos numéricos")
            return None

        if not re.match(r'^[0-9]{10}$', celular):
            print("El número de celular debe contener 10 dígitos numéricos")
            return None

        usuario_id = self.repositorio.agregar_usuario(nombre, apellido, correo, cedula, celular)

        if usuario_id:
            print(f"Nuevo usuario agregado con ID: {usuario_id}")

            nueva_cuenta_id = self.repositorio.crear_cuenta_ahorros(usuario_id, saldo_inicial=20)

            if nueva_cuenta_id:
                print(f"Se ha creado una cuenta de ahorros con ID: {nueva_cuenta_id}")

    def realizar_deposito(self, numero_cuenta_destino, monto):
        self.repositorio.depositar_en_cuenta(numero_cuenta_destino, monto)


    def realizar_retiro(self, numero_cuenta_origen, monto):
        self.repositorio.retirar_de_cuenta(numero_cuenta_origen, monto)

    def eliminar_cuenta_y_usuario(self, numero_cuenta):
        self.repositorio.eliminar_cuenta_y_usuario(numero_cuenta)