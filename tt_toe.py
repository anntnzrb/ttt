# librerias externa
import sys
import time
from _datetime import datetime

import mysql.connector
from mysql.connector import Error

# librerias de utilidades local
import util as ut
from data import *

""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Variables globales
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Ajustar variables acorde al sistema

sql_clave = "mysql"
sql_db = "proy_sbdg1"

# obtener tiempo ahora mismo
now = datetime.now()

""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Preámbulo
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def crear_conex_sv(sql_host="localhost", sql_usr="root", sql_clave="root"):
    """Función encargada de realizar la conexión con el servidor SQL

    Argumentos:
    sql_host  -- host de la base de datos
    sql_usr   -- usuario con el que se accede de la base de datos
    sql_clave -- clave para acceder a la base de datos

    Retorna:
    Objeto 'conex'
    """

    conex = None
    try:
        conex = mysql.connector.connect(
            host=sql_host,
            user=sql_usr,
            passwd=sql_clave
        )
        print("==> ! Se ha conectado al servidor de la base de datos exitosamente.")
    except Error as err:
        print(f"Se ha producido el siguiente error: '{err}'")

    return conex


def crear_bd(conex, query):
    cursor = conex.cursor()

    try:
        cursor.execute(query)
        print("==> ! Se ha creado/conectado a la base de bases existosamente.")
    except Error as err:
        print(f"==> Se ha producido el siguiente error: '{err}'")




def crear_conex_bd(sql_host, sql_usr, sql_clave, sql_bd):
    """Función encargada de realizar la conexión con la base de datos de SQL

    Argumentos:
    sql_host  -- host de la base de datos
    sql_usr   -- usuario con el que se accede de la base de datos
    sql_clave -- clave para acceder a la base de datos

    Retorna:
    Objeto 'conex'
    """

    conex = None
    try:
        conex = mysql.connector.connect(
            host=sql_host,
            user=sql_usr,
            passwd=sql_clave,
            db=sql_bd
        )
        print("==> ! Se ha conectado a la base de datos exitosamente.")
    except Error as err:
        print(f"Se ha producido el siguiente error: '{err}'")

    return conex


def exec_query(conex, query, mute=False):
    cursor = conex.cursor()

    try:
        cursor.execute(query)
        conex.commit()
        if not mute:
            print("==> Se ha procesado la consulta exitosamente.")
    except Error as err:
        print(f"==> Se ha producido el siguiente error: '{err}'")


def exec_list_query(conex, query, val, mute=False):
    cursor = conex.cursor()

    try:
        cursor.executemany(query, val)
        conex.commit()
        if not mute:
            print("==> Se ha procesado la consulta exitosamente.")
    except Error as err:
        print(f"==> Se ha producido el siguiente error: '{err}'")


def leer_consulta(conex, consulta):
    cursor = conex.cursor()
    result = None

    try:
        cursor.execute(consulta)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"==> Se ha producido el siguiente error: '{err}'")


# Inicializar conexión con el servidor SQL
conex = crear_conex_sv("localhost", "root", sql_clave)

# Crear base de datos si es que no existe
crear_bd_query = "CREATE DATABASE IF NOT EXISTS proy_sbdg1"
crear_bd(conex, crear_bd_query)

# Schema
conex = crear_conex_bd("localhost", "root", sql_clave, sql_db)
exec_query(conex, sql_tbl_partida, mute=True)
exec_query(conex, sql_tbl_jugador, mute=True)
exec_query(conex, sql_tbl_juega, mute=True)
exec_query(conex, sql_tbl_participa, mute=True)
exec_query(conex, sql_tbl_genera, mute=True)
exec_query(conex, sql_tbl_jugada, mute=True)
exec_query(conex, sql_tbl_clasificacion, mute=True)
exec_query(conex, sql_tbl_asignacion, mute=True)
exec_query(conex, sql_tbl_torneo_express, mute=True)

# Data
exec_query(conex, sql_db_data, mute=True)

