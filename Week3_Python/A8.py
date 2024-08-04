import math

def cosine(x, n):
    cosine = 0
    sign = 1
    for i in range(n):
        term = (x ** (2 * i)) / math.factorial(2 * i)
        cosine += sign * term
        sign *= -1
    return cosine

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))

print("cos(x) =", cosine(x, n))

