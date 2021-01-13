# Proyecto Sistemas de Bases de Datos - G1

<!-- Markdown TOC :: Start -->
**Tabla de Contenidos**

- [Proyecto Sistemas de Bases de Datos - G1](#proyecto-sistemas-de-bases-de-datos---g1)
    - [Instrucciones del proyecto](#instrucciones-del-proyecto)
    - [Sistema](#sistema)
        - [Instrucciones dependencias de Python](#instrucciones-dependencias-de-python)
    - [Integrantes](#integrantes)

<!-- Markdown TOC :: End -->

## Instrucciones del proyecto

El proyecto consistirá en que usted debe implementar una aplicación de juego de
3 en raya, para esto el sistema debe cumplir lo siguiente.

Cada jugador se debe registrar y va a contener los datos de nombre, apellido,
usuario, contraseña, estado(activo:1, inactivo:2), email, sexo, fecha de
nacimiento.

Los jugadores ingresan al sistema con su usuario y su contraseña y generan una
nueva partida.

Cada partida debe guardarse los datos de fecha y hora de inicio, fecha y hora de
fin, los dos jugadores, el jugador ganador, en caso de empate el jugador ganador
debe tener un valor de null; el estado de la partida (1: terminada, 2:
abandonada)

Adicional de cada partida debe guardarse las coordenadas que cada jugador
escogió en el siguiente sistema de coordenadas.

| (0,0) | (0,1) | (0,2) |
|:-----:|:-----:|:-----:|
| (1,0) | (1,1) | (1,2) |
| (2,0) | (2,1) | (2,2) |

Cada partida ganada aumenta un valor de 5 pts al score del jugador ganador. Este
dato no se deba almacenar , se debe calcular.

Adicional, Se puede crear campeonatos express, para lo cual se debe almacenar la
asignación y clasificación de los jugadores, la fecha del campeonato, y el
ganador el cual le suma 10 pts al score del jugador.

**NOTA** :: Documento original (completo) en [PDF](./lib/docs/Proyecto_SDB.pdf).

## Sistema

### Instrucciones dependencias de Python

El proyecto está escrito en Python, la lista de requerimientos de
[pip](https://pypi.org/) se encuentra en
[este archivo txt](./lib/python/requirements.txt)

Se pueden instalar dichos requerimientos mediante:

(_estando en la ruta principal del proyecto_)

```console
pip install -r ./lib/python/requirements.txt
```

## Integrantes

Grupo #1

- Juan Antonio González Orbe :: `juangonz@espol.edu.ec`
- Rogger Daniel Jimenez Silva :: `rodajime@espol.edu.ec`
- Darwin Adrian Kuonqui Yance :: `dkuonqui@espol.edu.ec`
- Andres Marcelo Noboa Veliz Veliz :: `amnoboa@espol.edu.ec`
- Bryan Jair Segovia Mariscal :: `bsegovia@espol.edu.ec`
