-- MySQL Script generated by MySQL Workbench
-- Tue Jul 23 14:09:44 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema cine
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cine
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cine` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `cine` ;

-- -----------------------------------------------------
-- Table `cine`.`peliculas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine`.`peliculas` (
  `pelicula_id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(100) NOT NULL,
  `genero` VARCHAR(45) NOT NULL,
  `duracion` INT NOT NULL,
  `rating` DECIMAL(3,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`pelicula_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1862
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cine`.`salas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine`.`salas` (
  `sala_id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `capacidad` INT NOT NULL,
  `estado` TINYINT NOT NULL,
  PRIMARY KEY (`sala_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 7127
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cine`.`horarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine`.`horarios` (
  `horario_id` INT NOT NULL AUTO_INCREMENT,
  `pelicula_id` INT NOT NULL,
  `sala_id` INT NOT NULL,
  `fecha` DATETIME NOT NULL,
  PRIMARY KEY (`horario_id`),
  INDEX `fk_horarios_peliculas` (`pelicula_id` ASC) VISIBLE,
  INDEX `fk_horarios_salas` (`sala_id` ASC) VISIBLE,
  CONSTRAINT `fk_horarios_peliculas`
    FOREIGN KEY (`pelicula_id`)
    REFERENCES `cine`.`peliculas` (`pelicula_id`),
  CONSTRAINT `fk_horarios_salas`
    FOREIGN KEY (`sala_id`)
    REFERENCES `cine`.`salas` (`sala_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 37882
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cine`.`asientos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine`.`asientos` (
  `asiento_id` INT NOT NULL AUTO_INCREMENT,
  `numero_asiento` INT NOT NULL,
  `seccion` VARCHAR(45) NOT NULL,
  `sala_id` INT NOT NULL,
  `estado` TINYINT NOT NULL,
  `horario_id` INT NOT NULL,
  PRIMARY KEY (`asiento_id`),
  INDEX `salas_id_idx` (`sala_id` ASC) VISIBLE,
  INDEX `fk_horario_asientos_id_idx` (`horario_id` ASC) VISIBLE,
  CONSTRAINT `fk_horario_asientos_id`
    FOREIGN KEY (`horario_id`)
    REFERENCES `cine`.`horarios` (`horario_id`),
  CONSTRAINT `fk_salas_asientos_id`
    FOREIGN KEY (`sala_id`)
    REFERENCES `cine`.`salas` (`sala_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cine`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine`.`clientes` (
  `cliente_id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `apellido` VARCHAR(100) NOT NULL,
  `correo` VARCHAR(100) NULL DEFAULT NULL,
  `documento` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cliente_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1201
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cine`.`ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine`.`ventas` (
  `venta_id` INT NOT NULL AUTO_INCREMENT,
  `cliente_id` INT NOT NULL,
  `pelicula_id` INT NOT NULL,
  `horario_id` INT NOT NULL,
  `fecha_venta` DATE NOT NULL,
  `asiento_id` INT NOT NULL,
  PRIMARY KEY (`venta_id`),
  INDEX `fk_ventas_clientes` (`cliente_id` ASC) VISIBLE,
  INDEX `fk_ventas_peliculas` (`pelicula_id` ASC) VISIBLE,
  INDEX `fk_ventas_horarios` (`horario_id` ASC) VISIBLE,
  INDEX `fk_ventas_asientos_idx` (`asiento_id` ASC) VISIBLE,
  CONSTRAINT `fk_ventas_asientos`
    FOREIGN KEY (`asiento_id`)
    REFERENCES `cine`.`asientos` (`asiento_id`),
  CONSTRAINT `fk_ventas_clientes`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `cine`.`clientes` (`cliente_id`),
  CONSTRAINT `fk_ventas_horarios`
    FOREIGN KEY (`horario_id`)
    REFERENCES `cine`.`horarios` (`horario_id`),
  CONSTRAINT `fk_ventas_peliculas`
    FOREIGN KEY (`pelicula_id`)
    REFERENCES `cine`.`peliculas` (`pelicula_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `cine` ;

-- -----------------------------------------------------
-- Placeholder table for view `cine`.`vista_general_asientos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine`.`vista_general_asientos` (`asiento_id` INT, `numero_asiento` INT, `seccion` INT, `sala_id` INT, `estado` INT, `horario_id` INT);

-- -----------------------------------------------------
-- Placeholder table for view `cine`.`vista_general_clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine`.`vista_general_clientes` (`cliente_id` INT, `nombre` INT, `apellido` INT, `correo` INT, `documento` INT);

-- -----------------------------------------------------
-- Placeholder table for view `cine`.`vista_general_horarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine`.`vista_general_horarios` (`horario_id` INT, `pelicula_id` INT, `sala_id` INT, `fecha` INT);

-- -----------------------------------------------------
-- Placeholder table for view `cine`.`vista_general_peliculas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine`.`vista_general_peliculas` (`pelicula_id` INT, `titulo` INT, `genero` INT, `duracion` INT, `rating` INT);

-- -----------------------------------------------------
-- Placeholder table for view `cine`.`vista_general_salas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine`.`vista_general_salas` (`sala_id` INT, `nombre` INT, `capacidad` INT, `estado` INT);

-- -----------------------------------------------------
-- Placeholder table for view `cine`.`vista_general_ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine`.`vista_general_ventas` (`venta_id` INT, `cliente_id` INT, `pelicula_id` INT, `horario_id` INT, `fecha_venta` INT, `asiento_id` INT);

-- -----------------------------------------------------
-- View `cine`.`vista_general_asientos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cine`.`vista_general_asientos`;
USE `cine`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `cine`.`vista_general_asientos` AS select `cine`.`asientos`.`asiento_id` AS `asiento_id`,`cine`.`asientos`.`numero_asiento` AS `numero_asiento`,`cine`.`asientos`.`seccion` AS `seccion`,`cine`.`asientos`.`sala_id` AS `sala_id`,`cine`.`asientos`.`estado` AS `estado`,`cine`.`asientos`.`horario_id` AS `horario_id` from `cine`.`asientos`;

-- -----------------------------------------------------
-- View `cine`.`vista_general_clientes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cine`.`vista_general_clientes`;
USE `cine`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `cine`.`vista_general_clientes` AS select `cine`.`clientes`.`cliente_id` AS `cliente_id`,`cine`.`clientes`.`nombre` AS `nombre`,`cine`.`clientes`.`apellido` AS `apellido`,`cine`.`clientes`.`correo` AS `correo`,`cine`.`clientes`.`documento` AS `documento` from `cine`.`clientes`;

-- -----------------------------------------------------
-- View `cine`.`vista_general_horarios`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cine`.`vista_general_horarios`;
USE `cine`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `cine`.`vista_general_horarios` AS select `cine`.`horarios`.`horario_id` AS `horario_id`,`cine`.`horarios`.`pelicula_id` AS `pelicula_id`,`cine`.`horarios`.`sala_id` AS `sala_id`,`cine`.`horarios`.`fecha` AS `fecha` from `cine`.`horarios`;

-- -----------------------------------------------------
-- View `cine`.`vista_general_peliculas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cine`.`vista_general_peliculas`;
USE `cine`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `cine`.`vista_general_peliculas` AS select `cine`.`peliculas`.`pelicula_id` AS `pelicula_id`,`cine`.`peliculas`.`titulo` AS `titulo`,`cine`.`peliculas`.`genero` AS `genero`,`cine`.`peliculas`.`duracion` AS `duracion`,`cine`.`peliculas`.`rating` AS `rating` from `cine`.`peliculas`;

-- -----------------------------------------------------
-- View `cine`.`vista_general_salas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cine`.`vista_general_salas`;
USE `cine`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `cine`.`vista_general_salas` AS select `cine`.`salas`.`sala_id` AS `sala_id`,`cine`.`salas`.`nombre` AS `nombre`,`cine`.`salas`.`capacidad` AS `capacidad`,`cine`.`salas`.`estado` AS `estado` from `cine`.`salas`;

-- -----------------------------------------------------
-- View `cine`.`vista_general_ventas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cine`.`vista_general_ventas`;
USE `cine`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `cine`.`vista_general_ventas` AS select `cine`.`ventas`.`venta_id` AS `venta_id`,`cine`.`ventas`.`cliente_id` AS `cliente_id`,`cine`.`ventas`.`pelicula_id` AS `pelicula_id`,`cine`.`ventas`.`horario_id` AS `horario_id`,`cine`.`ventas`.`fecha_venta` AS `fecha_venta`,`cine`.`ventas`.`asiento_id` AS `asiento_id` from `cine`.`ventas`;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
