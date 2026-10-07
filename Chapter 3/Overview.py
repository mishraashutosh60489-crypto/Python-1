# Strings in Python
# A string can be created using single quotes, double quotes, or triple quotes.
a = 'harry'          # Single-quoted string
b = "harry"          # Double-quoted string
c = '''harry'''       # Triple-quoted string

# String slicing
# Syntax: string[start:end:step]
word = "amazing"
print(word[1:6:2])    # Output: mzn

s = a[1:5]            # Slice from index 1 to 4
print(s)              # Output: arry

# Advanced slicing examples
print(word[-7:-1])    # Output: amazin
print(word[:7])        # Output: amazing
print(word[0:])        # Output: amazing

# Built-in string methods
# 1. len() returns the length of the string.
string = 'ashutosh'
print(len(string))    # Output: 8

# 2. endswith() checks if the string ends with the given text.
print(string.endswith('h'))  # Output: True

# 3. count() counts the total occurrences of a character or substring.
print(string.count('h'))    # Output: 2

# 4. capitalize() capitalizes the first character.
print(string.capitalize())  # Output: Ashutosh

# 5. find() returns the index of the first occurrence.
print(string.find('h'))     # Output: 2

# 6. replace(old, new) replaces the old text with the new text.
print(string.replace('osh', 'on'))  # Output: ashuton

# 7. upper() converts the string to uppercase.
print(string.upper())  # Output: ASHUTOSH

# 8. lower() converts the string to lowercase.
print(string.lower())  # Output: ashutosh
