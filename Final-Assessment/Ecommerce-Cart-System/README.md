# E-Commerce Cart System

## Project Description

A menu-driven Python and MySQL application that simulates a simple e-commerce shopping cart system.

## Features

- View Products
- Add Product
- Add To Cart
- View Cart
- Remove From Cart
- Generate Bill
- Clear Cart
- MySQL Database Integration

## Technologies Used

- Python
- MySQL
- mysql-connector-python

## Database Tables

### products
- product_id
- product_name
- price

### cart
- cart_id
- product_id
- quantity

## How to Run

1. Execute ecommerce.sql in MySQL.
2. Update MySQL credentials in ecommerce.py.
3. Run:

```bash
python ecommerce.py