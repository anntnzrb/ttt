import os

tablero = ["_", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def clear():
    """Limpia consola dependiendo del SO"""
    os.system("cls" if os.name == "nt" else "clear")


def linea_blanco(n=1):
    """Imprime n saltos de linea

    Argumentos:
    n -- cantidad de lineas a saltar (default 1)
    """
    print("\n" * n, end="")


def dibujar_tablero():
    """Imprime el tablero"""

    sep_sp = 15  # cantidad de repeticiones
    delim = "\t|\t"  # delimitador entre celdas
    sep_cell = "-" * sep_sp  # separador de celdas
    sep_lim = "+" * sep_sp  # separador en limites de tablero

    linea_blanco(2)
    print(
        f"""
        \t\t\t3 en Raya

        |{sep_cell}|{sep_cell}|{sep_cell}|
    {delim}{tablero[1]}{delim}{tablero[2]}{delim}{tablero[3]}{delim}
        |{sep_cell}|{sep_cell}|{sep_cell}|
    {delim}{tablero[4]}{delim}{tablero[5]}{delim}{tablero[6]}{delim}
        |{sep_cell}|{sep_cell}|{sep_cell}|
    {delim}{tablero[7]}{delim}{tablero[8]}{delim}{tablero[9]}{delim}
        |{sep_cell}|{sep_cell}|{sep_cell}|
    """
    )
    linea_blanco(2)


def marcar_tablero(eleccion, sym):
    """Imprime n saltos de linea

    Argumentos:
    eleccion -- celda elegida
    sym      -- simbolo ('X' | 'O')
    """

    if tablero[1] == "1" and eleccion == 1:
        tablero[1] = sym
    elif tablero[2] == "2" and eleccion == 2:
        tablero[2] = sym
    elif tablero[3] == "3" and eleccion == 3:
        tablero[3] = sym
    elif tablero[4] == "4" and eleccion == 4:
        tablero[4] = sym
    elif tablero[5] == "5" and eleccion == 5:
        tablero[5] = sym
    elif tablero[6] == "6" and eleccion == 6:
        tablero[6] = sym
    elif tablero[7] == "7" and eleccion == 7:
        tablero[7] = sym
    elif tablero[8] == "8" and eleccion == 8:
        tablero[8] = sym
    elif tablero[9] == "9" and eleccion == 9:
        tablero[9] = sym
    else:
        print("Movimiento inválido")


def check_juego():
    """Revisa el estado del juego

    Retorna:
    0  -- juego terminado
    1  -- continua juego
    -1 -- empate
    """

    # check horizontal
    if tablero[1] == tablero[2] == tablero[3]:
        return 0
    elif tablero[4] == tablero[5] == tablero[6]:
        return 0
    elif tablero[7] == tablero[8] == tablero[9]:
        pass
        return 0

    # check vertical
    elif tablero[1] == tablero[4] == tablero[7]:
        return 0
    elif tablero[2] == tablero[5] == tablero[8]:
        return 0
    elif tablero[3] == tablero[6] == tablero[9]:
        return 0

    # check diagonal
    elif tablero[1] == tablero[5] == tablero[9]:
        return 0
    elif tablero[3] == tablero[5] == tablero[7]:
        return 0

    # empate
    elif (
        tablero[1] != "1"
        and tablero[2] != "2"
        and tablero[3] != "3"
        and tablero[4] != "4"
        and tablero[5] != "5"
        and tablero[6] != "6"
        and tablero[7] != "7"
        and tablero[8] != "8"
        and tablero[9] != "9"
    ):
        return -1

    else:
        return 1
