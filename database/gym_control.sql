-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-04-2024 a las 22:41:47
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
-- Estructura de tabla para la tabla `contacto_gym`
--

CREATE TABLE `contacto_gym` (
  `id` int(11) NOT NULL,
  `nombre_gym` varchar(50) DEFAULT NULL,
  `telefono_gym` varchar(10) DEFAULT NULL,
  `correo_gym` varchar(65) DEFAULT NULL,
  `direccion_gym` varchar(50) DEFAULT NULL,
  `barrio_gym` varchar(50) DEFAULT NULL,
  `hubicacion_gym` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `contacto_gym`
--

INSERT INTO `contacto_gym` (`id`, `nombre_gym`, `telefono_gym`, `correo_gym`, `direcion_gym`, `barrio_gym`, `hubicacion_gym`) VALUES
(1, 'ACROPOLIS', '3226836027', 'samaileen1503@gmail.com', 'carrera 25 #30-23', 'salesianos', 'tulua valle');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `creador_rutina`
--

CREATE TABLE `creador_rutina` (
  `id_rutina` int(11) NOT NULL,
  `duracion` varchar(25) DEFAULT NULL,
  `descripcion` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `creador_rutina`
--

INSERT INTO `creador_rutina` (`id_rutina`, `duracion`, `descripcion`) VALUES
(1, '05/10/2024', 'prueba'),
(2, '05/10/2024', 'prueba2'),
(5, '2024-04-25', 'esta locura');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ejercicios`
--

CREATE TABLE `ejercicios` (
  `contador_ejercicio` int(11) NOT NULL,
  `nombre_ejercicio` varchar(25) DEFAULT NULL,
  `repeciones` int(11) DEFAULT NULL,
  `series` int(11) DEFAULT NULL,
  `tipo` int(11) DEFAULT NULL,
  `img` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ejercicios`
--

INSERT INTO `ejercicios` (`contador_ejercicio`, `nombre_ejercicio`, `repeciones`, `series`, `tipo`, `img`) VALUES
(1, 'banco plano', 5, 10, 1, 'https://diariomelilla.com/wp-content/uploads/2022/01/press-de-banca-con-barra.jpg'),
(2, 'apetura mancuarela', 10, 5, 1, 'https://i.pinimg.com/236x/f6/fb/1c/f6fb1cc581a0ea4c2fc81d7229d8b346.jpg'),
(3, 'banco inclinado', 10, 8, 1, 'https://www.getpersonalgrowth.com/images/posts/9d8a1c914f42a913e55e2542b7650474-0.jpg'),
(4, 'flexiones', 5, 10, 3, 'https://prixz.com/salud/wp-content/uploads/2021/04/lagartijas2-300x175.png'),
(5, 'pull over', 10, 5, 2, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTov0oNLQjNpMF3HB6KcgxmNVH56v9qjR6hKVaKozg5dOz-6GSk6WrcmrcuJ8-MrgrfV8k&usqp=CAU'),
(6, 'flexion inclinada', 10, 5, 3, 'https://blogladiadoresfit.com/wp-content/uploads/2020/06/calistenia-flexiones-inclinadas.jpg'),
(12, 'prueba23', 4, 32, 3, 'Foto-20240419153826-.jpeg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ejercicio_rutina`
--

CREATE TABLE `ejercicio_rutina` (
  `ejercicio_rutina` int(11) NOT NULL,
  `id_rutina` int(11) DEFAULT NULL,
  `ejercicio` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ejercicio_rutina`
--

INSERT INTO `ejercicio_rutina` (`ejercicio_rutina`, `id_rutina`, `ejercicio`) VALUES
(1, 1, 1);

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
(4, 'Mensual', 30, 60000, 'activo'),
(5, 'personalizada', 30, 300000, 'activo'),
(6, 'Vencida', 0, 0, 'inactivo');

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
  `sexo` varchar(6) NOT NULL,
  `tipo_sangre` varchar(2) NOT NULL,
  `huella` varchar(500) NOT NULL,
  `nuemero_emergencia` int(16) NOT NULL,
  `correo` varchar(80) NOT NULL,
  `contrasena` varchar(50) NOT NULL,
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

INSERT INTO `registro_usuarios` (`cedula`, `nombre`, `apellido`, `fecha_nac`, `telefono`, `sexo`, `tipo_sangre`, `huella`, `nuemero_emergencia`, `correo`, `contrasena`, `tarjeta_nfc`, `id_membresia`, `fecha_inicio`, `fecha_vencimiento`, `fecha_registro`, `user_registro`, `estado`) VALUES
('10032165441', 'prueba', 'yeffer', '2013-10-16', '3216549876', 'hombre', 'A+', '', 321654789, 'yeferprueba1@gmail.com', 'prueba1', '', 6, '2024-03-01', '2024-03-14', '2024-03-01', 'yefer', 'inactivo'),
('1003699989', 'Carlos Alberto', 'Posada', '2008-02-14', '3152085189', 'hombre', 'AB', 'NULL', 2147483647, 'lokobrs@gmail.com', '0202020202', '10', 4, '2024-02-24', '2024-04-24', '2024-02-24', 'cristian', 'activo'),
('1007412611', 'Camilo', 'Castillo', '2001-11-24', '3172509264', '', '', '', 0, 'horuxjcc@gmail.com', '', '126196196962', 6, '0000-00-00', '2024-03-12', '2023-11-19', 'Camilo', 'inactivo'),
('1193592038', 'cristian', 'vanegas', '2003-10-28', '3152085189', '', '', '', 0, 'pequeflow-2003@hotmail.com', '', '01', 6, '0000-00-00', '2024-03-27', '2023-12-03', 'cristian', 'inactivo'),
('16161', 'camilo', 'castillo', '2001-11-24', '56944194', '', '', '', 0, 'yefer155@gmail.com', '', '255626', 6, '2023-10-11', '2023-11-11', '2023-10-11', 'camilo', 'inactivo'),
('232312222', 'alfonzo', 'alquaeda', '2008-02-21', '1222222222', 'hombre', 'AB', 'NULL', 2147483647, '12222222@nxjskdacns.com', '232312222', '25', 6, '2024-02-25', '2024-02-27', '2024-02-25', 'cristian', 'inactivo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rutina_cliente`
--

CREATE TABLE `rutina_cliente` (
  `id_rutina` int(11) DEFAULT NULL,
  `cliente` varchar(25) DEFAULT NULL,
  `dia` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rutina_cliente`
--

INSERT INTO `rutina_cliente` (`id_rutina`, `cliente`, `dia`) VALUES
(NULL, '1007412611', '23/04/2024'),
(1, '10032165441', '23/04/2024'),
(1, '16161', '23/04/2024'),
(1, '1003699989', '2024-04-30'),
(1, '1003699989', '2024-05-01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos_entrenamiento`
--

CREATE TABLE `tipos_entrenamiento` (
  `id_tipo` int(11) NOT NULL,
  `tipo_entrenamiento` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipos_entrenamiento`
--

INSERT INTO `tipos_entrenamiento` (`id_tipo`, `tipo_entrenamiento`) VALUES
(1, 'Resistencia'),
(2, 'Agilidad'),
(3, 'Potencia'),
(6, 'Fuerza');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria_productos`
--
ALTER TABLE `categoria_productos`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Indices de la tabla `contacto_gym`
--
ALTER TABLE `contacto_gym`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `creador_rutina`
--
ALTER TABLE `creador_rutina`
  ADD PRIMARY KEY (`id_rutina`);

--
-- Indices de la tabla `ejercicios`
--
ALTER TABLE `ejercicios`
  ADD PRIMARY KEY (`contador_ejercicio`),
  ADD KEY `tipo` (`tipo`);

--
-- Indices de la tabla `ejercicio_rutina`
--
ALTER TABLE `ejercicio_rutina`
  ADD PRIMARY KEY (`ejercicio_rutina`),
  ADD KEY `id_rutina` (`id_rutina`),
  ADD KEY `ejercicio` (`ejercicio`);

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
-- Indices de la tabla `rutina_cliente`
--
ALTER TABLE `rutina_cliente`
  ADD KEY `id_rutina` (`id_rutina`),
  ADD KEY `cliente` (`cliente`);

--
-- Indices de la tabla `tipos_entrenamiento`
--
ALTER TABLE `tipos_entrenamiento`
  ADD PRIMARY KEY (`id_tipo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categoria_productos`
--
ALTER TABLE `categoria_productos`
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `contacto_gym`
--
ALTER TABLE `contacto_gym`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `creador_rutina`
--
ALTER TABLE `creador_rutina`
  MODIFY `id_rutina` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `ejercicios`
--
ALTER TABLE `ejercicios`
  MODIFY `contador_ejercicio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `ejercicio_rutina`
--
ALTER TABLE `ejercicio_rutina`
  MODIFY `ejercicio_rutina` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
  MODIFY `id_membresia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `tipos_entrenamiento`
--
ALTER TABLE `tipos_entrenamiento`
  MODIFY `id_tipo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ejercicios`
--
ALTER TABLE `ejercicios`
  ADD CONSTRAINT `ejercicios_ibfk_1` FOREIGN KEY (`tipo`) REFERENCES `tipos_entrenamiento` (`id_tipo`);

--
-- Filtros para la tabla `ejercicio_rutina`
--
ALTER TABLE `ejercicio_rutina`
  ADD CONSTRAINT `ejercicio_rutina_ibfk_1` FOREIGN KEY (`id_rutina`) REFERENCES `creador_rutina` (`id_rutina`),
  ADD CONSTRAINT `ejercicio_rutina_ibfk_2` FOREIGN KEY (`ejercicio`) REFERENCES `ejercicios` (`contador_ejercicio`);

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

--
-- Filtros para la tabla `rutina_cliente`
--
ALTER TABLE `rutina_cliente`
  ADD CONSTRAINT `rutina_cliente_ibfk_1` FOREIGN KEY (`id_rutina`) REFERENCES `creador_rutina` (`id_rutina`),
  ADD CONSTRAINT `rutina_cliente_ibfk_2` FOREIGN KEY (`cliente`) REFERENCES `registro_usuarios` (`cedula`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
