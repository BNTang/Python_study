# -*- coding: utf-8 -*-

# @Time    : 2025-5-22 12:58:29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 68-Python-常用数据类型操作-列表-常用操作-乱序和反转

# 乱序
# import random
# l = [1, 3, 2, 4, 5, 22, 2, 2, 4, 19]
# result = random.shuffle(l)
# print(result)
# print(l)

# 反转
# l = [1, 3, 2, 4, 5, 22, 2, 2, 4, 19]
# result = l.reverse()
# print(result)
# print(l)

# 切片反转
l = [1, 3, 2, 4, 5, 22, 2, 2, 4, 19]
result = l[::-1]
print(result)
print(l)