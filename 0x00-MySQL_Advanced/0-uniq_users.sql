-- Create Table
CREATE TABLE users IF NOT EXISTS
(id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255))
