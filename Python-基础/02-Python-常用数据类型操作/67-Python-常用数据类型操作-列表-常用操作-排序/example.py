# -*- coding: utf-8 -*-

# @Time    : 2025-5-22 12:58:29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 67-Python-常用数据类型操作-列表-常用操作-排序

# s = "abcdefghijklmnopqrscccctuvwxyz"
# result = sorted(s)
# print(result)

# s = "abcdefghijklmnopqrscccctuvwxyz"
# result = sorted(s, reverse=True)
# print(result)

# s = [1, 3, 2, 4, 5, 22, 2, 2, 4, 19]
# result = sorted(s, reverse=True)
# print(result)

# s = [1, 3, 2, 4, 5, 22, 2, 2, 4, 19]
# result = sorted(s)
# print(result)

# s = [("neo", 20), ("程序员neo", 18), ("财务neo", 19)]
# result = sorted(s)
# print(result)

# def get_key(item):
#     return item[1]

# s = [("neo", 20), ("程序员neo", 18), ("财务neo", 19)]
# result = sorted(s, key=get_key)
# print(result)

# s = [("neo", 20), ("程序员neo", 18), ("财务neo", 19)]
# result = sorted(s, key=get_key, reverse=True)
# print(result)

# l = [1, 3, 2, 4, 5, 22, 2, 2, 4, 19]
# result = l.sort()
# print(result)
# print(l)

def get_key(item):
    return item[1]

# s = [("neo", 20), ("程序员neo", 18), ("财务neo", 19)]
# result = s.sort(key=get_key)
# print(result)
# print(s)

s = [("neo", 20), ("程序员neo", 18), ("财务neo", 19)]
result = s.sort(key=get_key, reverse=True)
print(result)
print(s)