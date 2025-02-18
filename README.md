## python-calculator
Python Calculator with Unit Testing

This repository contains a simple calculator program written in Python. It includes a command-line interface for performing basic arithmetic operations (addition, subtraction, multiplication, and division) and unit tests to ensure the calculator's functionality.

## Features

* Command-line interface:  Users can interact with the calculator through the terminal.
* Basic arithmetic operations: Supports addition, subtraction, multiplication, and division.
* Error handling: Handles invalid input (non-numerical values) and division by zero errors.
* Unit tests:  Includes a comprehensive set of unit tests to verify the correctness of the calculations.

## How to Run 

1. To run the calculator
    bash
    CopyEdit
    python calculator.py

2. To run the unit tests
    bash
    CopyEdit
    python -m unittest test_calculator.py

## Usage
The calculator will prompt you to enter two numbers and choose an operation (+, -, *, /).  It will then display the result.  You can continue performing calculations until you choose to exit.

Enter first number: 10
Enter second number: 5
Choose operation (+, -, *, /): +
Result: 10.0 + 5.0 = 15.0
Do you want to perform another calculation? (yes/no): yes
Enter first number: 20
Enter second number: 0
Choose operation (+, -, *, /): /
Cannot divide by zero.
Do you want to perform another calculation? (yes/no): no
Goodbye!

## Files
calculator.py: The main Python script containing the Calculator class and the main program loop.
test_calculator.py: The Python script containing the unit tests for the Calculator class.

## Requirements
Python 3.x
   


   
