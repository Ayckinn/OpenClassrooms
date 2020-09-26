SET NAMES utf8mb4;

-- CREATE AND USE DATABASE --
CREATE DATABASE IF NOT EXISTS openfoodfacts;
USE openfoodfacts;

-- CHECK AND AND REMOVE IF TABLES EXIST --
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS favorite;


-- CREATE CATEGORIES TABLES --
CREATE TABLE category (
  	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  	Name VARCHAR(300) NOT NULL,
  	URL TEXT,
  	PRIMARY KEY (ID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;


-- CREATE PRODUCTS TABLE --
CREATE TABLE product (
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	Name VARCHAR(300) NULL,
 	Brand VARCHAR(80) NULL,
 	Nutriscore CHAR(1) NULL,
 	URL TEXT,
 	Category_id SMALLINT UNSIGNED NOT NULL,
	PRIMARY KEY (ID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;


-- CREATE FAVORITES TABLE --
CREATE TABLE favorite (
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	product_id SMALLINT NOT NULL,
	Add_date DATETIME NOT NULL,
	PRIMARY KEY (ID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
