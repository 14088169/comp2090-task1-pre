# Inventory Management System
COMP2090SEF Group Project
Data Structures, Algorithms and Problem Solving

## Project Description
This is an inventory management system developed in Python with GUI using Tkinter.
The system supports two roles: Admin and User, including functions of product management, stock update, purchase and data persistence.
Features include admin login with password protection, input validation, purchase confirmation with total price calculation, and automatic data saving to JSON.

## Environment
- Built-in libraries: tkinter, json

## Project Files
- launcher.py      Main launcher (entry point of the application)
- main_admin.py         Admin interface module
- main_user.py          User interface module
- inventory.py          Inventory management class
- product.py            Product class
- warehouse_data.json   Data storage file (auto-generated)

## How to Run
1. Place all `.py` files in the same folder.
2. Run **launcher.py** as the main launcher.
3. On the home page, select your role:
   - For **Admin**: Enter password "admin123" in the login panel to access admin interface
   - Click **User** to enter the user purchase interface
4. Do NOT run main_admin.py or main_user.py directly.
   Please only use launcher.py as the official entry.

## Features

### Admin
- Add new products
- Update existing product information
- Delete products
- Search products by ID or name
- View and refresh product list
- Auto-save data to JSON

### User
- View all available products
- Select and purchase products
- Auto deduct stock after purchase
- Auto remove product when stock is 0

## OOP Concepts Applied
- Class and Object
- Encapsulation
- Constructor method __init__
- Instance variables and methods
- Modular programming with multiple files
- Separation of GUI and business logic
