# librerias externa
import sys
import time
from _datetime import datetime

import mysql.connector
from mysql.connector import Error

# librerias de utilidades local
import util as ut

""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Datos
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Ajustar siguientes variables acorde a su sistema

sql_host = "localhost"
sql_usr = "root"
sql_clave = "mysql"

""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Variables globales
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# obtener tiempo ahora mismo
now = datetime.now()

""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Preámbulo
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def crear_conex_sv(sql_host, sql_usr, sql_clave):
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
        print("==> Se ha conectado a la base de datos de forma exitosa.")
    except Error as err:
        print(f"Se ha producido el siguiente error: '{err}'")

    return conex


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
        print("==> Se ha conectado a la base de datos de forma exitosa.")
    except Error as err:
        print(f"Se ha producido el siguiente error: '{err}'")

    return conex


def crear_bd(conex, consulta):
    cursor = conex.cursor()

    try:
        cursor.execute(consulta, multi=True)
        print("==> Se ha creado la base de bases de forma existosa.")
    except Error as err:
        print(f"==> Se ha producido el siguiente error: '{err}'")


def exec_consulta(conex, consulta):
    cursor = conex.cursor()

    try:
        cursor.execute(consulta, multi=True)
        conex.commit()
        print("==> Se ha procesado la consulta exitosamente.")
    except Error as err:
        print(f"==> Se ha producido el siguiente error: '{err}'")


def leer_consulta(conex, consulta):
    cursor = conex.cursor()

    try:
        cursor.execute(consulta)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"==> Se ha producido el siguiente error: '{err}'")


# Iniciar conexión con SQL
conex = crear_conex_sv(sql_host, sql_usr, sql_clave)

# Crear base de datos si es que no existe
crear_bd(conex, "CREATE DATABASE IF NOT EXISTS proy_sbdg1")

# Conexión con base de datos
conex = crear_conex_bd(sql_host, sql_usr, sql_clave, "proy_sbdg1")

# Datos de base de datos (Schema)
sql_db_schema = """
USE proy_sbdg1;

CREATE TABLE IF NOT EXISTS `Jugador` (
    `usuario` VARCHAR(16) NOT NULL PRIMARY KEY,
    `nombre` VARCHAR(32) NOT NULL,
    `apellido` VARCHAR(32) NOT NULL,
    `sexo` VARCHAR(1) NOT NULL,
    `email` VARCHAR(64) NOT NULL,
    `clave` VARCHAR(32) NOT NULL,
    `fecha_nacimiento` DATE,
    `estado` BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS `Partida` (
    `ID_partida` VARCHAR(6) NOT NULL PRIMARY KEY,
    `fecha_inicio` DATETIME NOT NULL,
    `fecha_fin` DATETIME NOT NULL,
    `estado` BOOLEAN NOT NULL,
    `jugador_ganador` VARCHAR(12) NOT NULL
);

CREATE TABLE IF NOT EXISTS `Juega` (
    `ID_partida` VARCHAR(6) NOT NULL,
    `usuario` VARCHAR(12) NOT NULL,
    CONSTRAINT `pk_juega` PRIMARY KEY (`ID_partida` , `usuario`),
    CONSTRAINT `fk_ID_partida_1` FOREIGN KEY (`ID_partida`)
        REFERENCES Partida (`ID_partida`),
    CONSTRAINT `fk_usuario_1` FOREIGN KEY (`usuario`)
        REFERENCES Jugador (`usuario`)
);

CREATE TABLE IF NOT EXISTS `Torneo_Express` (
    `ID_campeonato` VARCHAR(6) NOT NULL PRIMARY KEY,
    `fecha` DATETIME,
    `jugador_ganador` VARCHAR(12) NOT NULL
);

CREATE TABLE IF NOT EXISTS `Clasificacion` (
    `ID_clasificacion` VARCHAR(6) NOT NULL PRIMARY KEY,
    `ID_campeonato` VARCHAR(6) NOT NULL,
    CONSTRAINT `fk_ID_campeonato_1` FOREIGN KEY (`ID_campeonato`)
        REFERENCES Torneo_Express (`ID_campeonato`)
);

CREATE TABLE IF NOT EXISTS `Participa` (
    `ID_campeonato` VARCHAR(6) NOT NULL,
    `usuario` VARCHAR(12) NOT NULL,
    CONSTRAINT `pk_participa` PRIMARY KEY (`ID_campeonato`, `usuario`),
    CONSTRAINT `fk_ID_campeonato_2` FOREIGN KEY (`ID_campeonato`)
        REFERENCES Torneo_Express (`ID_campeonato`),
    CONSTRAINT `fk_usuario_2` FOREIGN KEY (`usuario`)
        REFERENCES Jugador (`usuario`)
);

CREATE TABLE IF NOT EXISTS `Jugada` (
    `ID_jugada` VARCHAR(6) NOT NULL PRIMARY KEY,
    `ID_partida` VARCHAR(6) NOT NULL,
    `coordenada_x` TINYINT,
    `coordenada_y` TINYINT,
    CONSTRAINT `fk_ID_partida_2` FOREIGN KEY (`ID_partida`)
        REFERENCES Partida (`ID_partida`)
);

CREATE TABLE IF NOT EXISTS `Asignacion` (
    `ID_asignacion` VARCHAR(6) NOT NULL PRIMARY KEY,
    `ID_campeonato` VARCHAR(6) NOT NULL,
    CONSTRAINT `fk_ID_campeonato_3` FOREIGN KEY (`ID_campeonato`)
        REFERENCES Torneo_Express (`ID_campeonato`)
);

CREATE TABLE IF NOT EXISTS `Genera` (
    `ID_campeonato` VARCHAR(6) NOT NULL,
    `ID_partida` VARCHAR(6) NOT NULL,
    CONSTRAINT `pk_genera` PRIMARY KEY (`ID_campeonato` , `ID_partida`),
    CONSTRAINT `fk_ID_partida_3` FOREIGN KEY (`ID_partida`)
        REFERENCES Partida (`ID_partida`),
    CONSTRAINT `fk_ID_campeonato_4` FOREIGN KEY (`ID_campeonato`)
        REFERENCES Torneo_Express (`ID_campeonato`)
);
"""

