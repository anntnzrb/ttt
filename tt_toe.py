# librerias de utilidades local
import util as ut

# librerias externa
import pymysql
import time
import mysql.connector
from _datetime import datetime
from mysql.connector import errorcode

now = datetime.now()


connection = pymysql.connect(
    host="localhost",
    user = "root",
    password="daky1997",
    db="proy_sbdg1"
)


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
    usuario = input("Ingrese su nombre de usuario: ").upper()
    while not usuario.strip():      #verifica que no sea vacio
        usuario = input("Ingrese su nombre de usuario: ").upper()
    return usuario


def sol_clave():
    key = input("Ingrese clave: ")
    while not key.strip():       #verifica que no sea vacio
        key = input("Ingrese clave: ")
    return key

def sol_estado():
    est = 0
    while (est != "1") and (est != "2"):
        est = input("Ingrese estado del jugador(1.Activo, 2.Inactivo): ")
    return int(est)

def comprobar_usr_clave(usuario, clave):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jugador")
    lineas_jugador = cursor.fetchall()
    for fila in lineas_jugador:  # filas
        usuario_base=fila[0]         #obtiene el nombre de usuario de la base de datos para validar con el de entrada por consola
        clave_base = fila[5]        #obtiene la clave de usuario de la base de datos para validar con la de entrada por consola
        if (usuario == usuario_base) and (clave==clave_base):
            return True
        else:
            return False
    connection.close()


""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Opciones menú numérico
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def menu_opt1():
    """ Opción #1 del menú numérico :: Juego simple """


    # Solicitud de datos
    usr = sol_usr()
    clave = sol_clave()

    año = str(now.year)
    mes = str(now.month)
    dia = str(now.day)
    hora = str(now.hour)
    minuto = str(now.minute)
    segundo = str(now.second)
    inicio = año+mes+dia+" "+hora+minuto+segundo

    # TODO: check credenciales

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
        except:
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

    año_fin = str(now.year)
    mes_fin = str(now.month)
    dia_fin = str(now.day)
    hora_fin = str(now.hour)
    minuto_fin = str(now.minute)
    segundo_fin = str(now.second)
    fin = año_fin+mes_fin+dia_fin+" "+hora_fin+minuto_fin+segundo_fin

    id_partida = "part1"

    return id_partida,inicio, fin, estado, jugador

def menu_opt2():
    """ Opción #2 del menú numérico :: Campeonato """

    sol_num_jug = int(input("Ingrese el numero de jugadores a registrar: "))

    count = 0
    while count < sol_num_jug:
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
    estado_jugador=sol_estado()
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

             # Limpiar consola
             ut.clear()
             # Opción
             user=sol_usr().upper()
             passw = sol_clave()
             if comprobar_usr_clave(user,passw):
                 id_partida,inicio, fin, estado, jugador = menu_opt1()
             else:
                 while comprobar_usr_clave(user, passw)!=True:
                    print("usuario o clave incorrecto ")
                    if comprobar_usr_clave(user, passw)!=True:
                        salir = input("desea salir?(si desea salir ingrese si, caso contrario ingrese cualquier cosa)").upper()
                        if salir =="SI":
                            break
                        else:
                            user = sol_usr().upper()
                            passw = sol_clave()

                    elif comprobar_usr_clave(user, passw):
                        id_partida,inicio, fin, estado, jugador = menu_opt1()
             cursor=connection.cursor()
             sql = "INSERT INTO partida(ID_partida, fecha_inicio, fecha_fin, estado, jugador_ganador) VALUES('{}','{}','{}','{}','{}')".format(
                 id_partida,inicio, fin, estado, jugador)
             cursor.execute(sql)  # executa el insert into para agregar datos a la tabla partida

             connection.commit()

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
             cursor.execute(sql)  # executa el insert into para agregar datos a la tabla jugador

             connection.commit()

         elif sel == 4:
             print("Has salido del juego.")
             break

         else:

             ut.clear()
             print("Error")
main()