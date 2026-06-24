def read_number(prompt):
    """Safely read a number from the user."""
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return read_number(prompt)


# Read two numbers with validation
a = read_number("Enter the first number: ")
b = read_number("Enter the second number: ")

print(f"Before swapping: a = {a}, b = {b}")

# Swap using tuple unpacking
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")
