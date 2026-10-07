# Chapter 7: Loops in Python - Quick Notes
# 1. While loop: print numbers from 1 to 50

i = 1
while i <= 50:
    print(i)
    i += 1

# 2. While loop: print the items of a list
students = ["Harry", "Raam", "Somesh", "Rohit"]
index = 0

while index < len(students):
    print(students[index])
    index += 1

# 3. Range function in Python
print("Even numbers from 1 to 100:")
for num in range(1, 101):
    if num % 2 == 0:
        print(num)

# Note: range(100, 5) is empty because the loop starts at 100 and stops before 5.
# If you want to print in descending order, use a negative step:
print("Numbers from 100 to 6:")
for num in range(100, 5, -1):
    print(num)

# 4. For loop with else
numbers = [2, 3, 4, 6]
for num in numbers:
    print(num)
else:
    print("Done!")

# 5. break and continue in Python
print("break example:")
for num in range(100):
    if num == 23:
        break  # exits the loop immediately
    print(num)

print("continue example:")
for num in range(100):
    if num == 23:
        continue  # skips this iteration
    print(num)

# 6. pass keyword: used when a block needs to exist but do nothing
for _ in range(30):
    pass

for i in range(10):
    print(i)

# End of notes
