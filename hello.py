import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

print("First number:", a)
print("Second number:", b)

a, b = b, a

print("After swapping:")
print("First number:", a)
print("Second number:", b)
