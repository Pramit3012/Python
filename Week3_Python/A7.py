import math

def sine(x, n):
    sine = 0
    sign = 1
    for i in range(n):
        term = (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        sine += sign * term
        sign *= -1
    return sine

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))

print("sin(x) =", sine(x, n))
