import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

print("First number:", a)
print("Second number:", b)

a, b = b, a

print("After swapping:")
print("First number:", a)
print("Second number:", b)

---------------------------------------------------------------------------------------------------------
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

print("Sum =", a + b)

-----------------------------------------------------------------------------------------------------------

import sys

n = int(sys.argv[1])

fact = 1

for i in range(1, n + 1):
fact *= i

print("Factorial =", fact)

--------------------------------------------------------------------------------------------------------------

import sys

n = int(sys.argv[1])

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
print(a, end=" ")
a, b = b, a + b
