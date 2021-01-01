# librerias de utilidades local
import util as ut

# librerias externa
import time
import getpass
import mysql.connector


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
            ut.clear()
            print("hi 2")
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
