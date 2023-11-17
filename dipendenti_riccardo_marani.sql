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
-- Struttura della tabella `dipendenti_riccardo_marani`
--

CREATE TABLE `dipendenti_riccardo_marani` (
  `id_dipendente` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cognome` varchar(100) NOT NULL,
  `indirizzo` varchar(100) NOT NULL,
  `posizione_lavorativa` varchar(100) NOT NULL,
  `data_assunzione` date NOT NULL,
  `data_nascita` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `dipendenti_riccardo_marani`
--

INSERT INTO `dipendenti_riccardo_marani` (`id_dipendente`, `nome`, `cognome`, `indirizzo`, `posizione_lavorativa`, `data_assunzione`, `data_nascita`) VALUES
(1, 'riccardo', 'marani', 'viadallep', 'dipendente', '2000-12-22', '1980-12-22');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `dipendenti_riccardo_marani`
--
ALTER TABLE `dipendenti_riccardo_marani`
  ADD PRIMARY KEY (`id_dipendente`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `dipendenti_riccardo_marani`
--
ALTER TABLE `dipendenti_riccardo_marani`
  MODIFY `id_dipendente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
