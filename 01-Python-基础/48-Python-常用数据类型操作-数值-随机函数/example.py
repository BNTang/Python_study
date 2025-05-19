# -*- coding: utf-8 -*-

# @Time    : 2025-5-19 13:23:53
# @Author  : NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 48-Python-常用数据类型操作-数值-随机函数

# 范围之内的随机小数

# random(

# [0,1)·

# 随机函数

# 从一个序列中,随机挑选一个数值

# random.choice((1,3, 6,8))

# uniform(x,y)·[x,y]· 范围之内的随机小数

# randomint(x,y)· [x,y]· 范围之内的随机整数

# randrange(start, stop=None, step=1)

# choice(seq)

# 给定区间内的一随机整数

# [start, stop)

# random模块

# random：0,1，范围之内的随机小数
# import random
# print(random.random())  # 0.0 <= x < 1.0

# choice：从一个序列中,随机挑选一个数值
# print(random.choice((1, 3, 6, 8)))  # 随机挑选一个数值

# uniform：范围之内的随机小数
# print(random.uniform(1, 3))  # 1.0 <= x < 3.0

# randint：范围之内的随机整数
# print(random.randint(1, 3))  # 1 <= x <= 3

# randrange：给定区间内的一随机整数
# print(random.randrange(1, 3))  # 1 <= x < 3