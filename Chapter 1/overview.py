"""A beginner's guide to getting started with Python.

This file is both a reference and a small, runnable example. Read the notes,
then try the examples in a Python interpreter or in your own .py file.
"""

# ---------------------------------------------------------------------------
# 1. Start Python
# ---------------------------------------------------------------------------
# Install Python 3 from https://www.python.org/downloads/ if it is not already
# installed. On Windows, enable "Add Python to PATH" in the installer.
# Open Command Prompt or PowerShell and check the installation:
#
#     py --version
#
# Start the interactive Python prompt (the REPL):
#
#     py
#
# At the >>> prompt, enter Python statements. For example:
#
#     >>> print("Hello, Python!")
#     Hello, Python!
#
# Exit the REPL with exit() or Ctrl+Z, then Enter on Windows. A REPL is useful
# for quick experiments; save longer programs in files ending in .py.
#
# To run a script from its folder, use:
#
#     py overview.py
#
# Python executes a script from top to bottom. Indentation (usually four
# spaces) defines the body of functions, loops, and conditions.


# ---------------------------------------------------------------------------
# 2. Python basics
# ---------------------------------------------------------------------------
# Assign values to variables; Python determines their types at runtime.
name = "Ada"                 # str: text, written inside quotes
age = 12                     # int: whole number
temperature = 21.5           # float: decimal number
is_learning = True           # bool: True or False

# print() displays values. input() reads text from the user.
print("Hello,", name)
# favorite_color = input("What is your favorite color? ")

# Common collection types:
colors = ["blue", "green"]   # list: ordered and changeable
point = (3, 4)                # tuple: ordered and not changeable
settings = {"theme": "dark"} # dict: key/value pairs
unique_numbers = {1, 2, 3}    # set: unique values

# Use if/elif/else to choose what to do. A colon starts an indented block.
if age >= 18:
	age_group = "adult"
else:
	age_group = "under 18"

# Loops repeat work. range(3) produces 0, 1, and 2.
for number in range(3):
	print(number)

# Define reusable behavior with a function.
def greet(person):
	"""Return a greeting for person."""
	return f"Hello, {person}!"


# ---------------------------------------------------------------------------
# 3. Comments and docstrings
# ---------------------------------------------------------------------------
# A comment begins with #. Python ignores the # and everything after it on
# that line. Use comments to explain intent, assumptions, or non-obvious code.
# Avoid comments that merely repeat what the code already says.

# This is a single-line comment.
total = 2 + 3  # An end-of-line comment is also possible.

# For a longer note, use # at the beginning of each line:
# Keep this value in seconds because the API expects seconds.
# Convert to minutes only when displaying it to the user.

# A docstring is a string immediately inside a module, function, or class.
# It documents what that object does and can be viewed with help(). This file's
# opening triple-quoted string is its module docstring; greet() has one too.


# ---------------------------------------------------------------------------
# 4. Modules and imports
# ---------------------------------------------------------------------------
# A module is a Python file that can provide code to another file. Python's
# standard library includes modules such as math, random, and pathlib.
# Import a whole module and access its members using module.member:
#
#     import math
#     print(math.sqrt(25))  # 5.0
#
# Import a specific member when that makes the code clearer:
#
#     from pathlib import Path
#     folder = Path(".")
#
# Avoid naming your own files after standard-library modules (for example,
# math.py or random.py), because that can interfere with imports.
#
# A module can also be your own .py file. If hello.py is beside app.py, app.py
# can use `import hello`. Python searches the current project and configured
# import paths for modules. Larger projects often group modules in packages
# (directories containing Python files).
#
# Code intended to run only when a file is launched directly goes under this
# guard. When another file imports this module, that code is not run.
if __name__ == "__main__":
	print(greet(name))


# ---------------------------------------------------------------------------
# 5. pip and third-party packages
# ---------------------------------------------------------------------------
# pip is Python's package installer. It downloads third-party packages from
# the Python Package Index (PyPI); it is not needed to import the standard
# library. Prefer a virtual environment so project dependencies stay separate.
# Run these commands in a terminal, not at the Python >>> prompt:
#
#     py -m venv .venv
#     .venv\Scripts\activate
#     py -m pip install requests
#     py -m pip show requests
#     py -m pip list
#
# On macOS/Linux, activate the environment with:
#     source .venv/bin/activate
#
# Use `py -m pip` to ensure pip belongs to the Python interpreter selected by
# `py`. Record project dependencies when appropriate:
#
#     py -m pip freeze > requirements.txt
#     py -m pip install -r requirements.txt
#
# Then use the installed package in Python, for example:
#     import requests
#
# Install packages only from sources you trust. If a command is unavailable,
# check that Python is installed and that the virtual environment is active.
