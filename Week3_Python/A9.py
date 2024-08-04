def print_pattern(N):
    for i in range(N):
        print(" " * (N - i - 1) + "/" + " " * (2 * i) + "\\")
    print("/" + "_" * (2 * N - 2) + "\\")
2
N = int(input("Enter the number of lines: "))
print_pattern(N)