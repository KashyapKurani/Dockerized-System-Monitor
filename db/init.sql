CREATE DATABASE IF NOT EXISTS monitor_db;

USE monitor_db;

CREATE TABLE IF NOT EXISTS visits (
    id INT PRIMARY KEY,
    visit_count INT NOT NULL
);

INSERT IGNORE INTO visits (id, visit_count)
VALUES (1, 0);