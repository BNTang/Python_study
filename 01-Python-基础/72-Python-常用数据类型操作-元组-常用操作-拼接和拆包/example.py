# -*- coding: utf-8 -*-

# @Time    : 2025-5-22 12:58:29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 72-Python-常用数据类型操作-元组-常用操作-拼接和拆包

# *
# str = "a" * 3
# print(str)  # 输出aaa

# str = [1, 2] * 3
# print(str)  # 输出[1, 2, 1, 2, 1, 2]

# str = (1, 2) * 3
# print(str)  # 输出(1, 2, 1, 2, 1, 2)

# +
# str = "a" + "b"
# print(str)  # 输出ab

# str = [1, 2] + [3, 4]
# print(str)  # 输出[1, 2, 3, 4]

# str = (1, 2) + (3, 4)
# print(str)  # 输出(1, 2, 3, 4)

# 元祖与列表是不可拼接的因为元祖是不可变的
# str = (1, 2) + [3, 4]
# print(str)  # 输出TypeError: can only concatenate tuple (not "list") to tuple

# 拆包
# a = 10
# b = 20
# t = (a, b)
# print(t[0], t[1])  # 输出10 20

# a, b = (10, 20)
# print(a, b)  # 输出10 20

# a, b = 10, 20
# print(a, b)  # 输出10 20

a = 1
b = 2
b, a = a, b
print(a, b)  # 输出2 1
