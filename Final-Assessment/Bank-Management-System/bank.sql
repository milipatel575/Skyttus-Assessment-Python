CREATE DATABASE bank_System_db;

USE bank_System_db;

CREATE TABLE accounts(
    account_no INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(50) NOT NULL,
    balance DECIMAL(10,2) DEFAULT 0
);

SELECT * FROM accounts;

USE bank_System_db;

CREATE TABLE transactions(
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    account_no INT,
    transaction_type VARCHAR(20),
    amount DECIMAL(10,2),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(account_no)
    REFERENCES accounts(account_no)
);

SHOW TABLES;

USE bank_System_db;

ALTER TABLE accounts
ADD mobile VARCHAR(15);

ALTER TABLE accounts
ADD account_type VARCHAR(20);

DESC accounts;

SHOW CREATE TABLE accounts;
SELECT * FROM transactions;
DESCRIBE transactions;
SHOW CREATE TABLE transactions;
