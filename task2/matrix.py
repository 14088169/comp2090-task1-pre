class Matrix:
    def __init__(self, data):
        # Validate that data is a list of lists and that all rows have the same number of columns
        if not all(isinstance(row, list) for row in data):
            raise ValueError("matrix must be composed of lists")
        row_length = len(data[0])
        if not all(len(row) == row_length for row in data):
            raise ValueError("the number of columns in each row must be the same")
        
        # Initialize the matrix data and dimensions
        self.data = data
        self.rows = len(data)
        self.cols = row_length

    def __str__(self):
        # Create a string representation of the matrix for easy visualization
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        # For matrix addition, both matrices must have the same dimensions
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("two matrices must have the same dimensions for addition")
        
        result = []
        for i in range(self.rows):
            # Create a new row by adding corresponding elements from both matrices
            new_row = [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            result.append(new_row)
        return Matrix(result)

    def __mul__(self, other):
        # For matrix multiplication, the number of columns in the first matrix must equal the number of rows in the second matrix
        if self.cols != other.rows:
            raise ValueError("the number of columns in the first matrix must equal the number of rows in the second matrix")
        
        # Initialize the result matrix with zeros
        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        # Perform matrix multiplication
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    # Accumulate the product of the corresponding elements
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def transpose(self):
        # Transpose of a matrix is obtained by swapping rows with columns
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(result)
