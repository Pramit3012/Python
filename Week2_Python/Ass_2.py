import math

a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The roots are real and different.")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif discriminant == 0:
    root1 = root2 = -b / (2*a)
    print("The roots are real and the same.")
    print("Root 1 and Root 2:", root1)