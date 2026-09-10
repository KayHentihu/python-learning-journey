# 🧮 Calculator Python

A simple command-line calculator built with Python as part of my Python learning journey.

This project started as a basic calculator and was gradually refactored to make the code cleaner, more organized, and easier to maintain.

## ✨ Features

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* `%` Modulus
* 🚪 Exit menu
* ⚠️ Input validation
* 🛡️ Handling division and modulus by zero
* 🔄 Interactive menu using a loop

## 📂 Project Structure

```text
Calculator-Python/
│
├── main.py
├── menu_calculator.py
│
└── modules/
    ├── penjumlahan.py
    ├── pengurangan.py
    ├── perkalian.py
    ├── pembagian.py
    ├── modulus.py
    └── tunggu_enter.py
```

## 🧠 What I Learned

Through this project, I practiced:

* Creating and calling functions
* Using function parameters and return values
* Importing functions from different modules
* Using `while True` for interactive programs
* Using `match-case` for menu selection
* Handling errors with `try-except`
* Using `continue` and `return`
* Passing functions as values
* Refactoring repeated code into a simpler structure
* Organizing a Python project into multiple modules

## 🔄 Refactoring

One of the main improvements in this project was reducing repeated code inside the menu.

Instead of calculating each operation separately inside every `case`, the selected mathematical operation is stored in a variable and executed afterward.

This makes the menu easier to read and makes the code more maintainable.

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

## 🎯 Learning Goal

This project is part of my journey to strengthen my Python fundamentals through small, practical projects.

> ⭐ Built as part of my Python learning journey.
