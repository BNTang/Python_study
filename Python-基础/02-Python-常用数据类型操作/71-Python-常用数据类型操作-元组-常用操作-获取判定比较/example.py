# -*- coding: utf-8 -*-

# @Time    : 2025-5-22 12:58:29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 71-Python-常用数据类型操作-元组-常用操作-获取判定比较

# 获取元组的个数
# t = (1, 2, 3, 4, 5, 2)
# c = t.count(2)
# print(c)  # 2

# 获取的元素不在元组中会存在返回什么内容呢？
# t = (1, 2, 3, 4, 5, 2)
# c = t.count(6)
# print(c)  # 0

# 获取元组的索引
# t = (1, 2, 3, 4, 5, 2)
# i = t.index(2)
# print(i)  # 1

# 获取的元素不在元组中会存在返回什么内容呢？
# t = (1, 2, 3, 4, 5, 2)
# i = t.index(6)
# print(i)  # ValueError: tuple.index(x): x not in tuple

# len：获取元组的长度
# t = (1, 2, 3, 4, 5, 2)
# l = len(t)
# print(l)  # 6

# max：获取元组的最大值
# t = (1, 2, 3, 4, 5, 2)
# m = max(t)
# print(m)  # 5

# min：获取元组的最小值
# t = (1, 2, 3, 4, 5, 2)
# m = min(t)
# print(m)  # 1

# 判定 ================== ========================
# in：判断元素是否在元组中
# t = (1, 2, 3, 4, 5, 2)
# print(2 in t)  # True
# print(6 in t)  # False

# not in：判断元素是否不在元组中
# t = (1, 2, 3, 4, 5, 2)
# print(2 not in t)  # False
# print(6 not in t)  # True

# cmp：比较两个元组，Python 2.x 中使用，Python 3.x 中不支持
# t1 = (1, 2, 3)
# t2 = (1, 2, 3)
# t3 = (1, 2, 4)
# print(cmp(t1, t2))  # 0
# print(cmp(t1, t3))  # -1
# print(cmp(t3, t1))  # 1

t1 = (1, 2, 3)
l2 = [1, 2, 3]
result = cmp(t1, l2)
print(result)
