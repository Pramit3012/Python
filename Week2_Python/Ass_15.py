base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = 1
for _ in range(exponent):
    result *= base

print(f"{base} to the power of {exponent} is {result}")
