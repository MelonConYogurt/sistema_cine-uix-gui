-- MySQL Script generated by MySQL Workbench
-- Mon Jul 15 18:00:37 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cine_pruebas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cine_pruebas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cine_pruebas` DEFAULT CHARACTER SET utf8 ;
USE `cine_pruebas` ;

-- -----------------------------------------------------
-- Table `cine_pruebas`.`peliculas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine_pruebas`.`peliculas` (
  `movie_id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NULL,
  `genero` VARCHAR(45) NULL,
  `duracion` VARCHAR(45) NULL,
  `ratin` INT NULL DEFAULT 0,
  PRIMARY KEY (`movie_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cine_pruebas`.`salas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine_pruebas`.`salas` (
  `sala_id` INT NOT NULL AUTO_INCREMENT,
  `sitio` VARCHAR(45) NULL,
  `estado` TINYINT NULL,
  PRIMARY KEY (`sala_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cine_pruebas`.`asientos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine_pruebas`.`asientos` (
  `asientos_id` INT NOT NULL AUTO_INCREMENT,
  `numero_asiento` INT NULL,
  `seccion_asiento` VARCHAR(45) NULL,
  `estado_asiento` TINYINT NULL,
  PRIMARY KEY (`asientos_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cine_pruebas`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine_pruebas`.`clientes` (
  `cliente_id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
  PRIMARY KEY (`cliente_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cine_pruebas`.`ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cine_pruebas`.`ventas` (
  `venta_id` INT NOT NULL AUTO_INCREMENT,
  `cliente_id` INT NULL,
  `numero_asiento` INT NULL,
  `pelicula_id` INT NULL,
  `sala_id` VARCHAR(45) NULL,
  `fecha_venta` DATE NULL,
  PRIMARY KEY (`venta_id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
