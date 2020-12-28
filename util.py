import os

tablero = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}


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
    """marca el tablero

    Argumentos:
    eleccion -- celda elegida
    sym      -- simbolo ('X' | 'O')

    Retorna:
    (True, msg)  -- Acción satisfactoria + mensaje
    (False, msg) -- Acción ilegal/error + mensaje
    """

    if 0 < eleccion < 10:
        if tablero[eleccion]:
            return False, "Esta celda ya está ocupada"
        else:
            tablero[eleccion] = sym
            return True, ""
    else:
        return False, "Celda incorrecta, ingrese una celda valida (1-9)"


def check_celdas(*celdas):
    """
    Check para analizar las celdas del tablero

    Argumentos:
    *celdas -- Celda o Celdas a analizar

    Retorna:
    True  -- Todos los elementos en 'celdas' son iguales y no vacíos
    False -- Caso contrario de True
    """

    return celdas[0] and all(celda == celdas[0] for celda in celdas)


def check_fil(fila):
    """
    Check para analizar una fila del tablero

    Argumentos:
    fila -- fila a analizar

    Retorna:
    True  -- Todos los elementos de la fila son iguales
    False -- Caso contrario de True
    """

    fila = fila * 3 - 2
    return check_celdas(tablero[fila], tablero[fila + 1], tablero[fila + 2])


def check_col(col):
    """
    Check para analizar una columna del tablero

    Argumentos:
    col -- columna a analizar

    Retorna:
    True  -- Todos los elementos de la columna son iguales
    False -- Caso contrario de True
    """

    return check_celdas(tablero[col], tablero[col + 3], tablero[col + 6])


def check_juego():
    """Revisa el estado del juego

    Retorna:
    0  -- juego terminado
    1  -- continua juego
    -1 -- empate
    """

    if (
        check_fil(1)
            or check_fil(2)
            or check_fil(3)
            or check_col(1)
            or check_col(2)
            or check_col(3)
            or check_celdas(tablero[1], tablero[5], tablero[9])
            or check_celdas(tablero[3], tablero[5], tablero[7])
    ):
        return 0

    # empate
    elif all(tablero.values()):
        return -1

    # continuar
    else:
        return 1
