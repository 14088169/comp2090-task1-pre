from matrix import Matrix

print("===== 矩阵运算 =====")
print("请选择操作：")
print("1  矩阵相加")
print("2  矩阵相乘")
choice = int(input("输入编号："))

print("\n请输入第一个矩阵的行数和列数（用空格分开）：")
r1, c1 = map(int, input().split())
print("请输入矩阵数据，一行一行输：")
m1_data = []
for _ in range(r1):
    row = list(map(int, input().split()))
    m1_data.append(row)

print("\n请输入第二个矩阵的行数和列数（用空格分开）：")
r2, c2 = map(int, input().split())
print("请输入矩阵数据，一行一行输：")
m2_data = []
for _ in range(r2):
    row = list(map(int, input().split()))
    m2_data.append(row)

m1 = Matrix(m1_data)
m2 = Matrix(m2_data)

print("\n===== 结果 =====")
if choice == 1:
    print(m1 + m2)
elif choice == 2:
    print(m1 * m2)
else:
    print("输入错误")
