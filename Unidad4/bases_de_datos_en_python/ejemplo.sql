-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 24-04-2021 a las 14:34:59
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ejemplo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carreras`
--

CREATE TABLE `carreras` (
  `id` int(2) NOT NULL,
  `codigo` varchar(5) NOT NULL,
  `carrera` varchar(50) NOT NULL,
  `creditos` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `carreras`
--

INSERT INTO `carreras` (`id`, `codigo`, `carrera`, `creditos`) VALUES
(1, '123', 'Ingeniería de SIstemas', '15'),
(2, '456', 'Economía', '16'),
(3, '789', 'Ingeniería electrónica', '20'),
(4, '111', 'Administración de empresas', '17'),
(5, '222', 'Licenciatura en Idiomas', '18'),
(6, '333', 'Contaduría Pública', '16'),
(7, '444', 'Ingeniería Mecánica', '21'),
(8, '555', 'Ingeniería Industrial', '20'),
(9, '666', 'Matemáticas', '21'),
(10, '777', 'Física', '21');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id` int(5) NOT NULL,
  `documento` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `genero` int(2) NOT NULL,
  `edad` int(3) NOT NULL,
  `carrera` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`id`, `documento`, `nombre`, `apellido`, `genero`, `edad`, `carrera`) VALUES
(1, '1122334455', 'Pepito', 'Pérez Paez', 1, 26, 789),
(2, '1234567890', 'Juana', 'De Arco', 2, 16, 456),
(3, '3654328907', 'Andrés Felipe', 'Contreras Arango', 1, 45, 111),
(4, '9807806543', 'Maria Camila', 'Molano', 2, 26, 333),
(5, '1230984567', 'Andrea', 'Muñoz Arango', 2, 34, 666),
(6, '1002347654', 'Mateo', 'Castro Vásquez', 1, 31, 777),
(7, '8203456', 'Gabriel Jaime', 'Gallego Vásquez', 1, 38, 789),
(8, '1000298764', 'María Cecilia', 'Martínez', 2, 56, 444),
(9, '43567890', 'Isabel Critina', 'Estrada', 2, 32, 123),
(10, '70987654', 'Armando', 'Martínez Pérez', 1, 45, 222);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carreras`
--
ALTER TABLE `carreras`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `carreras`
--
ALTER TABLE `carreras`
  MODIFY `id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
