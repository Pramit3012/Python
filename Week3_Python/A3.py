import math

def _solve_quadratic_eqn_(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        realPart = -b / (2 * a)
        imaginaryPart = math.sqrt(-discriminant) / (2 * a)
        return (f"{realPart} + {imaginaryPart}i", f"{realPart} - {imaginaryPart}i")


a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))

solutions = _solve_quadratic_eqn_(a, b, c)
print("The solution(s) of the quadratic equation are:", solutions)
