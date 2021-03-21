-- create user for app with limited grants/privileges
CREATE USER 'cinemadb'@'localhost' IDENTIFIED BY 'cinema123!';
GRANT CREATE, INSERT, SELECT, DROP ON *.* TO 'cinemadb'@'localhost';
GRANT REFERENCES ON *.* TO 'cinemadb'@'localhost';
FLUSH PRIVILEGES;