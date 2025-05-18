# -*- coding: utf-8 -*-

# @Time    : 2025-5-18 13:49:39
# @Author  : NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 37-Python-循环-99乘法表

# 1. 37-Python-循环-99乘法表
# 2. 99乘法表是一个经典的数学表格，通常用于帮助学生学习乘法。
# 3. 它的结构是一个矩阵，其中行和列的索引从1到9，单元格中的值是行索引和列索引的乘积。
# 4. 例如，第一行是1到9的乘法，第二行是2到9的乘法，以此类推。
# 5. 99乘法表的特点是对称性，即第i行第j列的值等于第j行第i列的值。
# 6. 99乘法表的输出格式通常是一个矩形，每个单元格之间用空格分隔。

# 实现1：经典三角形99乘法表
print("实现1：经典三角形99乘法表")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} × {i} = {i*j}", end="\t")
    print()  # 换行

print("\n" + "-" * 50)

# 实现2：完整矩形99乘法表
print("实现2：完整矩形99乘法表")
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j} × {i} = {i*j}", end="\t")
    print()  # 换行