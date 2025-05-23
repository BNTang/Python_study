# -*- coding: utf-8 -*-

# @Time    : 2025-5-23
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 83-Python-常用数据类型操作-字典-常用操作-计算-判定

# 计算，len
d = {"name": "NEO", "age": 18, "address": "China"}
print(len(d))

# 判定，in,not in
print("name" in d)
print("name" not in d)

# has_key python3 中已经废弃,python2 中使用
print(d.has_key("name"))
print(d.has_key("name1"))
