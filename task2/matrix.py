class Matrix:
    def __init__(self, data):
        if not all(isinstance(row, list) for row in data):
            raise ValueError("矩阵必须由列表组成")
        row_length = len(data[0])
        if not all(len(row) == row_length for row in data):
            raise ValueError("矩阵每一行的元素个数必须相同")
        
        self.data = data
        self.rows = len(data)
        self.cols = row_length

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("两个矩阵的行列数必须相同才能相加")
        
        result = []
        for i in range(self.rows):
            new_row = [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            result.append(new_row)
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("第一个矩阵的列数必须等于第二个矩阵的行数")
        
        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def transpose(self):
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(result)
