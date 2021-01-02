-- -----------------------------------------------------------------------------
-- Preambulo 
-- -----------------------------------------------------------------------------

DROP DATABASE IF EXISTS proy_sbdg1; # testing (inseguro)

CREATE DATABASE IF NOT EXISTS proy_sbdg1;
use proy_sbdg1;

-- -----------------------------------------------------------------------------
-- Tablas
-- -----------------------------------------------------------------------------

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