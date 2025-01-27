-- Switch to the NeuroSymbolicTABQA database
USE NeuroSymbolicTABQA;

-- Drop tables if they exist
DROP TABLE IF EXISTS PersonalInformation;
DROP TABLE IF EXISTS Medal;
DROP TABLE IF EXISTS Format;
DROP TABLE IF EXISTS Tournament;
DROP TABLE IF EXISTS Athlete;


CREATE TABLE Athlete (
    athlete_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE Tournament (
    tournament_id INT AUTO_INCREMENT PRIMARY KEY,
    athlete_id INT,
    name VARCHAR(100) NOT NULL,
    FOREIGN KEY (athlete_id) REFERENCES Athlete(athlete_id)
);

CREATE TABLE Format (
    format_id INT AUTO_INCREMENT PRIMARY KEY,
    tournament_id INT,
    name VARCHAR(100) NOT NULL,
    FOREIGN KEY (tournament_id) REFERENCES Tournament(tournament_id)
);

CREATE TABLE Medal (
    medal_id INT AUTO_INCREMENT PRIMARY KEY,
    format_id INT,
    type VARCHAR(50) NOT NULL,
    year INT,
    location VARCHAR(100) NOT NULL,
    FOREIGN KEY (format_id) REFERENCES Format(format_id)
);

CREATE TABLE PersonalInformation (
    info_id INT AUTO_INCREMENT PRIMARY KEY,
    athlete_id INT,
    birth_year INT,
    birth_month INT,
    birth_day INT,
    FOREIGN KEY (athlete_id) REFERENCES Athlete(athlete_id)
);

