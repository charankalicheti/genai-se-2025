# Practice 1: Python Basics
# Topics: variables, data types, input/output, and basic operations

# --- Variables and Data Types ---
name = "Alice"
age = 25
height = 5.6
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# --- String operations ---
greeting = "Hello, " + name + "!"
print(greeting)
print("Name in uppercase:", name.upper())
print("Name length:", len(name))

# --- Arithmetic ---
x = 10
y = 3
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Division:", x / y)
print("Floor division:", x // y)
print("Modulus:", x % y)
print("Power:", x ** y)

# --- List basics ---
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
print("First fruit:", fruits[0])
fruits.append("mango")
print("After append:", fruits)

# --- Dictionary basics ---
person = {"name": "Bob", "age": 30, "city": "New York"}
print("Person:", person)
print("City:", person["city"])

# --- Conditional ---
score = 72
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"
print("Grade:", grade)

# --- Loop ---
print("Counting 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# --- User input (uncomment to try interactively) ---
# user_name = input("Enter your name: ")
# print("Hello,", user_name)
