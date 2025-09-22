-- Create Database
CREATE DATABASE IF NOT EXISTS restaurant_db;
USE restaurant_db;

-- Admins Table
CREATE TABLE IF NOT EXISTS admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

-- Chefs Table
CREATE TABLE IF NOT EXISTS chefs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

-- Menu Table
CREATE TABLE IF NOT EXISTS menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL DEFAULT 0
);

-- Orders Table
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    quantity INT NOT NULL,
    status INT NOT NULL DEFAULT 0, -- 0 = placed, 1 = being prepared, 2 = ready
    FOREIGN KEY (item_id) REFERENCES menu(id) ON DELETE CASCADE
);

-- Insert Sample Admins
INSERT INTO admins (username, password) VALUES
('admin1', 'admin123'),
('admin2', 'password');

-- Insert Sample Chefs
INSERT INTO chefs (username, password) VALUES
('chef1', 'chef123'),
('chef2', 'password');

-- Insert Sample Menu Items
INSERT INTO menu (name, price, quantity) VALUES
('Veg Burger', 80.00, 10),
('Chicken Burger', 120.00, 8),
('French Fries', 60.00, 15),
('Pasta Alfredo', 150.00, 5),
('Coke', 40.00, 20);

-- Insert Sample Orders
INSERT INTO orders (item_id, quantity, status) VALUES
(1, 2, 0),
(2, 1, 1),
(3, 3, 2);
