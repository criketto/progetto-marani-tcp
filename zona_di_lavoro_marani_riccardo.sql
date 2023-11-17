-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Creato il: Nov 17, 2023 alle 10:19
-- Versione del server: 5.7.40-0ubuntu0.18.04.1
-- Versione PHP: 7.2.24-0ubuntu0.18.04.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5ATepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `zona_di_lavoro_marani_riccardo`
--

CREATE TABLE `zona_di_lavoro_marani_riccardo` (
  `id_zona` int(11) NOT NULL,
  `nome_zona` varchar(100) NOT NULL,
  `numero_clienti` varchar(1024) NOT NULL,
  `id_dipendente` varchar(100) NOT NULL,
  `ore_di_lavoro_giornaliere` int(24) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `zona_di_lavoro_marani_riccardo`
--

INSERT INTO `zona_di_lavoro_marani_riccardo` (`id_zona`, `nome_zona`, `numero_clienti`, `id_dipendente`, `ore_di_lavoro_giornaliere`) VALUES
(1, 'correggio', '123', '1', 12),
(2, 'sammartino', '100', '2', 10);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `zona_di_lavoro_marani_riccardo`
--
ALTER TABLE `zona_di_lavoro_marani_riccardo`
  ADD PRIMARY KEY (`id_zona`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `zona_di_lavoro_marani_riccardo`
--
ALTER TABLE `zona_di_lavoro_marani_riccardo`
  MODIFY `id_zona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
