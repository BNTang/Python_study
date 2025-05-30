# -*- coding: utf-8 -*-

# @Time    : 2025-5-23
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 82-Python-常用数据类型操作-字典-常用操作-查-遍历

# 先遍历所有的key，然后，根据指定的key，获取对应的值
# d = {"name": "NEO", "age": 18, "address": "China"}

# # 1.先获取所有的key
# keys = d.keys()

# # 2.遍历所有的key
# for key in keys:
#     # 3.根据key获取对应的值
#     value = d[key]
#     print(f"key: {key}, value: {value}")

# 直接遍历所有的键值对
d = {"name": "NEO", "age": 18, "address": "China"}
d['iphone'] = '13'
for key, value in d.items():
    print(f"key: {key}, value: {value}")
