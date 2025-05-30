# -*- coding: utf-8 -*-

# @Time    : 2025-5-22 12:58:29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 70-Python-常用数据类型操作-元组-常用操作-查询

# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 不能删除
# del t[0] # TypeError: 'tuple' object doesn't support item deletion

# 不能修改
# t[0] = 100 # TypeError: 'tuple' object does not support item assignment

# 不能添加
# t.append(100) # AttributeError: 'tuple' object has no attribute 'append'

# 查
# print(t[0])  # 1
# print(t[-1])  # 10

# 切片
# print(t[0:3])  # (1, 2, 3)

# 从后往前切片
# print(t[4:1:-1])  # (5, 4, 3, 2)
# 4：代表从第5个元素开始
# 1：代表到第2个元素结束
# -1：代表从后往前切片
