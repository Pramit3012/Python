def generate_pattern(N):
    matrix = [[0]*N for _ in range(N)]
    
    num = 1
    left, right, top, bottom = 0, N-1, 0, N-1
    
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

N = int(input("Enter the number of lines: "))
matrix = generate_pattern(N)
print_matrix(matrix)
