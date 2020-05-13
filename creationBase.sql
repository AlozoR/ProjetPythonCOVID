create schema covid;

USE covid;

create user 'testuser'@'localhost' IDENTIFIED BY 'testuser';

grant all privileges on covid.* to 'testuser'@'localhost';

