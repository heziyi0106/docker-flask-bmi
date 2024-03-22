CREATE DATABASE IF NOT EXISTS `docker_flask` DEFAULT CHARACTER SET utf8;
USE `docker_flask`;

DROP TABLE IF EXISTS `user_bmi`;

CREATE TABLE `user_bmi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `height` float NOT NULL,
  `weight` float NOT NULL,
  `bmi` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `site_visits`;

CREATE TABLE `site_visits` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `visit_count` int(11) DEFAULT 0
);


INSERT INTO `user_bmi` (`id`, `height`, `weight`, `bmi`) VALUES 
(3, 123, 12, 7.93),
(4, 123, 24, 15.86),
(5, 123, 23, 15.2),
(6, 123, 23, 15.2),
(7, 46, 32, 151.23),
(8, 168, 80, 28.34),
(9, 168, 80, 28.34),
(10, 124, 2, 1.3),
(11, 123, 21, 13.88),
(12, 123, 42, 27.76);
