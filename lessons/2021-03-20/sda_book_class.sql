-- this is one line comment

/*
	this is multiline comment
*/

DROP DATABASE IF EXISTS sda_book;
CREATE DATABASE sda_book;

-- system user for app
DROP USER IF EXISTS 'sda_user'@'localhost';
CREATE USER 'sda_user'@'localhost' IDENTIFIED BY 'qwerty123';
-- grant SELECT, INSERT and UPDATE permissions for both DB
GRANT SELECT, INSERT, UPDATE ON sda_book.* TO 'sda_user'@'localhost';
GRANT SELECT, INSERT, UPDATE ON sda_ads.* TO 'sda_user'@'localhost';
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
-- ALTER TABLE profiles ADD birth_date DATE NOT NULL DEFAULT CURRENT_DATE;

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
)
COMMENT 'passwords table';

INSERT INTO passwords (id, pass) VALUES (2, 'qwerty123');
INSERT INTO passwords (id, pass) VALUES (3, 'qwerty123');
INSERT INTO passwords (id, pass) VALUES (4, 'qwerty123');

CREATE TABLE stories(
	id INTEGER AUTO_INCREMENT,
    story VARCHAR(800) NOT NULL,
    author INTEGER NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rating DECIMAL(2,1),
    -- alternative to id INTEGER PRIMARY KEY AUTO_INCREMENT,
    CONSTRAINT pk_stories_id PRIMARY KEY(id),
    CONSTRAINT chk_rating CHECK(rating > 3.0)
); 

-- just for example of altering table
ALTER TABLE stories ADD revision INTEGER DEFAULT 1;

INSERT INTO stories (story, author, rating) VALUES
	('SQL is awesome', 2, 3.5),
    ('Python is awesome', 2, 4.5),
    ('Nice wather', 4, 3.1),
    ('C++ is awesome', 3, 4.1),
    ('C# is awesome', 7, 3.1),
    ('Java is awesome', 9, 4.5);
    
-- sda_ads DB created
DROP DATABASE IF EXISTS sda_ads;
CREATE DATABASE sda_ads;

-- switch to newly created db, to add tables there (not under the previous db)
USE sda_ads;

CREATE TABLE ads(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    category VARCHAR(10) NOT NULL,
    product VARCHAR(30) NOT NULL,
    active BOOLEAN DEFAULT FALSE,
    rating DECIMAL(2,1) NOT NULL
);

INSERT INTO ads (category, product, active, rating) VALUES 
	('cars', 'Mazda', TRUE, 3.1),
    ('travels', 'Ventspils', TRUE, 4.5),
    ('tv', 'Samsung', TRUE, 4.1);

-- material combined from 2021-03-20
-- switch back to sda_book
USE sda_book;

-- create indexing on table profiles for column username
CREATE INDEX profiles_on_username_index ON profiles(username);
-- indexing table is just like: SELECT username, id FROM profiles ORDER BY username ASC;

-- create VIEW for stories.story matching authors as profiles.username
CREATE VIEW story_authors AS
	SELECT story, username, rating FROM stories
    JOIN profiles ON author = profiles.id;

DELIMITER //

-- trigger to ++1 to revision, if story is updated
-- note, triggers are table specific, so applied for stories in this particular case
CREATE TRIGGER revision_tracker
BEFORE UPDATE ON stories
FOR EACH ROW
BEGIN
	SET NEW.revision = NEW.revision + 1; 
END//

-- procedure, create new profile, return id for newly created entry
-- usage: CALL create_profile('rambo', 'John Rambo', 35)
CREATE PROCEDURE create_profile(
	username_cf VARCHAR(10),
    name_cf VARCHAR(20),
    age_cf INTEGER
    )
BEGIN
    INSERT INTO profiles (username, name, age) VALUES (username_cf, name_cf, age_cf);
	SELECT last_insert_id() AS id;
END//

-- function, returns status based on rating
-- usage1: SELECT get_status(3.2)
-- usage2: SELECT story, rating, get_status(rating) AS status FROM stories;
-- important! these are called SQL UFD (user defined functions), don't mix with SQL server functions
CREATE FUNCTION get_status(rating DOUBLE)
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
	DECLARE status VARCHAR(20);
    IF rating > 4.0 THEN
		SET status = 'story teller';
    ELSE
		SET status = 'basic user';
	END IF;
    RETURN status;
END//

/*
-- alternative to upper SQL UDF function
SELECT story, rating, CASE
	WHEN rating > 4.0 THEN 'story teller' ELSE 'basic user'
	END AS status
FROM stories    
*/

DELIMITER ;