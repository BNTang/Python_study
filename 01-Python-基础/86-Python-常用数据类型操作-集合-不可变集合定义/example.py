# -*- coding: utf-8 -*-

# @Time    : 2025-5-23
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 86-Python常用数据类型操作-集合-不可变集合定义

# 不可变集合frozenset

# fs = frozenset(iterable)

# 其中iterable可以是字符串、列表、元组、字典等

# 但是为dict时，只会获取提Key作为set的元素

# 集合推导式

# s=frozenset(x**2 forxin range(1,10)ifx%2 ==0)