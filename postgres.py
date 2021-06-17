CREATE DATABASE noteapp;
CREATE TABLE users (id INTEGER PRIMARY KEY,
username VARCHAR,
password VARCHAR,
first_name VARCHAR,
last_name VARCHAR,
active BOOLEAN,
added_on TIMESTAMP, 
last_active TIMESTAMP);

CREATE TABLE note(id INTEGER PRIMARY KEY,
created_by INTEGER,
title VARCHAR,
note VARCHAR,
created_on TIMESTAMP, 
last_update TIMESTAMP);
