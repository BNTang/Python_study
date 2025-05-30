# -*- coding: utf-8 -*-

# @Time    : 2025-5-23
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 81-Python-常用数据类型操作-字典-常用操作-查-所有键-值-键值对

# 获取所有的值
# 1. values() 方法
# d = {"name": "NEO", "age": 18}
# result = d.values()
# print(result) # dict_values(['NEO', 18])

# 2. items() 方法
# d = {"name": "NEO", "age": 18}
# result = d.items()
# print(result) # dict_items([('name', 'NEO'), ('age', 18)])

# 3. keys() 方法
# d = {"name": "NEO", "age": 18}
# result = d.keys()
# print(result) # dict_keys(['name', 'age'])

# d = {"name": "NEO", "age": 18}

# vs = d.values()
# its = d.items()
# ks = d.keys()

# print("所有的值：", vs, its, ks)

# d['address'] = 'China'
# print(d)

# print("所有的值：", vs, its, ks)

# Python 2.x 与 Python 3.x 获取键获取值是有区别的
# Python 2.x，获取键值，老的与新的是完全两个不相同的对象内容
# Python 3.x，获取键值，老的与新的是完全两个相同的对象内容

# Dictionary ViewObjects，Python 2 是列表

# Python2.x和Python3.x版本之间关于获取键,获取值, 获取item, 之间的区别

# Python2.x直接是一个列表

# 可通过下标进行获取指定元素

# Python3.x 中是Dictionary view objects 

# 注意

# 在Python2.x中提供了如下方法

# viewkeys()

# viewvalues()

# viewitems()

# 作用如同Python3.x中的

# Dictionary view objects