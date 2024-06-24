-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-06-2024 a las 14:49:50
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
  `id_contacto` int(11) NOT NULL,
  `nombre_gym` varchar(50) DEFAULT NULL,
  `telefono_gym` varchar(10) DEFAULT NULL,
  `correo_gym` varchar(65) DEFAULT NULL,
  `direccion_gym` varchar(50) DEFAULT NULL,
  `barrio_gym` varchar(50) DEFAULT NULL,
  `ubicacion_gym` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `contacto_gym`
--

INSERT INTO `contacto_gym` (`id_contacto`, `nombre_gym`, `telefono_gym`, `correo_gym`, `direccion_gym`, `barrio_gym`, `ubicacion_gym`) VALUES
(1, 'ACROPOLIS', '3226836027', 'samaileen1503@gmail.com', 'tulua valle', 'asnos', 'carrera 25 30 23as'),
(2, 'prueba', '321654462', 'prueba@gmail.com', 'bariro', 'jfbfjnfkjn', 'kjfkfbk'),
(3, 'pruebagymg', '3216549875', 'prueba@prueba.com', 'la salle', 'kdjfvnlksjjbvkljsbvkjb', ' bhdhfbvgjksbgkjfb'),
(4, 'power_hands', '321654879', 'prueba@prueba.com', 'dsfgerhtse', 'dfgshfhtfr', 'jgedjf'),
(5, 'aaaa', '3215465258', 'asa@gmail.com', 'aaaaaaa', 'aaaaa', 'aaaa'),
(6, 'aaaaaaaaaaaaaaaa', '4444444444', 'asa@gmail.com', 'aaaaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa'),
(7, 'aa', '2222222222', 'aaaaaaa@aaa', 'aaaaaaaaaaaaa', 'aaaaaaaaa', 'aaaaaaa'),
(8, 'a', '222', 'aaaaaaa@aaa', 'aaaa', 'aaaa', 'aaaa'),
(9, 'aaaaa', '122122121', 'asa@gmail.com', 'asaasas', 'asasas', 'aaaaaaaaaaaa'),
(10, 'aaaaaaaaaaaaaaaa', '3215465258', 'asa@gmail.com', 'aaaaaaa', 'asas', 'aaaaaaaaaaaa'),
(11, 'aaaaaaaaaa', '1111111111', 'asa@gmail.com', 'ascacasc acasc', 'casasa ascacsa', 'cali');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `creador_rutina`
--

