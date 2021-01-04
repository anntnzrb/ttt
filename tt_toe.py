# librerias de utilidades local
import util as ut

# librerias externa
import pymysql
import time
import getpass
import mysql.connector
from mysql.connector import errorcode

connection = pymysql.connect(
    host="localhost",
    user = "root",
    password="daky1997",
    db="proy_sbdg1"
)
cursor = connection.cursor()


""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Funciones generales
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def crear_jugador():
    """ Crea un jugador y asigna su pieza a partir de stdin """

    nombre = input("Ingrese su nombre: ")
    token = input("Ingrese su pieza: ")

    return Jugador(nombre, token)


def sol_usr():
    """ Realiza la solicitud del nombre de usuario """
    usuario = input("Ingrese su nombre de usuario: ").upper()
    while not usuario.strip():      #verifica que no sea vacio
        usuario = input("Ingrese su nombre de usuario: ").upper()
    return


# def sol_clave():
#     """ Realiza la solicitud de la clave del usuario """
#     return getpass.getpass(prompt="Ingrese clave (no se mostrará en pantalla): ").upper()

def sol_clave():
    key = input("Ingrese clave: ")
    while not key.strip():       #verifica que no sea vacio
        key = input("Ingrese clave: ")
    return key

def sol_estado():
    est = 0
    while (est != "1") and (est != "2"):
        est = input("Ingrese estado del jugador(1.Activo, 2.Inactivo: )")
    return int(est)


""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Opciones menú numérico
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def menu_opt1():
    """ Opción #1 del menú numérico :: Juego simple """

    # Solicitud de datos
    usr = sol_usr()
    clave = sol_clave()

    # TODO: check credenciales

    # valores iniciales
    jugador = 1
    estado = 1

    while estado == 1:
        # limpiar consola
        ut.clear()

        # dibujar el tablero
        ut.dibujar_tablero()

        # actualizar turno
        jugador = 1 if jugador % 2 else 2
        sym = "X" if jugador == 1 else "O"
        print(f"Es el turno del jugador '{jugador}' ('{sym}')\n")

        # interceptar elección de celda
        try:
            eleccion = int(input("Ingresa el número de una celda (1-9): "))
        except:
            print("Eso no es un numero...")
            print("Intenta de nuevo...")
            time.sleep(2)
            continue

        # marcar tablero a partir de la celda seleccionada
        error, err_msg = ut.marcar_tablero(eleccion, sym)

        # mostrar errores
        if error:
            print(err_msg)
            time.sleep(1)

        # verificar el estado del tablero (juego)
        estado = ut.check_juego()

        # actualizar turno del jugador
        if not error:
            jugador += 1

    # dibujar el tablero
    ut.dibujar_tablero()

    if estado == 0:
        jugador -= 1
        print(f"El jugador '{jugador}' ('{sym}') ha ganado!")

        # restablecer tablero
        ut.tablero = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
    else:
        print("Nadie gana. Es un empate!")
        # restablecer tablero
        ut.tablero = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}

def menu_opt2():
    """ Opción #2 del menú numérico :: Campeonato """

    sol_num_jug = int(input("Ingrese el numero de jugadores a registrar: "))

    count = 0
    while count < sol_num_jug:
        # Solicitud de datos
        usr = sol_usr()
        clave = sol_clave()

        # Actualizar
        count +=1


def menu_opt3():
    """ Opción #3 del menú numérico :: Registro de nuevo jugador """

    # Solicitud de datos
    usr = sol_usr()
    nombre = input("Ingrese nombre: ").upper()
    apellido = input("Ingrese apellido: ").upper()
    sexo = input("Ingrese sexo [género] (F/M): ").upper()
    email = input("Ingrese e-mail: ").upper()
    clave = sol_clave()
    fecha_nac = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")
    estado_jugador=sol_estado()
    return usr, nombre, apellido, sexo, email, clave, fecha_nac

usr, nombre, apellido, sexo, email, clave, fecha_nac, estado_jugador = menu_opt3()

sql = "INSERT INTO jugador(usuario, nombre, apellido, sexo, email, clave, fecha_nacimiento,estado) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(usr,nombre,apellido,sexo,email,clave,fecha_nac,estado,estado_jugador)
cursor.execute(sql)

connection.commit()


""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# SQL
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def conect_sql():
#     """ Realiza la conexión a las base de datos SQL bajo credenciales
#     específicas."""
#
#     # credenciales
#     sql_config = {
#         'host': "localhost",
#         'user': "root",
#         'passwd': "mysql",
#         'db': "proy_sbdg1"
#     }
#
#     # Intento de conexión
#     conx = mysql.connector.connect(**sql_config)


# def main():
#     """ Programa principal. """
#
#     # Conexión SQL
#     # conect_sql()
#
#     # Menú numérico
#     while True:
#         print(
#             """
#             \t\t\t3 en Raya
#
#             1. Juego simple
#             2. Campeonato
#             3. Registrar jugador
#             4. Salir
#             """
#         )
#
#         # Seleccionar opción
#         sel = int(input("Elija opción (1-3) :: "))
#
#         # Listado de opciones (menú numérico)
#         if sel == 1:
#             # Limpiar consola
#             ut.clear()
#
#             # Opción
#             menu_opt1()
#
#         elif sel == 2:
#             # Limpiar consola
#             ut.clear()
#
#             # Opción
#             menu_opt2()
#
#         elif sel == 3:
#             # Limpiar consola
#             ut.clear()
#
#             # Opción
#             menu_opt3()
#
#         elif sel == 4:
#             print("Has salido del juego.")
#             break
#
#         else:
#             ut.clear()
#             print("Error")
#
# # if __name__ == "__main__":
# #     main()
