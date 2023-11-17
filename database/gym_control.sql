-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-11-2023 a las 23:30:32
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gym_control`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria_productos`
--

CREATE TABLE `categoria_productos` (
  `id_categoria` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_productos`
--

CREATE TABLE `inventario_productos` (
  `id_productos` int(11) NOT NULL,
  `nombre` varchar(125) DEFAULT NULL,
  `id_categoria` int(11) DEFAULT NULL,
  `precio_compra` int(11) DEFAULT NULL,
  `precio_venta` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `imagen` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `membresias`
--

CREATE TABLE `membresias` (
  `id_membresia` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `tiempo_duracion` int(11) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operadores`
--

CREATE TABLE `operadores` (
  `usuario` varchar(50) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(30) NOT NULL,
  `cedula` varchar(16) NOT NULL,
  `telefono` varchar(16) NOT NULL,
  `correo` varchar(80) NOT NULL,
  `contrasena` varchar(128) NOT NULL,
  `rol` varchar(15) NOT NULL,
  `fecha_registro` datetime NOT NULL,
  `user_registro` varchar(15) NOT NULL,
  `estado` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `operadores`
--

INSERT INTO `operadores` (`usuario`, `nombre`, `apellido`, `cedula`, `telefono`, `correo`, `contrasena`, `rol`, `fecha_registro`, `user_registro`, `estado`) VALUES
('camilo01', 'Camilo', 'Castillo', '1007456213', '321458963', 'camilo@gmail.com', 'camilo1234', 'administrador', '2023-09-08 00:00:00', 'cristian', 'activo'),
('diego', 'Diego alberto', 'pinilla', '61619696', '61611611', 'jahash@gmail.com', '1234', 'entrenador', '2023-10-13 21:54:04', 'Camilo', 'activo'),
('juan', 'Juan', 'Posada', '5181961961', '499611515', 'juan@gmail.com', '1234', 'entrenador', '2023-10-13 00:00:00', 'Camilo', 'activo'),
('vanegas00', 'cristian', 'vanegas', '120052475', '3215586325', 'vanegas@gmail.com', 'vanegas123', 'super_admin', '2023-09-01 00:00:00', '', 'activo'),
('yefer', 'Yeffer', 'Cuesta', '6516169', '314752591', 'dwwcw@gmail.com', '1234', 'entrenador', '2023-10-16 16:12:29', 'Camilo', 'activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_usuarios`
--

CREATE TABLE `registro_usuarios` (
  `cedula` varchar(16) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `fecha_nac` date NOT NULL,
  `telefono` varchar(16) NOT NULL,
  `correo` varchar(80) NOT NULL,
  `tarjeta_nfc` varchar(255) NOT NULL,
  `id_membresia` int(11) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_vencimiento` date NOT NULL,
  `fecha_registro` date NOT NULL,
  `user_registro` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria_productos`
--
ALTER TABLE `categoria_productos`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Indices de la tabla `inventario_productos`
--
ALTER TABLE `inventario_productos`
  ADD PRIMARY KEY (`id_productos`),
  ADD KEY `fk_categoria_productos` (`id_categoria`);

--
-- Indices de la tabla `membresias`
--
ALTER TABLE `membresias`
  ADD PRIMARY KEY (`id_membresia`);

--
-- Indices de la tabla `operadores`
--
ALTER TABLE `operadores`
  ADD PRIMARY KEY (`usuario`);

--
-- Indices de la tabla `registro_usuarios`
--
ALTER TABLE `registro_usuarios`
  ADD PRIMARY KEY (`cedula`),
  ADD KEY `fk_membresia` (`id_membresia`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categoria_productos`
--
ALTER TABLE `categoria_productos`
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inventario_productos`
--
ALTER TABLE `inventario_productos`
  MODIFY `id_productos` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `membresias`
--
ALTER TABLE `membresias`
  MODIFY `id_membresia` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `inventario_productos`
--
ALTER TABLE `inventario_productos`
  ADD CONSTRAINT `fk_categoria_productos` FOREIGN KEY (`id_categoria`) REFERENCES `categoria_productos` (`id_categoria`);

--
-- Filtros para la tabla `registro_usuarios`
--
ALTER TABLE `registro_usuarios`
  ADD CONSTRAINT `fk_membresia` FOREIGN KEY (`id_membresia`) REFERENCES `membresias` (`id_membresia`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
