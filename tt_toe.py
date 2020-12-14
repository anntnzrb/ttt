# libreria de utilidades local
import util as ut


def crear_jugador():
    """ Crea un jugador y asigna su pieza a partir de stdin """

    nombre = input("Ingrese su nombre: ")
    token = input("Ingrese su pieza: ")

    return Jugador(nombre, token)


def init():
    """ Configuraciones predeterminadas para el arranque del juego """
    pass


def menu_opt1():
    """ Opción #1 del menú numérico :: Juego simple """
    # inicializar
    jugador = 1
    estado = 1

    while estado == 1:
        # limpiar consola
        ut.clear()

        # dibujar el tablero
        ut.dibujar_tablero()


def main():
    while True:
        print(
            f"""
            \t\t\t3 en Raya

            1. Juego simple
            2. Campeonato
            3. Registrar jugador
            """
        )
        sel = int(input("Elija opción (1-3) :: "))

        if sel == 1:
            ut.clear()
            menu_opt1()
        elif sel == 2:
            ut.clear()
            print("hi 2")
        elif sel == 3:
            break
        else:
            ut.clear()
            print("Error")


if __name__ == "__main__":
    main()
