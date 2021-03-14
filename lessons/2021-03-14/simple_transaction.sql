-- start transaction
START TRANSACTION;
-- make a savepoint before any actions
SAVEPOINT sp_1;
-- make insert into table
INSERT INTO stories (story, author) VALUES ('Fine day for a walk', 2);
-- check the result in db
SELECT * FROM stories;
-- do a rollback
ROLLBACK TO sp_1;
-- end transaction
COMMIT;
-- additionally run SELECT .. to check what's the content
-- added entry within transaction shouldn't be there