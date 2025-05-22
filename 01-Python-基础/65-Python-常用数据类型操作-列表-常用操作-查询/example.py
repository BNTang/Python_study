# -*- coding: utf-8 -*-

# @Time    : 2025-5-22 12:58:29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 65-Python-常用数据类型操作-列表-常用操作-查询

# 获取单个元素
# list1 = range(1, 10)
# print(list1[0])  # 1

# 取最后一个元素
# list1 = range(1, 10)
# print(list1[-1])  # 9

# 获取元素索引
# list1 = range(1, 10)
# print(list1.index(5))  # 4

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# idx = list1.index(5, 1) # 不能使用 range()，否则会报错
# print(idx)  # 4

# 获取指定元素的个数
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list1.count(5))  # 1

# 获取多个元素，切片
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list1[0:3])  # [1, 2, 3]
# print(list1[0:3:2])  # [1, 3]
# print(list1[::])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list1[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# 遍历方式1：for
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# curIdx = 0
# for num in nums:
#     idx = nums.index(num, curIdx)
#     print(idx, end=' ')
#     curIdx = idx + 1
    # print(num, end=' ')

# 遍历方式2：
# vars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # idxs = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# # idxs = range(11)
# count = len(vars)
# idxs = range(count)
# for idx in idxs:
#     print(vars[idx], end=' ')

# 遍历方式3：通过创建枚举对象
# vars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # 1.先根据列表，创建一个枚举对象
# print(enumerate(vars))  # <enumerate object at 0x000001A2D3F4C8B0>
# print(list(enumerate(vars)))  # [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]

# 2.再通过for循环遍历枚举对象
# for idx, value in enumerate(vars):
#     print(idx, value)

# for idx, value in enumerate(vars, start=1):
#     print(idx, value)

# 遍历方式4：通过迭代器
# vars = "abc"
# vars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 给我一个对象，判定是不是可迭代对象
# for var in vars:
#     print(var, end=' ')
# import collections.abc
# Iterable 是判断是否是可迭代对象的一个类
# result = isinstance(vars, collections.abc.Iterable)
# print(result)  # True

# vars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# import collections.abc
# # 判断是否是可迭代对象 Iterable是判断是否是可迭代对象的一个类
# result = isinstance(vars, collections.abc.Iterable)
# print(result)  # False

# vars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# import collections.abc
# i = iter(vars)
# # print(i)  # <list_iterator object at 0x000001A2D3F4C8B0>
# result = isinstance(i, collections.abc.Iterator)
# print(result)  # True

# 斐波那契数列，小于1w的

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 创建一个迭代器
it = iter(l)

# print(next(it))  # 1

for v in it:
    print(v, end=' ')

for v in it:
    print(v, end=' ')