# -*- coding: utf-8 -*-

# @Time    : 2025-5-22 12:58:29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 77-Python-常用数据类型操作-字典-常用操作-增

# 增，当key在原字典中不存在时，即为新增操作
d = {"name": "NEO", "age": 18}
print(type(d))
print(d)
print(id(d))

# 新增
d["gender"] = "男"
print(d)
print(id(d))