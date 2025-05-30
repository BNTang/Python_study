# -*- coding: utf-8 -*-

# @Time    : 2025-5-22 12:58:29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 79-Python-常用数据类型操作-字典-常用操作-改

# 只能改值，不能改 key，dict[key] = value
# d = {'a': 1, 'b': 2, 'c': 3}
# d['a'] = 100
# print(d)

# 如果key不存在就是新增
# d = {'a': 1, 'b': 2, 'c': 3}
# d['d'] = 4
# print(d)

# 批量修改键值对
# d = {'a': 1, 'b': 2, 'c': 3}
# d.update({'a': 100, 'b': 200})
# print(d)

# 批量修改如果key不存在就是新增
# d = {'a': 1, 'b': 2, 'c': 3}
# d.update({'d': 4, 'e': 5})
# print(d)