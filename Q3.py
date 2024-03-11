def matrix_power(A, m):
    n = len(A)
    result = [[0] * n for _ in range(n)]  # Initialize the result matrix with zeros

    # If m is 0, return the identity matrix
    if m == 0:
        for i in range(n):
            result[i][i] = 1
        return result

    # Initialize the result matrix with A if m is 1
    if m == 1:
        return A

    # Multiply the matrix A by itself m times
    result = A[:]  # Make a copy of A
    for _ in range(1, m):
        result = matrix_multiply(result, A)

    return result

def matrix_multiply(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]  # Initialize the result matrix with zeros

    # Perform matrix multiplication
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example usage:
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

m = 3  # Positive integer for matrix power

result = matrix_power(A, m)
print("A raised to the power of", m, "is:")
for row in result:
    print(row)
