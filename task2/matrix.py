class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.data = [[value for _ in range(cols)] for _ in range(rows)]

    def get(self, i, j):
        return self.data[i][j]

    def set(self, i, j, value):
        self.data[i][j] = value

    def display(self):
        for row in self.data:
            print(row)


m = Matrix(4, 3)
m.display()