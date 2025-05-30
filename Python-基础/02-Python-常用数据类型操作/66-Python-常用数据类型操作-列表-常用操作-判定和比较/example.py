# -*- coding: utf-8 -*-

# @Time    : 2025-5-22 12:58:29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 66-Python-常用数据类型操作-列表-常用操作-判定和比较

# 判定：
# 1. in：判断元素是否在列表中
# 2. not in：判断元素是否不在列表中
# s = "abc"
# l = [1, 2, 3, 4, 5]
# print("a" in s)  # True
# print("c" in l)  # False

# vars = [1, 2, 3, 4, 5]
# print(1 in vars)  # True
# print(6 not in vars)  # True

# 比较：
# 1. cmp(), python2中使用，python3中不支持
# 2. 如果是python3中使用，使用运算符进行比较

# result = cmp(1, 2)
# print(result)  # -1

# result = cmp(1.2, 2)
# print(result)  # -1

# result = cmp(1.2, 2)
# print(result)  # -1

# result = cmp(3, 2)
# print(result)  # 1

# result = cmp("a", "b")
# print(result)  # -1

# result = cmp("a", "a")
# print(result)  # 0

# result = cmp("aa", "ab")
# print(result)  # -1

# result = cmp("aad", "aba")
# print(result)  # -1

# result = cmp([1, 2, 3], [1, 2])
# print(result)  # 1

# result = cmp([1, 2, 3], [2, 2])
# print(result)  # -1

# result = cmp([2, 2, 3], [2, 2])
# print(result)  # 1

# result = [2, 3, 3] == [2, 3]
# print(result)  # False

# result = [2, 3, 4] > [2, 3, 3]
# print(result)  # True