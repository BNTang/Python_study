# -*- coding: utf-8 -*-

# @Time    : 2025-5-17 12:30:06
# @Author  : NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 35-Python-循环-循环和分支嵌套-和if嵌套

# 1. 35-Python-循环-循环和分支嵌套-和if嵌套
# 循环内嵌套if
# 本质就是只要是代码,都能放在代码块的位置案例· 打印1-100之间,所有3的倍数

# 示例1: 打印1-100之间,所有3的倍数
print("示例1: 打印1-100之间所有3的倍数")
for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=" ")
print("\n")

# 示例2: 循环嵌套分支 - 判断1-50之间的奇数和偶数
print("示例2: 判断1-50之间的奇数和偶数")
for i in range(1, 51):
    if i % 2 == 0:
        print(f"{i}是偶数")
    else:
        print(f"{i}是奇数")
print()

# 示例3: 嵌套循环 - 打印乘法表
print("示例3: 打印乘法表")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()
print()

# 示例4: 循环中的多重条件判断 - 1-100中同时是3和5的倍数的数字
print("示例4: 1-100中同时是3和5的倍数的数字")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
print()