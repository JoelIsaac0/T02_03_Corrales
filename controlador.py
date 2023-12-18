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


if __name__ == "__main__":
    controlador = Controlador()
    controlador.registrar_usuario_desde_consola()
    controlador.realizar_deposito_desde_consola()

    # Agrega llamadas a otros métodos del controlador según sea necesario

    # Cerrar la conexión al finalizar
    controlador.repositorio.cerrar_conexion()
