"""Practical overview of Python variables and common data types.

Run this file to see examples of creating, inspecting, and using values.
"""

# Variables are names that refer to values. Python infers each value's type.
name = "Asha"             # str: text
age = 18                  # int: whole number
height = 1.65             # float: decimal number
is_student = True         # bool: True or False
middle_name = None        # NoneType: no value

print("VARIABLES AND TYPES")
for label, value in (("name", name), ("age", age), ("height", height),
					 ("is_student", is_student), ("middle_name", middle_name)):
	print(f"{label}: {value!r} ({type(value).__name__})")

# Collection types group values in different ways.
subjects = ["Python", "Math"]                 # list: ordered and mutable
point = (4, 7)                                  # tuple: ordered and immutable
unique_numbers = {1, 2, 2, 3}                   # set: unique values
student = {"name": name, "age": age}           # dict: key-value pairs

print("\nCOLLECTIONS")
subjects.append("Science")
print("Updated subjects:", subjects)
print("First subject:", subjects[0])
print("Point:", point)
print("Unique numbers:", unique_numbers)
print("Student name:", student["name"])

# A variable can be reassigned; arithmetic creates a new value.
age = age + 1
print("\nNext year, age:", age)

# Convert compatible values explicitly. input() also returns a string.
number = int("42")
price = float("3.50")
age_label = "Age: " + str(age)
print("\nCONVERSIONS")
print(number, price, age_label)

# Naming convention: descriptive lowercase names separated by underscores.
# Names are case-sensitive and cannot begin with a digit.
total_score = 95
print("Total score:", total_score)

# Uncomment these lines to try reading a whole number from the keyboard:
# user_age = int(input("Enter your age: "))
# print("Next year you will be", user_age + 1)