# Crear base de datos (Schema)
crear_bd(conex, sql_db_schema)

# Datos de base de datos (Data)
sql_db_data = """
INSERT INTO `Jugador`
    VALUES ("QWERTY", "QWERT", "TY", "F", "QWERTY@SOY.DEV", "azerty", "1970-01-29", 0);
INSERT INTO `Jugador`
    VALUES ("MAGAR", "Maria", "GARCIA", "F", "MAGAR@GNU.ORG", "magar876", "1995-07-07", 0);
INSERT INTO `Jugador`
    VALUES ("JLAW", "JHON", "Lawrance", "M", "JLAW@ESPOL.EDU.EC", "jlaw123", "1997-05-13", 0);
INSERT INTO `Jugador`
    VALUES ("NASANZA", "NICOLAS", "ASANZA", "M", "NASANZA@ESPOL.EDU.EC", "nasanz", "2002-03-14", 0);
INSERT INTO `Jugador`
    VALUES ("JUANGONZ", "JUAN ANTONIO", "GONZALEZ", "M", "JUANGONZ@ESPOL.EDU.EC", "qwerty", "1999-11-08", 0);
"""

# Agregar defaults a la base de datos (Data)
exec_consulta(conex, sql_db_data)

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
    est = 0
    while (est != "1") and (est != "2"):
        est = input("Ingrese estado del jugador(1.Activo, 2.Inactivo): ")
    return int(est)


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

    for fil in lineas_jugador:
        # obtiene el nombre de usuario de la base de datos para validar con el de entrada por consola
        usr_bd = fil[0]
        # obtiene la clave de usuario de la base de datos para validar con la de entrada por consola
        clave_bd = fil[5]

        return True if (usuario == usr_bd) and (clave == clave_bd) else False


""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Opciones menú numérico
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def menu_opt1():
    """ Opción #1 del menú numérico :: Juego simple """

    # Solicitud de datos
    usr = sol_usr()
    clave = sol_clave()

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

    return id_partida, inicio, fin, estado, jugador


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

    # Solicitud de datos
    usr = sol_usr()
    nombre = input("Ingrese nombre: ").upper()
    apellido = input("Ingrese apellido: ").upper()
    sexo = input("Ingrese sexo [género] (F/M): ").upper()
    email = input("Ingrese e-mail: ").upper()
    clave = sol_clave()
    fecha_nac = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")
    estado_jugador = sol_estado()

    return usr, nombre, apellido, sexo, email, clave, fecha_nac, estado_jugador


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
        sel = int(input("Elija opción (1-3) :: "))

        # Listado de opciones (menú numérico)
        if sel == 1:
            # Opción
            user = sol_usr()
            passw = sol_clave()
            if comprobar_datos_usr(user, passw):
                id_partida, inicio, fin, estado, jugador = menu_opt1()
            else:
                while not comprobar_datos_usr(user, passw):
                    print("==> Credenciales incorrectas.")
                    if not comprobar_datos_usr(user, passw):
                        salir = input("Desea salir? (S/N): ").upper()
                        if salir == "S":
                            sys.exit()
                        else:
                            user = sol_usr()
                            passw = sol_clave()

                    elif comprobar_datos_usr(user, passw):
                        id_partida, inicio, fin, estado, jugador = menu_opt1()
            sql = "INSERT INTO partida(ID_partida, fecha_inicio, fecha_fin, estado, jugador_ganador) VALUES('{}','{}','{}','{}','{}')".format(
                id_partida, inicio, fin, estado, jugador)
            # executa el insert into para agregar datos a la tabla partida
            exec_consulta(conex, sql)

            conex.commit()

        elif sel == 2:
            # Limpiar consola
            ut.clear()

            # Opción
            menu_opt2()

        elif sel == 3:
            # Limpiar consola
            ut.clear()

            # Opción
            usr, nombre, apellido, sexo, email, clave, fecha_nac, estado_jugador = menu_opt3()

            sql = "INSERT INTO jugador(usuario, nombre, apellido, sexo, email, clave, fecha_nacimiento,estado) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(
                usr, nombre, apellido, sexo, email, clave, fecha_nac, estado_jugador)

            # executa el insert into para agregar datos a la tabla jugador
            exec_consulta(conex, sql)

            conex.commit()

        elif sel == 4:
            print("Has salido del juego.")
            break

        else:

            ut.clear()
            print("Error")


main()
