CREATE DATABASE ecommerce_cart_system_db;

USE ecommerce_cart_system_db;

CREATE TABLE products(
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE cart(
    cart_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    quantity INT,

    FOREIGN KEY(product_id)
    REFERENCES products(product_id)
);

INSERT INTO products(product_name,price)
VALUES
('Laptop',50000),
('Mouse',500),
('Keyboard',1000),
('Headphones',2000),
('Pendrive',800);

SELECT * FROM products;