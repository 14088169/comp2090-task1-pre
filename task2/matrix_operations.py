"""
Quick demo script that exercises the Matrix class for
addition, multiplication, and transpose.
"""

from matrix import Matrix

print("===== matrix operations demo=====")

# Define two matrices
m1_data = [
    [1, 2, 3],
    [4, 5, 6]
]

m2_data = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Create Matrix objects from the raw nested lists
m1 = Matrix(m1_data)
m2 = Matrix(m2_data)

print("Matrix 1:")
print(m1)
print("\nMatrix 2:")
print(m2)

print("\n===== Results =====")
print("Matrix Addition (Matrix 1 + Matrix 1):")
print(m1 + m1)
print()
print("If Matrix 1 + Matrix 2 will raise an error because they have different dimensions")

# Multiplication uses the row-by-column rule: columns of first must match rows of second

print("\nMatrix Multiplication (Matrix 1 * Matrix 2):")
print(m1 * m2)

print("\nMatrix 1 Transpose:")
print(m1.transpose())
print("\nMatrix 2 Transpose:")
print(m2.transpose())
print("===== End =====")

