-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-02-2024 a las 01:55:04
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

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
  `nombre` varchar(100) DEFAULT NULL,
  `estado` varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categoria_productos`
--

INSERT INTO `categoria_productos` (`id_categoria`, `nombre`, `estado`) VALUES
(1, 'Creatina', 'activo'),
(3, 'Proteina', 'activo');

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
  `imagen` int(11) DEFAULT NULL,
  `estado` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inventario_productos`
--

INSERT INTO `inventario_productos` (`id_productos`, `nombre`, `id_categoria`, `precio_compra`, `precio_venta`, `cantidad`, `imagen`, `estado`) VALUES
(1, 'Legacy', 3, 55000, 80000, 5, NULL, 'activo'),
(2, 'BEST', 1, 50000, 90000, 10, NULL, 'activo'),
(3, 'alminoasidos a', 1, 150000, 260000, 260000, NULL, 'activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medidas`
--

CREATE TABLE `medidas` (
  `Id` int(11) NOT NULL,
  `cedula` varchar(16) NOT NULL,
  `user_registro` varchar(50) NOT NULL,
  `mes_registro` date NOT NULL,
  `peso_corporal` int(11) NOT NULL,
  `bicep_derecho` int(11) NOT NULL,
  `bicep_izquierdo` int(11) NOT NULL,
  `pecho` int(11) NOT NULL,
  `antebrazo_derecho` int(11) NOT NULL,
  `antebrazo_izquierdo` int(11) NOT NULL,
  `cintura` int(11) NOT NULL,
  `cadera` int(11) NOT NULL,
  `muslo_derecho` int(11) NOT NULL,
  `muslo_izquierdo` int(11) NOT NULL,
  `pantorrilla_derecha` int(11) NOT NULL,
  `pantorrilla_izquierda` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `medidas`
--

INSERT INTO `medidas` (`Id`, `cedula`, `user_registro`, `mes_registro`, `peso_corporal`, `bicep_derecho`, `bicep_izquierdo`, `pecho`, `antebrazo_derecho`, `antebrazo_izquierdo`, `cintura`, `cadera`, `muslo_derecho`, `muslo_izquierdo`, `pantorrilla_derecha`, `pantorrilla_izquierda`) VALUES
(1, '16161', 'dscsd', '2024-02-20', 222, 22, 22, 22, 222, 22, 22, 22, 22, 22, 22, 22),
(2, '1193592038', 'cristian', '2024-02-24', 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `membresias`
--

CREATE TABLE `membresias` (
  `id_membresia` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `tiempo_duracion` int(11) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `estado` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `membresias`
--

INSERT INTO `membresias` (`id_membresia`, `nombre`, `tiempo_duracion`, `precio`, `estado`) VALUES
(1, 'Diario', 1, 5000, 'activo'),
(2, 'Semanal', 6, 15000, 'activo'),
(3, 'Quincenal', 15, 30000, 'activo'),
(4, 'Mensual', 30, 60000, 'activo');

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
  `user_registro` varchar(15) NOT NULL,
  `estado` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `registro_usuarios`
--

INSERT INTO `registro_usuarios` (`cedula`, `nombre`, `apellido`, `fecha_nac`, `telefono`, `correo`, `tarjeta_nfc`, `id_membresia`, `fecha_inicio`, `fecha_vencimiento`, `fecha_registro`, `user_registro`, `estado`) VALUES
('1', 'dwwddw|', 'effff', '2001-11-24', '41515', 'ekfnfec@nkm.com', '5151558158', 1, '2023-11-19', '1999-01-10', '2023-11-19', 'Camilo', 'inactivo'),
('1007412611', 'Camilo', 'Castillo', '2001-11-24', '3172509264', 'horuxjcc@gmail.com', '126196196962', 4, '2023-11-19', '2023-12-19', '2023-11-19', 'Camilo', 'inactivo'),
('1193592038', 'cristian', 'vanegas', '2003-10-28', '3152085189', 'pequeflow-2003@hotmail.com', '01', 4, '2023-12-03', '2024-05-31', '2023-12-03', 'cristian', 'activo'),
('16161', 'camilo', 'castillo', '2001-11-24', '56944194', 'camilo@gmail.com', '255626', 2, '2023-10-11', '2023-11-11', '2023-10-11', 'camilo', 'inactivo'),
('21116969', 'cristian', 'vanegas', '2001-10-23', '41515', 'horuxjcc@gmail.com', '2162626', 1, '2023-11-19', '1999-01-10', '2023-11-19', 'Camilo', 'inactivo'),
('25252', 'cristian', 'vanegas', '2001-10-23', '41515', 'horuxjcc@gmail.com', '122622', 1, '2023-11-19', '1999-01-10', '2023-11-19', 'Camilo', 'inactivo'),
('45916126', 'Laura', 'Esguerra', '2003-12-08', '3210622652', 'laura@gmail.com', '116919611619612', 1, '2023-11-27', '2023-11-28', '2023-11-27', 'Camilo', 'inactivo'),
('62961112', 'cristian', 'vanegas', '2001-10-23', '141469419', 'cris@gmail.com', '541514514', 4, '2023-11-19', '1999-01-10', '2023-11-19', 'Camilo', 'inactivo');

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
-- Indices de la tabla `medidas`
--
ALTER TABLE `medidas`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `cedula` (`cedula`);

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
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `inventario_productos`
--
ALTER TABLE `inventario_productos`
  MODIFY `id_productos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `medidas`
--
ALTER TABLE `medidas`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `membresias`
--
ALTER TABLE `membresias`
  MODIFY `id_membresia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `inventario_productos`
--
ALTER TABLE `inventario_productos`
  ADD CONSTRAINT `fk_categoria_productos` FOREIGN KEY (`id_categoria`) REFERENCES `categoria_productos` (`id_categoria`);

--
-- Filtros para la tabla `medidas`
--
ALTER TABLE `medidas`
  ADD CONSTRAINT `medidas_ibfk_1` FOREIGN KEY (`cedula`) REFERENCES `registro_usuarios` (`cedula`);

--
-- Filtros para la tabla `registro_usuarios`
--
ALTER TABLE `registro_usuarios`
  ADD CONSTRAINT `fk_membresia` FOREIGN KEY (`id_membresia`) REFERENCES `membresias` (`id_membresia`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
