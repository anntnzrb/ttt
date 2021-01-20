"""
Proyecto Sistemas de Bases de Datos -- Clase Principal

ESPOL - II PAO 2020

Referencias:
https://github.com/thecraigd/Python_SQL/blob/master/mysql.ipynb
"""

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

sql_clave = ""
sql_db = "proy_sbdg1"

# obtener tiempo ahora mismo
now = datetime.now()

""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Preámbulo
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def crear_conex_sv(sql_host="localhost", sql_usr="root", sql_clave=""):
    """
    Función encargada de realizar la conexión con el servidor SQL

    @param sql_host: Host de la base de datos
    @param sql_usr: Usuario con el que se accede de la base de datos
    @param sql_clave: Clave para acceder a la base de datos
    @return: Objeto 'conex'
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
    """

    Crea la base de datos si es que ésta no está presente,
    no hace nada en caso contrario.

    @param conex: Objeto de conección a SQL
    @param query: Consulta a realizar
    """
    cursor = conex.cursor()

    try:
        cursor.execute(query)
        print("==> ! Se ha creado/conectado a la base de bases existosamente.")
    except Error as err:
        print(f"==> Se ha producido el siguiente error: '{err}'")


def crear_conex_bd(sql_host="localhost", sql_usr="root", sql_clave="root", sql_bd=None):
    """
    Función encargada de realizar la conexión con la base de datos de SQL

    @param sql_host: Host de la base de datos
    @param sql_usr: Usuario con el que se accede de la base de datos
    @param sql_clave: Clave para acceder a la base de datos
    @param sql_bd: Nomhbre de la base de datos a conectar
    @return: Objeto 'conex'
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
    """
    Función encargada de realizar un query y hacer commit a la base de datos.

    @param conex: Objeto de conección a SQL
    @param query: Consulta a realizar
    @param mute: Parámetro adicional para suprimir mensaje en pantalla
    """

    cursor = conex.cursor()

    try:
        cursor.execute(query)
        conex.commit()
        if not mute:
            print("==> Se ha procesado la consulta exitosamente.")
    except Error as err:
        print(f"==> Se ha producido el siguiente error: '{err}'")


def exec_list_query(conex, query, val, mute=False):
    """
    Función encargada de realizar un query con valores pasados como parámetro
    y hacer commit a la base de datos.

    @param conex: Objeto de conección a SQL
    @param query: Consulta a realizar
    @param val: Lista de valores para ser aplicada junto al query
    @param mute: Parámetro adicional para suprimir mensaje en pantalla
    """
    cursor = conex.cursor()

    try:
        cursor.executemany(query, val)
        conex.commit()
        if not mute:
            print("==> Se ha procesado la consulta exitosamente.")
    except Error as err:
        print(f"==> Se ha producido el siguiente error: '{err}'")


def leer_consulta(conex, consulta):
    """
    Función encargada de recoger información de la base de datos para
    posteriormente realizar alguna acción.

    @param conex: Objeto de conección a SQL
    @param consulta: Consulta a realizar
    @return:
    """
    cursor = conex.cursor()

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

def comprobar_datos_usr(usuario, clave):
    """
    Comprueba datos del usuario.

    @param usuario: usuario solicitado a verificar
    @param clave: clave solicitada a verificar
    @return:
    True  -- comprobación exitosa
    False -- comprobación fallida
    """

    lineas_jugador = leer_consulta(conex, "SELECT * FROM Jugador")

    return any(fil[0] == usuario and fil[5] == clave for fil in lineas_jugador)

def iniciar_partida():
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

    #query = 'INSERT INTO partida(fecha_inicio, fecha_fin, estado, jugador_ganador) VALUES('+inicio+','+fin+','+estado+',"JLOW")'

    ## executa el insert into para agregar datos a la tabla partida
    #exec_query(conex, query)

""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Opciones menú numérico
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def menu_opt1():
    """ Opción #1 del menú numérico :: Juego simple """

    # Ingreso de jugadores
    jugador1=input("Ingrese el usuario del jugador 1: ").upper()
    jugador2= input ("Ingrese el usuario del jugador 2: ").upper()

    try:
        #verificacion de status
        verif1=leer_consulta(conex, "select estado from jugador where usuario= \"" +jugador1+"\";")[0]
        verif2=leer_consulta(conex, "select estado from jugador where usuario= \"" +jugador2+"\";")[0]

        if verif1[0]==1 and verif2[0]==1:
            iniciar_partida()

        elif verif1[0]!=1:
            print("El jugador 1 no se ha loogeado!!")

        elif verif2[0]!=1:
            print("El jugador 2 no se ha loogeado!!")

    except IndexError:
        print("usuario mal ingresado")

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
    estado_jugador = 0

    query = """
    INSERT INTO Jugador(usuario, nombre, apellido, sexo, email, clave, fecha_nacimiento, estado)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
    """
    val = [(usr, nombre, apellido, sexo, email, clave, fecha_nac, estado_jugador)]

    # executa el insert into para agregar datos a la tabla jugador
    exec_list_query(conex, query, val)

def menu_opt4():
    """ Permite que un jugador inicie seción para poder jugar """
    usuario=input("Ingrese su usuario: ").upper()
    contraseña=input("Ingrese su contraseña: ")

    query='select usuario, clave from jugador where usuario = \"'+ usuario +'\";'
    try:
        comparar=leer_consulta(conex, query)[0]

        rusuario, rcontraseña= comparar

        if usuario==rusuario and contraseña==rcontraseña:
            query2='update jugador set estado=1 where usuario=\"' + rusuario +'\";'
            exec_query(conex,query2,True)
            print(' ACCESO CORRECTO ')
        else:
            print(' ACCESO INCORRECTO ')
    except IndexError as err:
        print(' Usuario no existe ')

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
            4. Iniciar sesión
            5. Salir
            """
        )

        # Seleccionar opción
        sel = int(input("Elija opción (1-5): "))

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
            menu_opt4()

        elif sel == 5:

            print("Has salido del juego.")
            query = 'update jugador set estado=0 where estado=1;'
            exec_query(conex, query, True)
            sys.exit()

        else:
            ut.clear()
            print("Error")


# Programa
if __name__ == "__main__":
    main()
