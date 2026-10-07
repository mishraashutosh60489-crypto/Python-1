# Dictionary in Python
# A dictionary stores data in key-value pairs.
# It is useful for representing structured information.
# details = {
#     "Name": "Ashutosh Mishra",
#     "RollNo": "25DIT058",
#     "Year": "2nd Yr",
#     "Course": "BSc ITM",
#     "list": [90, 99, 95]
# }

# Accessing values from a dictionary
# print(details, type(details))
# print(details["Name"])           # direct key access
# print(details.get("Course"))     # safer access using .get()
# print(details.get("Address", "Address not found"))

# Dictionary methods and useful operations
# print("items:", details.items())
# print("keys:", details.keys())
# print("values:", details.values())
# print("length:", len(details))
# print("Name exists:", "Name" in details)

# Add and update values in a dictionary
# details["City"] = "Ahmedabad"                 # add a new key-value pair
# details.update({"Year": "3rd Yr", "Semester": 5})
# details.setdefault("Email", "ashutosh@example.com")
# print("updated:", details)

# Remove values without changing the main dictionary
# example = details.copy()
# print("pop:", example.pop("Semester"))
# print("popitem:", example.popitem())
# del example["City"]
# print("after deletion:", example)

# Create a dictionary with the same default value for multiple keys
# subjects = dict.fromkeys(["Python", "Maths", "English"], 0)
# print("fromkeys:", subjects)

# Copy and clear a dictionary
# copied_details = details.copy()
# print("copy:", copied_details)
# copied_details.clear()
# print("clear:", copied_details)

# print("final dictionary:", details)

# Sets in Python
# A set stores unique values and does not keep duplicate items.
s = {1, 3, 5, 6}
print(type(s))
print(s)

# Empty set creation
# Note: {} creates an empty dictionary, not an empty set.
# Use set() to create an empty set.
e = set()
print(type(e))

# Methods used in sets
# len(s): Returns the number of items in the set.
print(len(s))

# add(item): Adds one item to the set. Duplicates are ignored.
s.add(8)
print("after add:", s)

# update(iterable): Adds multiple items from another iterable.
s.update([9, 10])
print("after update:", s)

# remove(item): Removes an item and raises KeyError if the item is missing.
s.remove(6)
print(s)

# discard(item): Removes an item if it exists; no error is raised if absent.
s.discard(100)
print("after discard:", s)

# pop(): Removes and returns an arbitrary item from the set.
s.pop()
print(s)

# copy(): Returns a shallow copy of the set.
s_copy = s.copy()
print("copy:", s_copy)

# clear(): Removes all items from the set.
s.clear()
print(s)

s1 = {1, 24, 5, 6, 8}
s2 = {2, 24, 6, 1}

# union(): Returns all unique items from both sets.
# The | operator can also be used: s1 | s2.
print(s1.union(s2))

# intersection(): Returns the common elements between both sets.
# The & operator can also be used.
print(s1.intersection(s2))

# difference(): Returns items in s1 that are not in s2.
# The - operator can also be used.
print("difference:", s1.difference(s2))

# symmetric_difference(): Returns items present in either set, but not both.
# The ^ operator can also be used.
print("symmetric difference:", s1.symmetric_difference(s2))

# issubset(): Checks whether every item in s1 is also in s2.
print("subset:", s1.issubset(s2))

# issuperset(): Checks whether s1 contains every item in s2.
print("superset:", s1.issuperset(s2))

# isdisjoint(): Checks whether two sets have no common elements.
print("disjoint:", s1.isdisjoint(s2))

# in / not in: Checks whether an item exists in a set.
print("24 in s1:", 24 in s1)
print("100 not in s1:", 100 not in s1)

