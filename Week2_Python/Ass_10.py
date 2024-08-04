import math

def is_krishnamurthy_number(number):
    digits = str(number)
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in digits)
    return sum_of_factorials == number

number = int(input("Enter a number: "))

if is_krishnamurthy_number(number):
    print(number, "is a Krishnamurthy number.")
else:
    print(number, "is not a Krishnamurthy number.")
