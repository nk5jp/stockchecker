CREATE DATABASE IF NOT EXISTS stockapp;
USE stockapp;

CREATE TABLE IF NOT EXISTS stock
(
    code varchar(4) NOT NULL PRIMARY KEY,
    name VARCHAR(100),
    dividend SMALLINT NOT NULL NOT NULL
);

CREATE TABLE IF NOT EXISTS daily
(
    code varchar(4) NOT NULL,
    get_date INT UNSIGNED NOT NULL,
    price DECIMAL(8,1) NOT NULL,
    PRIMARY KEY(code, get_date),
    FOREIGN KEY fk_d_code (code) REFERENCES stock (code) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS watch_by_code
(
    code varchar(4) NOT NULL,
    is_upper_bound BIT NOT NULL,
    price DECIMAL(8,1) NOT NULL,
    PRIMARY KEY(code, is_upper_bound),
    FOREIGN KEY fk_wbc_code (code) REFERENCES stock (code) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS watch_by_trend
(
    id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    duration SMALLINT UNSIGNED NOT NULL,
    is_positive BIT NOT NULL
);
