import psycopg2
import random
import string

# Conexión a la base de datos
conexion = psycopg2.connect(
    database="usuario",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cursor = conexion.cursor()

# Creación de la tabla de usuarios si no existe
crear_tabla_query = """
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    correo VARCHAR(100),
    cedula VARCHAR(20),
    celular VARCHAR(15)
);
"""
cursor.execute(crear_tabla_query)

# Creación de la tabla de cuentas bancarias si no existe
crear_tabla_cuentas_query = """
CREATE TABLE IF NOT EXISTS cuentas_bancarias (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id),
    numero_cuenta VARCHAR(20),
    saldo DECIMAL(15, 2)
);
"""
cursor.execute(crear_tabla_cuentas_query)

# Función para agregar un nuevo usuario
def agregar_usuario(nombre, apellido, correo, cedula, celular):
    try:
        # Validación de datos
        if not all([nombre, apellido, correo, cedula, celular]):
            raise ValueError("Por favor ingrese todos sus datos para el registro")

        # Verificar si el usuario ya existe por su cédula
        cursor.execute("SELECT id FROM usuarios WHERE cedula = %s;", (cedula,))
        usuario_existente = cursor.fetchone()
        if usuario_existente:
            raise ValueError("Ya existe un usuario con la misma cédula")

        # Inserción del usuario
        insertar_usuario_query = """
        INSERT INTO usuarios (nombre, apellido, correo, cedula, celular)
        VALUES (%s, %s, %s, %s, %s) RETURNING id;
        """
        cursor.execute(insertar_usuario_query, (nombre, apellido, correo, cedula, celular))
        usuario_id = cursor.fetchone()[0]
        conexion.commit()
        return usuario_id
    except Exception as e:
        print(f"Error al agregar usuario: {str(e)}")
        return None

# Función para agregar una nueva cuenta bancaria
def agregar_cuenta_bancaria(usuario_id, saldo):
    # (Manten el código de esta función igual)

# Obtener datos del usuario por consola
def obtener_datos_usuario():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    correo = input("Ingrese el correo electrónico: ")
    cedula = input("Ingrese la cédula: ")
    celular = input("Ingrese el número de celular: ")
    return nombre, apellido, correo, cedula, celular

try:
    datos_usuario = obtener_datos_usuario()
    nuevo_usuario_id = agregar_usuario(*datos_usuario)

    if nuevo_usuario_id:
        print(f"Nuevo usuario agregado con ID: {nuevo_usuario_id}")

        saldo_inicial = float(input("Ingrese el saldo inicial para la cuenta bancaria: "))
        nueva_cuenta_id = agregar_cuenta_bancaria(nuevo_usuario_id, saldo_inicial)
        if nueva_cuenta_id:
            print(f"Nueva cuenta bancaria agregada con ID: {nueva_cuenta_id}")

except Exception as e:
    print(f"Error: {str(e)}")

# Cierre de la conexión
cursor.close()
conexion.close()
