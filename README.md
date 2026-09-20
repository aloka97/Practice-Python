Practice-Python — Study Files

Overview

This repository contains beginner and intermediate Python study/example files intended for hands-on learning. Each file includes short explanations and runnable examples to demonstrate core concepts.

Files

- beginner_python_topics.py — Beginner-level topics with definitions and examples:
  - Variables, data types, and type conversion
  - Operators and expressions
  - Conditionals: if / elif / else
  - Loops: for and while
  - Lists, tuples, sets, and dictionaries
  - String operations and formatting
  - Functions: parameters, return values, scope
  - Default arguments and keyword arguments
  - Recursion basics
  - Lambda functions
  - List comprehensions and dictionary comprehensions
  - Basic input/output (handles missing input with safe defaults)
  - Error handling: try / except / finally

- intermediate_python_topics.py — Intermediate topics with examples:
  - Decorators
  - Higher-order functions
  - map(), filter(), reduce()
  - Modules and imports
  - File handling (reads/writes a temporary sample_file.txt)
  - JSON serialization/deserialization
  - Regular expressions
  - Object-oriented programming (classes, inheritance)
  - Dataclasses
  - Type hints
  - Exception handling and custom errors
  - Notes about packages and virtual environments

Prerequisites

- Python 3.8+ (recommended: 3.10/3.11)
- Windows users: use PowerShell or CMD from the repository root
- Optional but recommended: create and activate a virtual environment
  - python -m venv venv
  - venv\Scripts\Activate.ps1   (PowerShell)
  - venv\Scripts\activate.bat   (CMD)

How to run

Open a terminal in the repository root (C:\Users\USER\Documents\GitHub\Practise Python) and run:

- Run the beginner file:
  python beginner_python_topics.py

  The script prints explanations and runs examples. It asks for "Enter your name:" and "Enter a number:"; if no input is provided (or EOF), it uses safe defaults so the script still completes.

- Run the intermediate file:
  python intermediate_python_topics.py

Notes and safety

- The intermediate script creates a temporary file named sample_file.txt when demonstrating file handling. The file is removed by the verification step run during development; running the script yourself will recreate it in the repo folder.
- The beginner script handles EOF on input gracefully, but when running interactively you can provide input to see those examples live.

Suggested next steps

- Create exercises: add practice_*.py files that implement short problems (e.g., FizzBuzz, prime checks, text parsing).
- Add unit tests with pytest for key functions (e.g., factorial, add_numbers).
- Convert these scripts to a Jupyter notebook for interactive learning (optional).
- Add a 30-day practice plan or a quiz file to test understanding.

Contributing

Feel free to add, improve, or reorganize topics. If you add files, update this README to reflect the changes.

License

This repository is for personal learning. Add a license file if you plan to share or publish.

Contact

For help or changes you'd like automated (examples, exercises, quizzes), tell me what you'd like next and I can create the code or tests for you.