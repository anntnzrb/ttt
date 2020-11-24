import util as ut

if __name__ == "__main__":
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
        eleccion = int(input("Ingresa el número de una celda (1-9): "))

        # marcar tablero a partir de la celda seleccionada
        ut.marcar_tablero(eleccion, sym)

        # verificar el estado del tablero (juego)
        estado = ut.check_juego()

        # actualizar turno del jugador
        jugador += 1

    # dibujar el tablero
    ut.dibujar_tablero()

    if estado == 0:
        jugador -= 1
        print(f"El jugador '{jugador}' ('{sym}') ha ganado!")
    else:
        print("Nadie gana. Es un empate!")
