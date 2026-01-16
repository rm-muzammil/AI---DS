# Python Basics Tutorial

# 1. Variables and Basic Operations
# -------------------------------
# Variables are used to store data. You don't need to declare types in Python.
name = "Python"  # String
version = 3.12   # Float
is_awesome = True # Boolean

# Arithmetic Operations
a = 10
b = 3
sum_val = a + b       # Addition (13)
diff_val = a - b      # Subtraction (7)
prod_val = a * b      # Multiplication (30)
div_val = a / b       # Division (3.333...)
floor_div = a // b    # Floor Division (3) - removes decimal part
remainder = a % b     # Modulus (1) - remainder of division
power = a ** b        # Exponentiation (10^3 = 1000)

print(f"Operations: {a} + {b} = {sum_val}")


# 2. Control Flow (If/Else)
# -------------------------
# Python uses indentation (whitespace) to define blocks of code.
age = 18

if age >= 18:
    print("You are an adult.")
elif age > 12:
    print("You are a teenager.")
else:
    print("You are a child.")


# 3. Loops
# --------
# Loops allow you to repeat a block of code.

# For Loop: Great for iterating over sequences (like lists or ranges)
print("\n--- For Loop ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Range: Generates a sequence of numbers
# range(5) generates 0, 1, 2, 3, 4
print("Counting to 4:")
for i in range(5):
    print(i, end=" ") # end=" " prints on the same line
print() # New line

# While Loop: Runs as long as a condition is True
print("\n--- While Loop ---")
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1 # Decrement count
print("Liftoff!")


# 4. Functions
# ------------
# Functions are reusable blocks of code.

def greet(person_name, greeting="Hello"):
    """
    This is a docstring. It explains what the function does.
    Greets the person with the given greeting.
    """
    message = f"{greeting}, {person_name}!"
    return message

# Calling the function
msg1 = greet("Alice")
msg2 = greet("Bob", greeting="Hi")

print("\n--- Functions ---")
print(msg1)
print(msg2)


# 5. Lists and Dictionaries (Data Structures)
# -------------------------------------------
# Lists: Ordered, mutable collections
numbers = [1, 2, 3, 4, 5]
numbers.append(6) # Add to end
print(f"\nList: {numbers}")

# Dictionaries: Key-Value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"Dictionary: {person['name']} is from {person['city']}")
