matrix = [
    [1, 2, 3],
    [4, 1, 2],
    [5, 4, 1]
]

def is_toeplitz(mat):
    rows, cols = len(mat), len(mat[0])
    for i in range(1, rows):
        for j in range(1, cols):
            if mat[i][j] != mat[i-1][j-1]:
                return False
    return True

def is_symmetric(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i, n):
            if mat[i][j] != mat[j][i]:
                return False
    return True

def row_with_max_sum(mat):
    max_sum = float('-inf')
    row_index = -1

    for i, row in enumerate(mat):
        if sum(row) > max_sum:
            max_sum = sum(row)
            row_index = i

    return row_index, max_sum

def rotate_90_clockwise(mat):
    # Transpose
    transposed = list(zip(*mat))
    # Reverse each row
    return [list(row[::-1]) for row in transposed]

print("Toeplitz:", is_toeplitz(matrix))
print("Symmetric:", is_symmetric(matrix))
print("Row with max sum:", row_with_max_sum(matrix))
print("Rotated Matrix:")
for row in rotate_90_clockwise(matrix):
    print(row)
