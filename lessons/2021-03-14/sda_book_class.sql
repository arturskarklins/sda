-- this is one line comment

/*
	this is multiline comment
*/

DROP DATABASE IF EXISTS sda_book;
CREATE DATABASE sda_book;

-- system user for app
DROP USER IF EXISTS 'sda_user'@'localhost';
CREATE USER 'sda_user'@'localhost' IDENTIFIED BY 'qwerty123';
GRANT SELECT, INSERT, UPDATE ON sda_book.* TO 'sda_user'@'localhost';
-- remove UPDATE grant/permission
-- REVOKE UPDATE ON sda_book.* FROM 'sda_user'@'localhost';

USE sda_book;

CREATE TABLE profiles( 
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(10) NOT NULL UNIQUE,
    name VARCHAR(20) NOT NULL,
    age INTEGER NOT NULL,
    birth_date DATE
);

-- add to profiles birth_date DATE, NOT NULL
-- ALTER TABLE profiles ADD birth_date DATE NOT NULL DEFAULT '2021-03-13';

INSERT INTO profiles (username, name, age) VALUES ('bob', 'Bob', 45);
INSERT INTO profiles (name, username, age) VALUES ('Anna', 'anna', 23);
INSERT INTO profiles (name, username, age, birth_date) VALUES 
	('Tom', 'tom', 55, '2001-1-9'), 
    ('Tim', 'tim', 34, '1998-8-23'), 
    ('Geroge', 'george', 78, '2001-10-12');

CREATE TABLE passwords(
	id INTEGER UNIQUE,
    pass VARCHAR(20) NOT NULL,
    CONSTRAINT fk_pass_to_user FOREIGN KEY(id) REFERENCES profiles(id)
);

INSERT INTO passwords (id, pass) VALUES (2, 'qwerty123');
INSERT INTO passwords (id, pass) VALUES (3, 'qwerty123');
INSERT INTO passwords (id, pass) VALUES (4, 'qwerty123');


-- inner join
-- SELECT profiles.id AS profile_id, username, pass FROM profiles 
-- JOIN passwords ON profiles.id = passwords.id

-- SELECT pr.id AS profile_id, username, pass FROM profiles pr
-- JOIN passwords pa USING(id)

-- SELECT pr.id AS profile_id, username, pass FROM profiles pr
-- NATURAL JOIN passwords pa

-- generate report users and their passwords: id, username, password where pass null
-- profiles under sda_book.profiles and passwords sda_book_passwords

-- INNER JOIN: default -> JOIN
-- OUTER JOIN: LEFT and RIGHT JOIN

-- SELECT pr.id, username, pass
-- FROM profiles pr
-- LEFT JOIN passwords pa
-- ON pr.id = pa.id