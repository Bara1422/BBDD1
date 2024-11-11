DROP TABLE IF EXISTS Radio;
DROP TABLE IF EXISTS PROGRAMA;

CREATE TABLE `PROGRAMA` (
  `radio` varchar(255),
  `programa` varchar(255),
  `año` integer,
  `conductor` varchar(255) not null,
  PRIMARY KEY (`radio`, `programa`, `año`),
  KEY `index_radio_año` (`radio`, `año`)
);

CREATE TABLE `Radio` (
  `radio` varchar(255),
  `año` integer,
  `frecuencia_radio` double not null,
  `gerente` varchar(255) not null,
  PRIMARY KEY (`radio`, `año`),
  FOREIGN KEY (`radio`, `año`) REFERENCES `PROGRAMA`(`radio`, `año`) 
	ON DELETE CASCADE 
    ON UPDATE CASCADE
);