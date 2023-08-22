-- Setup Test database for the project 
-- create a new user in the localhost

-- Creates a test database "hbnb_test_db"
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user hbnb_test in the localhost
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all permissions on the hbnh_test_db on user hbnh_test
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant usage permission on performance_schema to user hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

