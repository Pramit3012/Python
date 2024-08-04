def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Undefined (vertical line)"
    return (y2 - y1) / (x2 - x1)

x1 = int(input("Enter the x-coordinate of the first point: "))
y1 = int(input("Enter the y-coordinate of the first point: "))
x2 = int(input("Enter the x-coordinate of the second point: "))
y2 = int(input("Enter the y-coordinate of the second point: "))

print("The slope of the line is:", calculate_slope(x1, y1, x2, y2))
