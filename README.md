# COMP2090 Tasks 1 & 2

## How to Run
### Task 1 (Inventory Management System)
1. Navigate to the `task1` folder
2. Run `python launcher.py`
3. Select role: Admin (password: admin123) or Staff

### Task 2 (Matrix & Sorting)
1. Navigate to the `task2` folder
2. Run `python matrix_operations.py` for matrix demos
3. Run `python shell_sort.py` for sorting demo

## Introduction Video
- Task 1 Demo: [Task 1 Video](https://drive.google.com/file/d/1jFeG9Oe34VU6IGwmcYHhzUdsRYWA2aXd/view?usp=sharing)
- Task 2 Demo: [Task 2 Video](https://drive.google.com/file/d/1Fnea_SJSloyjh5O4tLCtXjfR7Pg4LuMm/view?usp=sharing)
## Description
This repository contains two Python projects for COMP2090: Inventory Management System (Task 1)  Matrix and Shell Sort (Task 2). Both projects demonstrate OOP principles and practical implementations.

## OOP Concepts Used
- **Classes and Objects**: `Product`, `Inventory`, and `Matrix` model data and behavior. GUI pages are also classes in Task 1.
- **Encapsulation**: Data and operations are grouped inside classes; validation and stock changes are handled within methods.
- **Inheritance**: GUI pages inherit from `ttk.Frame`; `MainApp` inherits from `tk.Tk`.
- **Polymorphism**: `Product` and `Matrix` use `__str__()` for display; `Matrix` also overloads `__add__()` and `__mul__()`.
- **Abstraction**: `Inventory` and `Matrix` hide implementation details and expose clear operation methods.
- **Magic Methods**: `__init__()` validates input; `__str__()` formats output; `__add__()` and `__mul__()` support matrix operations.
  
## Project Structure
| File | Description |
| --- | --- |
| `task1/inventory.py` | Inventory management class |
| `task1/launcher.py` | Main application entry with GUI navigation |
| `task1/main_admin.py` | Admin interface for product management |
| `task1/main_user.py` | User interface for purchasing |
| `task1/product.py` | Product class with validation |
| `task1/README.md` | Task 1 documentation |
| `task1/warehouse_data.json` | Auto-generated data storage |
| `task2/matrix_operations.py` | Demo script for matrix operations |
| `task2/matrix.py` | Matrix class with operations |
| `task2/README.md` | Task 2 documentation |
| `task2/shell_sort.py` | Shell sort implementation |


## External Resources
- Python Tkinter documentation
- JSON for data persistence
- Matrix mathematics concepts
