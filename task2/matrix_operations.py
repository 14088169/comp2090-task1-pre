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

print("\nMatrix Multiplication (Matrix 1 * Matrix 2):")
print(m1 * m2)

print("\nMatrix 1 Transpose:")
print(m1.transpose())
print("\nMatrix 2 Transpose:")
print(m2.transpose())
print("===== End =====")

