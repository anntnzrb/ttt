# librerias de utilidades local
import util as ut

# librerias externa
import time
import getpass
import mysql.connector
from mysql.connector import errorcode


""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Opciones menú numérico
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def menu_opt1():
    """ Opción #1 del menú numérico :: Juego simple """
    pass
def menu_opt2():
    """ Opción #2 del menú numérico :: Campeonato """

    sol_num_jug = int(input("Ingrese el numero de jugadores a registrar: "))

    count = 0
    while sol_num_jug > count:
        sol_usr = input("Ingrese nombre de usuario: ").upper()
        sol_clave = getpass.getpass(prompt="Ingrese clave (no se mostrará en pantalla): ")

        # actualizar
        count +=1


def menu_opt3():
    """ Opción #3 del menú numérico :: Registro de nuevo jugador """

    # debug
    # credenciales
    sql_config = {
        'host': "localhost",
        'user': "root",
        'passwd': "mysql",
        'db': "proy_sbdg1"
    }

    # Intento de conexión
    conx = mysql.connector.connect(**sql_config)

    # cursor
    cursor = conx.cursor()

    # solicitar usuario
    sol_usr = input("Ingrese nombre de usuario: ")
    cursor.excute("SHOW TABLES")

    sol_clave = getpass.getpass(prompt="Ingrese clave (no se mostrará en pantalla): ")


""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# SQL
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def conect_sql():
    """ Realiza la conexión a las base de datos SQL bajo credenciales
    específicas."""

    # credenciales
    sql_config = {
        'host': "localhost",
        'user': "root",
        'passwd': "mysql",
        'db': "proy_sbdg1"
    }

    # Intento de conexión
    conx = mysql.connector.connect(**sql_config)

    # cursor
    cursor = conx.cursor()


""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Funciones generales
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def crear_jugador():
    """ Crea un jugador y asigna su pieza a partir de stdin """

    nombre = input("Ingrese su nombre: ")
    token = input("Ingrese su pieza: ")

    return Jugador(nombre, token)


def init():
    """ Configuraciones predeterminadas para el arranque del juego """
    pass


def sol_usr():
    return input("Ingrese su nombre de usuario: ")


def sol_clave():
    return getpass.getpass(prompt='Clave (no se mostrará en pantalla): ')


def main():
    """ Programa principal. """

    # Conexión SQL
    conect_sql()

    # Menú numérico
    while True:
        print(
            """
            \t\t\t3 en Raya

            1. Juego simple
            2. Campeonato
            3. Registrar jugador
            4. Salir
            """
        )

        # Seleccionar opción
        sel = int(input("Elija opción (1-3) :: "))

        # Listado de opciones (menú numérico)
        if sel == 1:
            # Limpiar consola
            ut.clear()

            # Opción
            menu_opt1()

        elif sel == 2:
            # Limpiar consola
            ut.clear()

            # Opción
            menu_opt2()

        elif sel == 3:
            menu_opt3()
        elif sel == 4:
            print("Has salido del juego.")
            break
        else:
            ut.clear()
            print("Error")

if __name__ == "__main__":
    main()
