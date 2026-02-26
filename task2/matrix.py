class Matrix:
    def __init__(self, rows):
        self.rows = rows 
        self.rows_num = len(rows)  
        self.cols_num = len(rows[0]) if rows else 0  

if __name__ == "__main__":
    m = Matrix([[1,2],[3,4]])
    print("矩阵行数：", m.rows_num, "列数：", m.cols_num)
