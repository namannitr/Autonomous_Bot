-- phpMyAdmin SQL Dump
-- version 4.2.12deb2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 30, 2015 at 07:07 PM
-- Server version: 5.6.24-0ubuntu2
-- PHP Version: 5.6.4-4ubuntu6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `eko_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `bank`
--

CREATE TABLE IF NOT EXISTS `bank` (
  `eko_id` text,
  `user_name` text,
  `balance` float DEFAULT NULL,
  `pin` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `id_link`
--

CREATE TABLE IF NOT EXISTS `id_link` (
  `whatsapp_id` varchar(50) DEFAULT NULL,
  `facebook_id` varchar(50) DEFAULT NULL,
  `twitter_id` varchar(50) DEFAULT NULL,
  `hike_id` varchar(50) DEFAULT NULL,
  `line_id` varchar(50) DEFAULT NULL,
  `eko_id` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `pending_request`
--

CREATE TABLE IF NOT EXISTS `pending_request` (
  `eko_id` varchar(100) DEFAULT NULL,
  `request` varchar(100) NOT NULL,
  `complete_flag` int(11) NOT NULL DEFAULT '0',
  `status_flag` int(11) NOT NULL DEFAULT '0',
  `time_stamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `received_message`
--

CREATE TABLE IF NOT EXISTS `received_message` (
`message_id` int(11) NOT NULL,
  `eko_id` text NOT NULL,
  `message_body` text,
  `message_source` int(11) NOT NULL,
  `message_type` int(11) NOT NULL,
  `message_status` int(11) NOT NULL,
  `time_stamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `response_message`
--

CREATE TABLE IF NOT EXISTS `response_message` (
  `message_id` int(11) NOT NULL,
  `eko_id` text NOT NULL,
  `message_body` text NOT NULL,
  `message_destination` int(11) NOT NULL,
  `message_type` int(11) NOT NULL,
  `message_state` int(11) NOT NULL DEFAULT '0',
  `time_stamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `id_link`
--
ALTER TABLE `id_link`
 ADD UNIQUE KEY `whatsapp_id` (`whatsapp_id`,`facebook_id`,`twitter_id`,`hike_id`,`line_id`,`eko_id`);

--
-- Indexes for table `received_message`
--
ALTER TABLE `received_message`
 ADD UNIQUE KEY `message_id` (`message_id`);

--
-- Indexes for table `response_message`
--
ALTER TABLE `response_message`
 ADD PRIMARY KEY (`message_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `received_message`
--
ALTER TABLE `received_message`
MODIFY `message_id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
