n = int(input("Enter the value of n: "))

sum_series = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_series -= 1 / i
    else:
        sum_series += 1 / i

print("The sum of the series is:", sum_series)
