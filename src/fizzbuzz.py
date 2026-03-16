import sys

# Check if argument exists
if len(sys.argv) < 2:
    print("Usage: python fizzbuzz.py <number>")
    sys.exit()

# Check if argument is a number
try:
    N = int(sys.argv[1])
except ValueError:
    print("Error: N must be a number")
    sys.exit()

# FizzBuzz logic
result = []

for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        result.append("FizzBuzz")
    elif i % 3 == 0:
        result.append("Fizz")
    elif i % 5 == 0:
        result.append("Buzz")
    elif i % 7 == 0:
        result.append("Jazz")
    else:
        result.append(str(i))

print(", ".join(result))