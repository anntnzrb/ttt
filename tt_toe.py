tablero = ["_", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

msgs = {"titulo": "\n\n\n3 en Raya\n", "tbl1": "a"}


def linea_blanco(n):
    print("\n" * n, end="")


def dibujar_tablero():
    sep_sp = 15  # cantidad de repeticiones
    delim = "\t|\t" # delimitador entre celdas
    sep_cell = "-" * sep_sp  # separador de celdas
    sep_lim = "+" * sep_sp  # separador en limites de tablero

    linea_blanco(2)
    print(f"\t|{sep_cell}|{sep_cell}|{sep_cell}|")
    print(f"{delim}{tablero[1]}{delim}{tablero[2]}{delim}{tablero[3]}{delim}")
    print(f"\t|{sep_cell}|{sep_cell}|{sep_cell}|")
    print(f"{delim}{tablero[4]}{delim}{tablero[5]}{delim}{tablero[6]}{delim}")
    print(f"\t|{sep_cell}|{sep_cell}|{sep_cell}|")
    print(f"{delim}{tablero[7]}{delim}{tablero[8]}{delim}{tablero[9]}{delim}")
    linea_blanco(2)


dibujar_tablero()