""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Funciones generales
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def sol_usr():
    """ Realiza la solicitud del nombre de usuario """

    usr = input("Ingrese su nombre de usuario: ").upper()
    # verifica que no sea vacio
    while not usr.strip():
        usr = input("Ingrese su nombre de usuario: ").upper()

    return usr


def sol_clave():
    """ Realiza la solicitud de la clave del usuario """

    key = input("Ingrese clave: ")
    # verifica que no sea vacio
    while not key.strip():
        key = input("Ingrese clave: ")

    return key


def sol_estado():
    estado = None
    while estado != 0 and estado != 1:
        estado = int(input("Ingrese estado del jugador (0 :: Inactivo, 1 :: Activo): "))

    return estado


def comprobar_datos_usr(usuario, clave):
    """Comprueba datos del usuario

    Argumentos:
    usuario -- usuario solicitado a verificar
    clave   -- clave solicitada a verificar

    Retorna:
    True  -- comprobación exitosa
    False -- comprobación fallida
    """

    lineas_jugador = leer_consulta(conex, "SELECT * FROM Jugador")

    return any(fil[0] == usuario and fil[5] == clave for fil in lineas_jugador)


""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Opciones menú numérico
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def menu_opt1():
    """ Opción #1 del menú numérico :: Juego simple """

    # Solicitud de datos (Inicio de Sesión)
    user = sol_usr()
    passw = sol_clave()

    while not comprobar_datos_usr(user, passw):
        print("==> Credenciales incorrectas.")

        if input("Desea salir? (S/N): ").upper() == "S":
            sys.exit()
        else:
            user = sol_usr()
            passw = sol_clave()

    print("Acceso exitoso.")

    # Inicio de tiempo
    anio = str(now.year)
    mes = str(now.month)
    dia = str(now.day)
    hora = str(now.hour)
    minuto = str(now.minute)
    segundo = str(now.second)
    inicio = anio + mes + dia + " " + hora + minuto + segundo

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
        except Error:
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

    anio_fin = str(now.year)
    mes_fin = str(now.month)
    dia_fin = str(now.day)
    hora_fin = str(now.hour)
    minuto_fin = str(now.minute)
    segundo_fin = str(now.second)
    fin = anio_fin + mes_fin + dia_fin + " " + hora_fin + minuto_fin + segundo_fin

    id_partida = "part1"

    # sql = "INSERT INTO partida(ID_partida, fecha_inicio, fecha_fin, estado, jugador_ganador) VALUES('{}','{}','{}','{}','{}')".format(
    #    id_partida, inicio, fin, estado, jugador)
    ## executa el insert into para agregar datos a la tabla partida
    # exec_query(conex, sql)

    # conex.commit()


def menu_opt2():
    """ Opción #2 del menú numérico :: Campeonato """

    sol_num_jug = int(input("Ingrese el numero de jugadores a registrar: "))

    count = 0
    while count < sol_num_jug:
        # Solicitud de datos
        usr = sol_usr()
        clave = sol_clave()

        # Actualizar
        count += 1


def menu_opt3():
    """ Opción #3 del menú numérico :: Registro de nuevo jugador """

    # Limpiar consola
    ut.clear()

    # Solicitud de datos
    usr = sol_usr()
    nombre = input("Ingrese nombre: ").upper()
    apellido = input("Ingrese apellido: ").upper()
    sexo = input("Ingrese sexo [género] (F/M): ").upper()
    email = input("Ingrese e-mail: ").upper()
    clave = sol_clave()
    fecha_nac = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")
    estado_jugador = sol_estado()

    query = """
    INSERT INTO Jugador(usuario, nombre, apellido, sexo, email, clave, fecha_nacimiento, estado)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
    """
    val = [(usr, nombre, apellido, sexo, email, clave, fecha_nac, estado_jugador)]

    # executa el insert into para agregar datos a la tabla jugador
    exec_list_query(conex, query, val)


def main():
    """ Programa principal. """

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
        sel = int(input("Elija opción (1-4) :: "))

        # Listado de opciones (menú numérico)
        if sel == 1:
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
            sys.exit()

        else:
            ut.clear()
            print("Error")


main()
