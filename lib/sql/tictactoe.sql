/**
* 3 en Raya - G1 
*/

DROP DATABASE IF EXISTS `tictactoe`;
CREATE DATABASE IF NOT EXISTS `tictactoe` DEFAULT CHARACTER SET utf8 ;

use tictactoe;

CREATE TABLE `Clasificacion` (
    `ID_clasificacion` VARCHAR(6),
    `ID_campeonato` VARCHAR(6),
    PRIMARY KEY (`ID_clasificacion`)
);

CREATE TABLE `Juega` (
    `ID_partida` VARCHAR(6),
    `usuario` VARCHAR(12),
    KEY `PK, FK` (`ID_partida` , `usuario`)
);

CREATE TABLE `Participa` (
    `ID_campeonato` VARCHAR(6),
    `usuario` VARCHAR(12),
    KEY `PK, FK` (`ID_campeonato` , `usuario`)
);

CREATE TABLE `Torneo Express` (
    `ID_campeonato` VARCHAR(6),
    `fecha` DATETIME,
    `jugador_ganador` VARCHAR(12),
    PRIMARY KEY (`ID_campeonato`)
);

CREATE TABLE `Jugador` (
    `usuario` VARCHAR(12),
    `nombre` VARCHAR(16),
    `apellido` VARCHAR(16),
    `sexo` VARCHAR(2),
    `email` VARCHAR(16),
    `clave` VARCHAR(16),
    `fecha_nacimiento` DATE,
    `estado` BOOLEAN,
    PRIMARY KEY (`usuario`)
);

CREATE TABLE `Jugada` (
    `ID_jugada` VARCHAR(6),
    `ID_partida` VARCHAR(6),
    `coordenada_x` TINYINT,
    `coordenada_y` TINYINT,
    PRIMARY KEY (`ID_jugada`)
);

CREATE TABLE `Partida` (
    `ID_partida` VARCHAR(6),
    `fecha_inicio` DATETIME,
    `fecha_fin` DATETIME,
    `estado` BOOLEAN,
    `jugador_ganador` VARCHAR(12),
    PRIMARY KEY (`ID_partida`)
);

CREATE TABLE `Asignación` (
    `ID_asignacion` VARCHAR(6),
    `ID_campeonato` VARCHAR(6),
    PRIMARY KEY (`ID_asignacion`)
);

CREATE TABLE `Genera` (
    `ID_campeonato` VARCHAR(6),
    `ID_partida` VARCHAR(6),
    KEY `PK FK` (`ID_campeonato` , `ID_partida`)
);