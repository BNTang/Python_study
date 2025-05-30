# -*- coding: utf-8 -*-

# @Time    : 2025-5-23
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 80-Python-常用数据类型操作-字典-常用操作-查-单个值

# dict[key]
# d = {"name": "neo", "age": 18}
# print(d["name"])  # neo
# print(d["age"])  # 18

# key不存在会报错
# print(d["gender"]) # KeyError

# 使用get方法
# d = {"name": "neo", "age": 18}
# print(d.get("name"))  # neo
# print(d.get("age"))  # 18

# 如果get根据key查找不到值，返回None
# d = {"name": "neo", "age": 18}
# print(d.get("gender"))  # None

# 如果key不存在，返回默认值
# d = {"name": "neo", "age": 18}
# print(d.get("gender", "unknown"))  # unknown

# 使用 setdefault方法
# d = {"name": "neo", "age": 18}
# print(d.setdefault("name"))  # neo

# 如果key不存在，则返回给定默认值，并返回该默认值
# d = {"name": "neo", "age": 18}
# print(d.setdefault("gender", "unknown"))  # unknown

# 如果key不存在，则返回默认值，并添加到字典中
d = {"name": "neo", "age": 18}
print(d.setdefault("gender"))  # None