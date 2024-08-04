number = int(input("Enter a number: "))

total = 0
while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print("The sum of the digits is:", total)

