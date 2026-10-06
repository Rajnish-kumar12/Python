# Introduction to Python

## What is Python?

Python is a general purpose high level programming language. It was created by Guido van Rossum, and released in 1991. It is used for web development (server-side), software development, mathematics, system scripting.

Python is a programming language that lets you work quickly and integrate systems more effectively.

## General-Purpose Programming Language

General Purpose programming languages are designed to be used for writing software in a wide variety of application domains.

Python is a general-purpose programming language that can be used for many different types of programming tasks, including:

* Web development
* Data analysis
* Standalone applications
* Artificial intelligence
* Scientific computing
* And more

It is known for its simplicity and readability, making it a popular choice for beginners and experienced developers alike.

## High-Level Programming Language

High level programming languages are designed to be easy for humans to read and write.

They abstract away many of the complex details of the computer's hardware, allowing developers to focus on solving problems rather than managing low-level details.

Python's syntax is clear and concise, which helps developers write code that is easy to understand and maintain.

# Python Basics

## Concise Code

Python has a simple and concise syntax. It allows developers to write programs using fewer lines of code while keeping the code readable and easy to maintain.

## Compiler

A compiler translates the **entire source code** into machine code or another lower-level form before execution.

### How a Compiler Works

The basic flow is:

**Source Code → Compiler → Machine Code → CPU → Output**

1. The developer writes the source code.
2. The compiler reads and analyzes the source code.
3. It checks the code for syntax and other compilation errors.
4. If the code is valid, the compiler translates it into machine code or an intermediate form.
5. The generated code is then executed by the CPU.
6. If compilation errors are found, the program generally cannot be executed until those errors are fixed.

## Interpreter

An interpreter executes a program **during runtime** by processing the source code or an intermediate representation and executing it.

### How an Interpreter Works

The basic flow is:

**Source Code → Interpreter → Execution → Output**

1. The developer writes the source code.
2. The interpreter processes the source code.

4. It executes the instructions during runtime.
5. If an error occurs during execution, the interpreter reports the error at that point.

## How Python Works Internally

Python is commonly called an **interpreted language**, but internally the process is a little more complex.

The simplified flow is:

**Python Source Code (`.py`)**
↓
**Python Compiler**
↓
**Bytecode**
↓
**Python Virtual Machine (PVM)**
↓
**Execution**
↓
**Output**

### Step-by-Step

1. We write Python source code in a `.py` file.
2. The Python implementation processes and compiles the source code into **bytecode**.
3. Bytecode is an intermediate representation of the Python program.
4. The **Python Virtual Machine (PVM)** executes this bytecode.
5. The PVM handles the runtime execution of the Python program.
6. If a runtime error occurs, execution stops and Python reports the error.

So, Python is called an **interpreted language** because the Python program is executed through the Python runtime/PVM rather than being directly compiled into a native machine-code executable like a typical C/C++ program.

## Dynamically Typed Language

Python is a **dynamically typed programming language**.

This means the type of a variable is determined automatically at **runtime**, and we do not need to explicitly declare the variable's data type.

## Data Types in Python

Python has several built-in data types, including:

* `int`
* `float`
* `str`
* `bool`
* `list`
* `tuple`
* `set`
* `dict`

Data types are available in Python, but we do not need to explicitly declare them when creating variables.

Below are the topics which are covered in this repository:

Language fundamentals
Operators
Input and output statements
flow control
string data type
list data structure
tuple data structure
set data structure
Dictionary data structure
functions
module
package
oops
Exception handling
file handling
regular expression & web scraping
multithreading
python database connectivity
generators
decorators
assertions
logging mechanism and many more advanced topics.
