-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- 主机: 127.0.0.1
-- 生成日期: 2013 年 11 月 13 日 16:19
-- 服务器版本: 5.5.27
-- PHP 版本: 5.3.16

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `movie`
--

-- --------------------------------------------------------

--
-- 表的结构 `crawler`
--

CREATE TABLE IF NOT EXISTS `crawler` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `movie_id` int(11) NOT NULL,
  `source_url` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3942 ;

-- --------------------------------------------------------

--
-- 表的结构 `movies`
--

CREATE TABLE IF NOT EXISTS `movies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alias_name` varchar(255) NOT NULL,
  `zh_name` varchar(255) NOT NULL,
  `en_name` varchar(255) NOT NULL,
  `director` varchar(255) NOT NULL,
  `tv_host` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `dubber` varchar(255) NOT NULL,
  `actor` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `movie_type` varchar(128) NOT NULL,
  `first_run` varchar(255) NOT NULL,
  `vido_type` varchar(64) NOT NULL,
  `lauange` varchar(64) NOT NULL,
  `total_parts` varchar(64) NOT NULL,
  `desc` text NOT NULL,
  `cover_image` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3942 ;

-- --------------------------------------------------------

--
-- 表的结构 `sources`
--

CREATE TABLE IF NOT EXISTS `sources` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `movie_id` int(11) NOT NULL,
  `sort` int(11) NOT NULL,
  `url` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=16679 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
