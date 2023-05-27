-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 14 Jan 2023 pada 04.17
-- Versi server: 10.4.11-MariaDB
-- Versi PHP: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `uasparkirdb`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES
(1, 'Ardian', 'admin@gmail.com', '$2b$12$kKSmd.YguqXPSppGjLja1OVHfNEBS0df8.eAuAZqe6wfU2ZiREEXG'),
(2, 'Ahmad', '123@gmail.com', '$2b$12$yVplB./Oz3/Qc25vL/yV9O25Q5QgOXVptJ2JMzSG7EK/yqCRBQ.na'),
(3, 'Yanto', 'yanto@gmail.com', '$2b$12$3bGYGd4YLVd7dD9AyAqmceBEjbc5MWbMS8Cgv5TpWoLgoLgEMjPru'),
(4, 'Fajar', 'fajar@gmail.com', '$2b$12$laxCVWD9RDYXQY7kheJy8OA0rTejxv4497s6DyyeL.7PG7M5KZXaC'),
(5, 'fika', 'fikanurhasari031@gmail.com', '$2b$12$wA138BRoqPXFHsvay9eMTOqGNTJ6J.qT6/ujJ4zp1r4it8uwuoSA6'),
(6, 'ayik', 'ayik@gmail.com', '$2b$12$em4kvzSgw6ZjG8EH2xBPQ.kUESM9qX8Er3sqsLckjHPTBsiFq/bs2');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
