num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
while num2 != 0:
    num1= num2
    num2= num1%num2
gcd = num1
print("The GCD of the two numbers is", gcd)