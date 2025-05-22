# -*- coding: utf-8 -*-

# @Time    : 2025-5-22 12:58:29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 69-Python-常用数据类型操作-元组-概念和定义

# 概念，有序的不可变的元素集合，和列表的区别就是，元祖元素不能修改
# 定义
# tuple1 = (1, 2, 3, 4, 5)
# print(type(tuple1))
# print(tuple1)

# 多个元素
# tuple2 = (1, 2, 3, 4, 5, 6)
# print(type(tuple2))
# print(tuple2)

# # 单个元素
# tuple3 = (1,)
# print(type(tuple3))
# print(tuple3)
# tuple4 = (1)  # 这不是元组，是整数
# print(type(tuple4))
# print(tuple4)

# t = ("abc",[1, 2], 3)
# print(type(t))
# print(t)

# 多个对象，以逗号隔开，默认为元祖
# t = 1, 2, 3, "neo"
# print(type(t))
# print(t)

# 从列表转换成元祖
# l = [1, 2, 3, 4, 5]
# t = tuple(l)
# print(type(t))
# print(t)

# 元祖嵌套
t = (1, 2, 3, (4, 5, 6), [7, 8, 9])
print(type(t))
print(t)