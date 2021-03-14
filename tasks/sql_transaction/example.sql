-- either use db prefix or use USE db
USE sda_book;
-- start transaction
START TRANSACTION;
-- make savepoint
SAVEPOINT pikachu;
-- delete all entries for rating from 3.2 to 4.2
-- disable the safe mode preference before and restart app
-- Edit -> Preferences -> SQL Editor (at the end that's the checkbox, uncheck it and restart Workbench)
DELETE FROM stories WHERE rating BETWEEN 3.2 AND 4.2;
-- make second savepoint
SAVEPOINT bulbasaur;
-- insert entry (doesn't matter) add rating as 3.5
INSERT INTO stories (story, author, rating) VALUES ('C is not bad', 3, 3.5);
-- make savepoint
SAVEPOINT squirtle;
-- update all entries starting with C (try using REGEXP not LIKE, I know you already are familiar with second one)
UPDATE stories SET story = 'Hasekll is great' WHERE story REGEXP '^[C]'; 
-- commit
COMMIT;
-- check result
SELECT * FROM stories;