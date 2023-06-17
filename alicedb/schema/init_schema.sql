CREATE DATABASE IF NOT EXISTS alicedb;
USE alicedb;


CREATE TABLE IF NOT EXISTS protein (
    protein_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    sequence TEXT NOT NULL,
    id VARCHAR(32) NOT NULL UNIQUE,
    source VARCHAR(10) NOT NULL,
    organism VARCHAR(32) NOT NULL
);


CREATE TABLE IF NOT EXISTS mutation (
    mutation_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    sequence TEXT NOT NULL,
    protein_id VARCHAR(32) NOT NULL,
    mutation VARCHAR(150) NOT NULL,
    position TEXT NOT NULL,
    mutation_type TEXT NOT NULL,
    description TEXT NOT NULL
);