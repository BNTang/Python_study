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
name_list = ['程序员NEO', '程序员小张', '程序员小李']
print(name_list)

print(type(name_list))

names = ['程序员NEO', True, 123]
print(names)

names = []
print(type(names))
print(names)

items = ["a", "b", "c"]
names = [1, 2, 3, items]
print(names)
print(type(names))

# 2. 使用list()函数
name_list = list(['程序员NEO', '程序员小张', '程序员小李'])
print(name_list)

print(type(name_list))

# 3. 使用range()函数
name_list = list(range(10))
print(name_list)

