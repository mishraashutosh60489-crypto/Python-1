# List in Python
# Lists are mutable, ordered collections that can store mixed data types.

l1 = [7, 9, "harry"]
print("Indexing accesses the first item in the list:")
print(l1[0])  # 7
print("Indexing accesses the second item in the list:")
print(l1[1])  # 9
print("Indexing accesses the third item in the list:")
print(l1[2])  # harry
print("Slicing gets the first two items from the list:")
print(l1[0:2])  # [7, 9]

# List methods
l2 = ["A", "B", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "W", "X", "Y"]
print("\nOriginal list:")
print(l2)

print("\nappend() adds an item to the end of the list:")
l2.append("Z")
print(l2)

print("\ninsert() adds an item at a specified index:")
l2.insert(2, "C")
print(l2)

print("\nremove() deletes the first matching item:")
l2.remove("A")
print(l2)

print("\npop() removes the item at the specified index:")
l2.pop(4)
print(l2)

print("\nreverse() reverses the order of the list:")
l2.reverse()
print(l2)

# Tuple in Python
# A tuple is an immutable data type in Python.
# Once created, its elements cannot be changed.

tuple1 = (1, 2, 3, 4, 5, "Raja", "Ashutosh", 23, 50)
print("\nTuple example:")
print(tuple1)
print(tuple1[0])
print(type(tuple1))

tuple2 = ()  # Empty tuple
print("\nEmpty tuple:", tuple2)

tuple3 = (1,)  # Tuple with only one element needs a trailing comma
print("Single-element tuple:", tuple3)

tuple4 = (1, 7, 2, 1)  # Tuple with more than one element
print("\nTuple with repeated values:", tuple4)

# Assign multiple variables at a time
# Number of variables must match the number of elements in the tuple.
a, b, c, d = tuple4
print("\nMultiple assignment:")
print(a, b, c, d)

# Tuple functions
print("\nTuple functions:")
print(tuple4.count(1))
print(tuple4.index(7))
print(7 in tuple4)

