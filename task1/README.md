# Inventory Management System

## Introduction
This is an inventory management system built with Python using Tkinter GUI.
It supports two roles: Admin and Staff, for managing products, updating stock, purchasing items, and automatically saving data to JSON.

## Environment Requirements
- Python 3.x
- Built-in libraries: tkinter, json

## Project Files
- launcher.py - Main program entry
- main_admin.py - Admin interface
- main_user.py - User interface
- inventory.py - Inventory management class
- product.py - Product class
- warehouse_data.json - Data file (auto-generated)

## How to Run
1. Unzip from github. Put all .py files in the same folder
2. Run launcher.py:
   ```
   cd ...\comp2090-task1-pre-main\task1
   python launcher.py (or python3 launcher.py)
   ```
3. On the home page, select your role:
   - For Admin: Enter password "admin123" to login
   - For Staff: Click "Staff" to enter the purchase interface
4. Note: Do not run main_admin.py or main_user.py directly. Only use launcher.py to start the program.

## Features

### Admin Features
- Add new products
- Update product information
- Delete products
- Search products
- View product list
- Auto-save data

### User Features
- View all products
- Select and purchase items
- Auto deduct stock after purchase
- Calculate total price
- Auto remove product when stock reaches 0

## Demo Video
Watch the demo video: [Link](...)
- Modular programming with multiple files
- Separation of GUI and business logic
