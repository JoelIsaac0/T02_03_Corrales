from repositorio import Repositorio
from servicio import Servicio
import re
import random
#AUTOR: JOEL CORRALES
class Controlador:
    def __init__(self):
        self.repositorio = Repositorio()
        self.servicio = Servicio(self.repositorio)

    def registrar_usuario_desde_consola(self):
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        correo = input("Ingrese el correo electrónico: ")
        cedula = input("Ingrese la cédula (10 dígitos numéricos): ")
        celular = input("Ingrese el número de celular (10 dígitos numéricos): ")

        self.servicio.registrar_usuario(nombre, apellido, correo, cedula, celular)

    def realizar_deposito_desde_consola(self):
        numero_cuenta_destino = input("Ingrese el número de cuenta de destino: ")
        monto = float(input("Ingrese el monto a depositar: "))

        self.servicio.realizar_deposito(numero_cuenta_destino, monto)

    def realizar_retiro_desde_consola(self):
        numero_cuenta_origen = input("Ingrese el número de cuenta de origen: ")
        monto = float(input("Ingrese el monto a retirar: "))

        self.servicio.realizar_retiro(numero_cuenta_origen, monto)

    def eliminar_cuenta_y_usuario_desde_consola(self):
        numero_cuenta = input("Ingrese el número de cuenta a eliminar: ")

        self.servicio.eliminar_cuenta_y_usuario(numero_cuenta)
	
if __name__ == "__main__":
    controlador = Controlador()
    #DESCOMENTAR PARA REALIZAR LAS RESPECTIVAS FUNCIONES
    
    controlador.registrar_usuario_desde_consola()
    #controlador.realizar_deposito_desde_consola()
    #controlador.eliminar_cuenta_y_usuario_desde_consola()
    controlador.realizar_deposito_desde_consola()
    controlador.realizar_retiro_desde_consola()
    # Cerrar la conexión al finalizar
    controlador.repositorio.cerrar_conexion()
