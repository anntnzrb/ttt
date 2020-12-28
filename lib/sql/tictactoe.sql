DROP DATABASE IF EXISTS proy_sbdg1;
CREATE DATABASE IF NOT EXISTS proy_sbdg1;
use proy_sbdg1;

CREATE TABLE IF NOT EXISTS `Clasificacion` (
    `ID_clasificacion` VARCHAR(6) NOT NULL,
    `ID_campeonato` VARCHAR(6) NOT NULL,
    PRIMARY KEY (`ID_clasificacion`)
);

CREATE TABLE IF NOT EXISTS `Juega` (
    `ID_partida` VARCHAR(6) NOT NULL,
    `usuario` VARCHAR(12) NOT NULL,
    PRIMARY KEY (`ID_partida`)
);

CREATE TABLE IF NOT EXISTS `Participa` (
    `ID_campeonato` VARCHAR(6) NOT NULL,
    `usuario` VARCHAR(12) NOT NULL,
    PRIMARY KEY (`ID_campeonato`)
);

CREATE TABLE IF NOT EXISTS `Torneo Express` (
    `ID_campeonato` VARCHAR(6) NOT NULL,
    `fecha` DATETIME,
    `jugador_ganador` VARCHAR(12) NOT NULL,
    PRIMARY KEY (`ID_campeonato`)
);

CREATE TABLE IF NOT EXISTS `Jugador` (
    `usuario` VARCHAR(12) NOT NULL,
    `nombre` VARCHAR(16) NOT NULL,
    `apellido` VARCHAR(16) NOT NULL,
    `sexo` VARCHAR(2) NOT NULL,
    `email` VARCHAR(16) NOT NULL,
    `clave` VARCHAR(16) NOT NULL,
    `fecha_nacimiento` DATE,
    `estado` BOOLEAN,
    PRIMARY KEY (`usuario`)
);

CREATE TABLE IF NOT EXISTS `Jugada` (
    `ID_jugada` VARCHAR(6) NOT NULL,
    `ID_partida` VARCHAR(6) NOT NULL,
    `coordenada_x` TINYINT,
    `coordenada_y` TINYINT,
    PRIMARY KEY (`ID_jugada`)
);

CREATE TABLE IF NOT EXISTS `Partida` (
    `ID_partida` VARCHAR(6) NOT NULL,
    `fecha_inicio` DATETIME,
    `fecha_fin` DATETIME,
    `estado` BOOLEAN,
    `jugador_ganador` VARCHAR(12) NOT NULL,
    PRIMARY KEY (`ID_partida`)
);

CREATE TABLE IF NOT EXISTS `Asignación` (
    `ID_asignacion` VARCHAR(6) NOT NULL,
    `ID_campeonato` VARCHAR(6) NOT NULL,
    PRIMARY KEY (`ID_asignacion`)
);

CREATE TABLE IF NOT EXISTS `Genera` (
    `ID_campeonato` VARCHAR(6) NOT NULL,
    `ID_partida` VARCHAR(6) NOT NULL,
    PRIMARY KEY (`ID_campeonato`),
    FOREIGN KEY (`ID_partida`)
        REFERENCES Partida (`ID_partida`)
);