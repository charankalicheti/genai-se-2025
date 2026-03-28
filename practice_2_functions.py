# Practice 2: Functions
# Topics: defining functions, parameters, default arguments, return values, *args/**kwargs

# --- Basic function ---
def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))
print(greet("Bob"))

# --- Default arguments ---
def describe_pet(name, animal="dog"):
    return f"{name} is a {animal}."

print(describe_pet("Rex"))
print(describe_pet("Whiskers", "cat"))

# --- Multiple return values ---
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print("Min:", low, "| Max:", high)

# --- *args: variable number of positional arguments ---
def add_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print("Sum:", add_all(1, 2, 3))
print("Sum:", add_all(10, 20, 30, 40))

# --- **kwargs: variable number of keyword arguments ---
def print_profile(**info):
    for key, value in info.items():
        print(f"  {key}: {value}")

print("Profile:")
print_profile(name="Carol", age=28, role="Engineer")

# --- Recursive function ---
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))
print("10! =", factorial(10))

# --- Lambda (anonymous function) ---
square = lambda x: x ** 2
print("Square of 7:", square(7))

numbers = [5, 3, 8, 1, 9, 2]
sorted_numbers = sorted(numbers, key=lambda x: x)
print("Sorted:", sorted_numbers)

# --- Higher-order functions ---
evens = list(filter(lambda x: x % 2 == 0, range(1, 11)))
squares = list(map(lambda x: x ** 2, range(1, 6)))
print("Evens 1-10:", evens)
print("Squares 1-5:", squares)
