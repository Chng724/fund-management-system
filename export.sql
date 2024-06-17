PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE funds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    manager_name TEXT NOT NULL,
    description TEXT,
    nav REAL NOT NULL,
    date_of_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
    performance REAL NOT NULL
);
INSERT INTO funds VALUES(1,'Beta Fund','Jane Smith','A diversified investment fund.',1500000.0,'2024-06-16 00:40:24',12.5);
INSERT INTO funds VALUES(2,'Beta Fund','Jane Smith','A diversified investment fund.',1500000.0,'2024-06-16 00:46:27',12.5);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('funds',2);
COMMIT;
