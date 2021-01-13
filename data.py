"""
Proyecto Sistemas de Bases de Datos -- Clase de datos

ESPOL - II PAO 2020
"""

""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Schema
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

sql_tbl_jugador = """
CREATE TABLE IF NOT EXISTS Jugador (
    usuario VARCHAR(16) NOT NULL PRIMARY KEY,
    nombre VARCHAR(32) NOT NULL,
    apellido VARCHAR(32) NOT NULL,
    sexo VARCHAR(1) NOT NULL,
    email VARCHAR(64) NOT NULL,
    clave VARCHAR(32) NOT NULL,
    fecha_nacimiento DATE,
    estado BOOLEAN NOT NULL
);
"""

sql_tbl_partida = """
CREATE TABLE IF NOT EXISTS Partida (
    ID_partida VARCHAR(6) NOT NULL PRIMARY KEY,
    fecha_inicio DATETIME NOT NULL,
    fecha_fin DATETIME NOT NULL,
    estado BOOLEAN NOT NULL,
    jugador_ganador VARCHAR(12) NOT NULL
);
"""

sql_tbl_juega = """
CREATE TABLE IF NOT EXISTS Juega (
    ID_partida VARCHAR(6) NOT NULL,
    usuario VARCHAR(12) NOT NULL,
    CONSTRAINT pk_juega PRIMARY KEY (ID_partida , usuario),
    CONSTRAINT fk_ID_partida_1 FOREIGN KEY (ID_partida)
        REFERENCES Partida (ID_partida),
    CONSTRAINT fk_usuario_1 FOREIGN KEY (usuario)
        REFERENCES Jugador (usuario)
);
"""

sql_tbl_torneo_express = """
CREATE TABLE IF NOT EXISTS Torneo_Express (
    ID_campeonato VARCHAR(6) NOT NULL PRIMARY KEY,
    fecha DATETIME,
    jugador_ganador VARCHAR(12) NOT NULL
);
"""

sql_tbl_clasificacion = """
CREATE TABLE IF NOT EXISTS Clasificacion (
    ID_clasificacion VARCHAR(6) NOT NULL PRIMARY KEY,
    ID_campeonato VARCHAR(6) NOT NULL
);
"""

sql_tbl_participa = """
CREATE TABLE IF NOT EXISTS Participa (
    ID_campeonato VARCHAR(6) NOT NULL,
    usuario VARCHAR(12) NOT NULL,
    CONSTRAINT pk_participa PRIMARY KEY (ID_campeonato, usuario),
    CONSTRAINT fk_usuario_2 FOREIGN KEY (usuario)
        REFERENCES Jugador (usuario)
);
"""

sql_tbl_jugada = """
CREATE TABLE IF NOT EXISTS Jugada (
    ID_jugada VARCHAR(6) NOT NULL PRIMARY KEY,
    ID_partida VARCHAR(6) NOT NULL,
    coordenada_x TINYINT,
    coordenada_y TINYINT,
    CONSTRAINT fk_ID_partida_2 FOREIGN KEY (ID_partida)
        REFERENCES Partida (ID_partida)
);
"""

sql_tbl_asignacion = """
CREATE TABLE IF NOT EXISTS Asignacion (
    ID_asignacion VARCHAR(6) NOT NULL PRIMARY KEY,
    ID_campeonato VARCHAR(6) NOT NULL
);
"""

sql_tbl_genera = """
CREATE TABLE IF NOT EXISTS Genera (
    ID_campeonato VARCHAR(6) NOT NULL,
    ID_partida VARCHAR(6) NOT NULL,
    CONSTRAINT pk_genera PRIMARY KEY (ID_campeonato , ID_partida),
    CONSTRAINT fk_ID_partida_3 FOREIGN KEY (ID_partida)
        REFERENCES Partida (ID_partida)
);
"""

""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Data
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

sql_db_data = """
INSERT IGNORE INTO Jugador VALUES
    ("QWERTY", "QWERT", "TY", "F", "QWERTY@SOY.DEV", "azerty", "1970-01-29", 0),
    ("MAGAR", "MARIA", "GARCIA", "F", "MAGAR@GNU.ORG", "magar876", "1995-07-07", 1),
    ("JLAW", "JHON", "LAWRANCE", "M", "JLAW@ESPOL.EDU.EC", "jlaw123", "1997-05-13", 0),
    ("NASANZA", "NICOLAS", "ASANZA", "M", "NASANZA@ESPOL.EDU.EC", "nasanz", "2002-03-14", 1),
    ("JUANGONZ", "JUAN ANTONIO", "GONZALEZ", "M", "JUANGONZ@ESPOL.EDU.EC", "qwerty", "1999-11-08", 1);
"""
