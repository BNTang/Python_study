# -*- coding: utf-8 -*-

# @Time    : 2025-5-21 12:07:16
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 61-Python-常用数据类型操作-列表-定义方式

# 列表定义方式

# 1. 直接定义
# name_list = ['程序员NEO', '程序员小张', '程序员小李']
# print(name_list)

# print(type(name_list))

# names = ['程序员NEO', True, 123]
# print(names)

# names = []
# print(type(names))
# print(names)

# items = ["a", "b", "c"]
# names = [1, 2, 3, items]
# print(names)
# print(type(names))

# 2. 列表生成式，range()函数
# 1 - 99
# name_list = range(1, 100)
# print(name_list)

# name_list = range(1, 100, 3)
# print(name_list)

# name_list = range(1, 10000)
# print(name_list)

# 3. 列表推导式
# 概念：一对一变更，过滤从多到少，从一个list，推导出另外一个list
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 原始的方式
# result = []
# for i in nums:
#     print(i)
#     if i % 2 == 0:
#         continue
#     resultNum = i ** 2
#     print(resultNum)
#     result.append(resultNum)

# print(result)

# 列表推导式
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# resultList = [num ** 2 for num in nums]
# print(resultList)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# resultList = [num ** 2 for num in nums if num % 2 == 0]
# print(resultList)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# resultList = [num ** 2 for num in nums for num2 in nums]
# print(resultList)