# librerias de utilidades local
import util as ut

# librerias externa
import time
import getpass
import mysql.connector
from mysql.connector import errorcode


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
    return input("Ingrese su nombre de usuario: ").upper()


def sol_clave():
    """ Realiza la solicitud de la clave del usuario """
    return getpass.getpass(prompt="Ingrese clave (no se mostrará en pantalla): ").upper()


""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Opciones menú numérico
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def menu_opt1():
    """ Opción #1 del menú numérico :: Juego simple """

    # Solicitud de datos
    usr = sol_usr()
    clave = sol_clave()

def menu_opt2():
    """ Opción #2 del menú numérico :: Campeonato """

    sol_num_jug = int(input("Ingrese el numero de jugadores a registrar: "))

    count = 0
    while sol_num_jug > count:
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
            # Limpiar consola
            ut.clear()

            # Opción
            menu_opt3()

        elif sel == 4:
            print("Has salido del juego.")
            break

        else:
            ut.clear()
            print("Error")

if __name__ == "__main__":
    main()
