import os

path = input("Enter directory path: ")

try:
    contents = os.listdir(path)

    print("Contents of the directory:")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Directory not found.")
except PermissionError:
    print("Permission denied.")