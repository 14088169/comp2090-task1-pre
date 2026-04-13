**COMP2090SEF Data Structures Project**

## Table of Contents
- [Project Description](#project-description)
- [OOP Concepts](#oop-concepts-used)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Features](#features)
- [Resources](#external-resources)

## Project Description

This project implements an Inventory Management System, which allows users to manage and organize products in a warehouse.

The system is developed using Object-Oriented Programming (OOP) concepts in Python and demonstrates data structure implementation and modular design.

## OOP Concepts Used

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Modular Programming (multiple Python files)

## Project Structure

```
task1/
├── launcher.py
├── main_admin.py
├── main_user.py
├── inventory.py
├── product.py
├── warehouse_data.json
└── README.md
```

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

- Add new products (Admin)
- Update product information (Admin)
- Delete products (Admin)
- Search products (Admin and User)
- View product list (Admin and User)
- Sort the product list (Admin and User)
- Purchase items (User)
- Auto-save data to JSON

## Project Introduction Video

[Task 1 Intro Video](https://drive.google.com/file/d/1GqVxCOcdOzp9UoSUT1AlNq3U3NBrLEvJ/view?usp=sharing)

## External Resources

- [Python Tkinter documentation 1](https://www.geeksforgeeks.org/python/create-first-gui-application-using-python-tkinter/ )
- [Python Tkinter documentation 1](https://realpython.com/python-gui-tkinter/ )
- [GeeksforGeeks](https://www.geeksforgeeks.org/python/create-first-gui-application-using-python-tkinter/ )
- [W3schools](https://www.w3schools.com/python/python_oop.asp)
- Copilot – used for debugging assistance
- GPT - used for conceptual clarification and syntax suggestions

## Notes

**Final code independently implemented**