CREATE TABLE `creador_rutina` (
  `id_rutina` int(11) NOT NULL,
  `duracion` varchar(25) DEFAULT NULL,
  `nombre` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `creador_rutina`
--

INSERT INTO `creador_rutina` (`id_rutina`, `duracion`, `nombre`) VALUES
(1, '05/10/2024', 'prueba'),
(2, '05/10/2024', 'prueba2'),
(5, '2024-04-25', 'esta locura'),
(6, '2024-06-04', 'asasasasasas');

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
(12, 'prueba23', 4, 32, 3, 'Foto-20240419153826-.jpeg'),
(13, 'aaaa', 2121, 121, 2, 'Foto-20240618173901-.png');

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
-- Estructura de tabla para la tabla `facturas`
--

CREATE TABLE `facturas` (
  `id_factura` varchar(20) NOT NULL,
  `fecha_registro` datetime NOT NULL,
  `creador` varchar(110) NOT NULL,
  `total_pago` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `facturas`
--

INSERT INTO `facturas` (`id_factura`, `fecha_registro`, `creador`, `total_pago`) VALUES
('16e3ef24786b', '2024-05-06 00:29:12', 'camilo01', 340000),
('1c1f0b768a1a', '2024-05-06 00:29:12', 'camilo01', 340000),
('63f3228a524a', '2024-05-06 00:28:44', 'camilo01', 340000),
('909526c25d35', '2024-05-06 00:28:44', 'camilo01', 340000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ingreso_usuarios`
--

CREATE TABLE `ingreso_usuarios` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `fecha_ingreso` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ingreso_usuarios`
--

INSERT INTO `ingreso_usuarios` (`id`, `id_usuario`, `fecha_ingreso`) VALUES
(2, 125155158, '2024-04-26 17:04:33'),
(3, 125155158, '2024-04-26 17:06:14'),
(4, 125155158, '2024-04-26 17:38:30'),
(5, 125155158, '2024-04-25 13:40:28'),
(6, 125155158, '2024-04-26 17:56:22'),
(7, 125155158, '2024-04-26 18:02:28'),
(8, 125155158, '2024-04-26 18:06:26'),
(9, 125155158, '2024-04-26 23:24:43'),
(10, 125155158, '2024-04-26 23:29:44'),
(11, 125155158, '2024-04-27 00:26:13'),
(12, 125155158, '2024-04-27 00:27:00'),
(13, 1007412611, '2024-04-27 00:27:48'),
(14, 1007412611, '2024-04-30 07:13:11'),
(15, 1007412611, '2024-04-30 07:16:44'),
(16, 2147483647, '2024-04-30 07:18:39'),
(17, 2147483647, '2024-04-30 07:19:27'),
(18, 1007412611, '2024-04-30 07:19:42'),
(19, 2147483647, '2024-04-30 07:19:53'),
(20, 2147483647, '2024-04-30 07:20:37'),
(21, 1007412611, '2024-04-30 07:23:14'),
(22, 1007412611, '2024-04-30 07:23:27'),
(23, 1007412611, '2024-04-30 07:23:36'),
(24, 1007412611, '2024-04-30 07:24:01');

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
  `Id_medidas` int(11) NOT NULL,
  `cedula` varchar(16) NOT NULL,
  `user_registro` varchar(50) NOT NULL,
  `mes_registro` datetime NOT NULL,
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

INSERT INTO `medidas` (`Id_medidas`, `cedula`, `user_registro`, `mes_registro`, `peso_corporal`, `bicep_derecho`, `bicep_izquierdo`, `pecho`, `antebrazo_derecho`, `antebrazo_izquierdo`, `cintura`, `cadera`, `muslo_derecho`, `muslo_izquierdo`, `pantorrilla_derecha`, `pantorrilla_izquierda`) VALUES
(1, '16161', 'dscsd', '2024-02-20 00:00:00', 222, 22, 22, 22, 222, 22, 22, 22, 22, 22, 22, 22),
(2, '1193592038', 'cristian', '2024-04-30 00:00:00', 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11),
(3, '16161', 'yefer', '2024-05-23 00:00:00', 100, 90, 40, 31, 13, 54, 75, 14, 22, 74, 84, 74),
(6, '10032165441', 'vanegas', '2024-06-12 16:35:57', 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20);

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
('camilo01', 'Camilo', 'Castillo', '1007456213', '321458963', 'camilo@gmail.com', '01defe492d2c21adb95134ef29cfb6a410c53d4ce0b71c0431f03ba1f7afc03327740a7d0a69ef507bf33db1e66e96c0c7306eb17e00246199f11b99e08684ae', 'administrador', '2023-09-08 00:00:00', 'cristian', 'activo'),
('diego', 'Diego alberto', 'pinilla', '61619696', '61611611', 'jahash@gmail.com', '1234', 'entrenador', '2023-10-13 21:54:04', 'Camilo', 'activo'),
('juan', 'Juan', 'Posada', '5181961961', '499611515', 'juan@gmail.com', '1234', 'entrenador', '2023-10-13 00:00:00', 'Camilo', 'activo'),
('prueba', 'prueba', 'prueba', '111111111111111', '1111111111', 'hola@gmail.com', 'e24a017aa47f2ff569d8d5cfedcfb0e5bfc914ea547fbb0757f419113edf47beaae7f22e2b2a4580ed76bc880d3812239b2f0af1bfa35c9203823d56b686b7c0', 'entrenador', '2024-06-11 18:05:08', 'cristian', 'activo'),
('vanegas00', 'cristian', 'vanegas', '120052475', '3215586325', 'vanegas@gmail.com', '6965c3d914f059e8b5dd6d0ca72366ccf2c5e5e544f3a3c3b21e72dfe5ebf03df440859f6d4f2ef8843721b0c40b791655a89422801eaaa072b6084df42d2045', 'super_admin', '2023-09-01 00:00:00', '', 'activo'),
('yefer', 'Yeffer', 'Cuesta', '6516169', '314752591', 'dwwcw@gmail.com', '1234', 'super_admin', '2023-10-16 16:12:29', 'Camilo', 'activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagos_productos`
--

CREATE TABLE `pagos_productos` (
  `id_pago` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `id_factura` varchar(20) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio_unidad` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pagos_productos`
--

INSERT INTO `pagos_productos` (`id_pago`, `id_producto`, `id_factura`, `cantidad`, `precio_unidad`) VALUES
(84, 1, '63f3228a524a', 1, 80000),
(85, 3, '909526c25d35', 1, 260000),
(86, 1, '16e3ef24786b', 1, 80000),
(87, 3, '1c1f0b768a1a', 1, 260000);

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
  `contrasena` varchar(200) NOT NULL,
  `leciones` varchar(2) NOT NULL,
  `id_membresia` int(11) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_vencimiento` date NOT NULL,
  `fecha_registro` date NOT NULL,
  `user_registro` varchar(15) NOT NULL,
  `estado` varchar(8) NOT NULL,
  `imagenuser` varchar(100) DEFAULT NULL,
  `codigo` int(6) NOT NULL,
  `leciones_descripcion` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `registro_usuarios`
--

INSERT INTO `registro_usuarios` (`cedula`, `nombre`, `apellido`, `fecha_nac`, `telefono`, `sexo`, `tipo_sangre`, `huella`, `nuemero_emergencia`, `correo`, `contrasena`, `leciones`, `id_membresia`, `fecha_inicio`, `fecha_vencimiento`, `fecha_registro`, `user_registro`, `estado`, `imagenuser`, `codigo`, `leciones_descripcion`) VALUES
('10032165441', 'pruebamedida', 'yeffer', '2013-10-16', '3216549877', 'hombre', 'A+', '', 321654789, 'yeferprueba2@gmail.com', '132f8f4459d4dcd768a432d143586f1c3a28ab6da0c66c3881204f625223bb910d75b1958b1c4d562dbc05a704729e67b6416a2a4070333b3338fe2c3f19c947', '', 6, '0000-00-00', '2024-04-30', '2024-03-01', 'yefer', 'inactivo', 'Foto-20240607215602.jpg', 0, ''),
('1003699989', 'Carlos Alberto', 'Posada', '2008-02-14', '3152085189', 'hombre', 'AB', 'NULL', 2147483647, 'lokobrs@gmail.com', '0202020202', '', 6, '2024-02-24', '2024-04-24', '2024-02-24', 'cristian', 'inactivo', NULL, 0, ''),
('1007412611', 'Camilo', 'Castillo', '2001-11-24', '3172509264', '', '', '', 0, 'horuxjcc@gmail.com', '', '', 6, '0000-00-00', '2024-03-12', '2023-11-19', 'Camilo', 'inactivo', NULL, 0, ''),
('1193592038', 'cristian', 'vanegas', '2003-10-28', '3152085189', '', '', '', 0, 'pequeflow-2003@hotmail.com', 'd9e6762dd1c8eaf6d61b3c6192fc408d4d6d5f1176d0c29169bc24e71c3f274ad27fcd5811b313d681f7e55ec02d73d499c95455b6b5bb503acf574fba8ffe85', '', 6, '0000-00-00', '2024-03-27', '2023-12-03', 'cristian', 'inactivo', NULL, 245692, ''),
('155555555555555', 'aaaaaaa', 'aaaaaaa', '2024-05-31', '1111111111', 'hombre', 'O+', 'NULL', 2147483647, 'cscscscs@gmail.com', '5ee14d3d6b45bf3d8dd1e25507b761c0e2c1f5c9051fe50d9eb0ee0b97a4743354f62bf77cd4ad044103981a0f9a64cbb09a8d2dc65138cfc7f3af88a6aa320d', 'si', 6, '2024-06-16', '2024-06-17', '2024-06-16', 'cristian', 'inactivo', NULL, 0, 'prueba'),
('16161', 'camilo', 'castillo', '2001-11-24', '56944194', '', '', '', 0, 'yefer155@gmail.com', 'prueba112', '', 6, '2023-10-11', '2023-11-11', '2023-10-11', 'camilo', 'inactivo', NULL, 0, ''),
('222222222', 'prueba', 'prueba', '1995-06-06', '3201544365', 'hombre', 'A+', 'NULL', 2147483647, 'hola@gmail.com', 'e24a017aa47f2ff569d8d5cfedcfb0e5bfc914ea547fbb0757f419113edf47beaae7f22e2b2a4580ed76bc880d3812239b2f0af1bfa35c9203823d56b686b7c0', '', 6, '2024-06-11', '2024-06-12', '2024-06-11', 'cristian', 'inactivo', NULL, 0, ''),
('232312222', 'alfonzo', 'alquaeda', '2008-02-21', '1222222222', 'hombre', 'AB', 'NULL', 2147483647, '12222222@nxjskdacns.com', '232312222', '', 6, '2024-02-25', '2024-02-27', '2024-02-25', 'cristian', 'inactivo', NULL, 0, ''),
('444444444444444', 'aaaaaaas', 'asasasa', '2024-06-04', '6666666666', 'hombre', 'A-', 'NULL', 1222222222, 'cscscq@gmail.com', 'bff34d4e7f654a4105e44630145731320dae0ffa7ebf12cf36afd908c42b4d0e67f51a2bd952e40ac6f02141a1198d1f7946ac219877e5499bbedc3f16a4d9f5', 'no', 6, '2024-06-16', '2024-06-17', '2024-06-16', 'cristian', 'inactivo', NULL, 0, 'no tiene leciones'),
('666666666666666', 'alberto', 'jose', '2024-06-20', '4444444444', 'hombre', 'O+', 'NULL', 2147483647, 'dada@gmail.com', 'cb0b4a73a5176053e6eb3766f5eabe2a9faad01e3a32adf077ba0bfc7b0a56be8996d1b12c33796569e464f33802fc7e873a606b37a46f6d56c7813c79314a7b', 'no', 6, '2024-06-12', '2024-06-13', '2024-06-12', 'cristian', 'inactivo', NULL, 0, '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rutina_cliente`
--

CREATE TABLE `rutina_cliente` (
  `id_rutina` int(11) DEFAULT NULL,
  `cliente` varchar(25) DEFAULT NULL,
  `dia` varchar(25) DEFAULT NULL,
  `contador_de_rutinas_clientes` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rutina_cliente`
--

INSERT INTO `rutina_cliente` (`id_rutina`, `cliente`, `dia`, `contador_de_rutinas_clientes`) VALUES
(NULL, '1007412611', '23/04/2024', 1),
(1, '10032165441', '23/04/2024', 2),
(1, '16161', '23/04/2024', 3),
(1, '1003699989', '2024-04-30', 4),
(1, '1003699989', '2024-05-01', 5),
(NULL, '1007412611', '23/04/2024', 6),
(1, '10032165441', '23/04/2024', 7),
(1, '16161', '23/04/2024', 8),
(1, '1003699989', '2024-04-30', 9),
(1, '1003699989', '2024-05-01', 10),
(NULL, '1007412611', '23/04/2024', 11),
(1, '10032165441', '23/04/2024', 12),
(1, '16161', '23/04/2024', 13),
(1, '1003699989', '2024-04-30', 14),
(1, '1003699989', '2024-05-01', 15),
(NULL, '1007412611', '23/04/2024', 16),
(1, '10032165441', '23/04/2024', 17),
(1, '16161', '23/04/2024', 18),
(1, '1003699989', '2024-04-30', 19),
(1, '1003699989', '2024-05-01', 20);

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
  ADD PRIMARY KEY (`id_contacto`);

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
-- Indices de la tabla `facturas`
--
ALTER TABLE `facturas`
  ADD PRIMARY KEY (`id_factura`);

--
-- Indices de la tabla `ingreso_usuarios`
--
ALTER TABLE `ingreso_usuarios`
  ADD PRIMARY KEY (`id`);

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
  ADD PRIMARY KEY (`Id_medidas`),
  ADD KEY `medidas_ibfk_1` (`cedula`);

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
-- Indices de la tabla `pagos_productos`
--
ALTER TABLE `pagos_productos`
  ADD PRIMARY KEY (`id_pago`);

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
  ADD PRIMARY KEY (`contador_de_rutinas_clientes`),
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
  MODIFY `id_contacto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `creador_rutina`
--
ALTER TABLE `creador_rutina`
  MODIFY `id_rutina` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `ejercicios`
--
ALTER TABLE `ejercicios`
  MODIFY `contador_ejercicio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `ejercicio_rutina`
--
ALTER TABLE `ejercicio_rutina`
  MODIFY `ejercicio_rutina` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `ingreso_usuarios`
--
ALTER TABLE `ingreso_usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `inventario_productos`
--
ALTER TABLE `inventario_productos`
  MODIFY `id_productos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `medidas`
--
ALTER TABLE `medidas`
  MODIFY `Id_medidas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `membresias`
--
ALTER TABLE `membresias`
  MODIFY `id_membresia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `rutina_cliente`
--
ALTER TABLE `rutina_cliente`
  MODIFY `contador_de_rutinas_clientes` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

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

--
-- Filtros para la tabla `rutina_cliente`
--
ALTER TABLE `rutina_cliente`
  ADD CONSTRAINT `rutina_cliente_ibfk_2` FOREIGN KEY (`id_rutina`) REFERENCES `creador_rutina` (`id_rutina`),
  ADD CONSTRAINT `rutina_cliente_ibfk_3` FOREIGN KEY (`cliente`) REFERENCES `registro_usuarios` (`cedula`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
