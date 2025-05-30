# -*- coding: utf-8 -*-

# @Time    : 2025-5-22 12:58:29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 78-Python-常用数据类型操作-字典-常用操作-删

# del：
# d = {"name": "NEO", "age": 18}
# # del d["name"]
# del d["name2"] # KeyError
# print(d)

# pop
# d = {"name": "NEO", "age": 18}
# # result = d.pop("name")
# # result = d.pop("name2") # KeyError
# result = d.pop("name2", "NEO")
# print(result)
# print(d)

# popitem
# d = {"name": "NEO", "age": 18, "gender": "男"}
# result = d.popitem()
# print(result)
# print(d)

# d = {}
# result = d.popitem()
# print(result)
# print(d)

# clear
d = {"name": "NEO", "age": 18, "gender": "男"}
result = d.clear()
print(result)
print(d)