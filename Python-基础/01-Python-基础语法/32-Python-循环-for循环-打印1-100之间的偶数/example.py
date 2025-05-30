# -*- coding: utf-8 -*-

# @Time    : 2025-5-17 12:30:06
# @Author  : NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 32-Python-循环-for循环-打印1-100之间的偶数

# 1. 32-Python-循环-for循环-打印1-100之间的偶数
# 打印1-100之间的偶数
# 1-100这样的集合
# 函数 -> range(1, 101)
# 1. range(1, 101) -> 1-100
# 什么是偶数？能被2整除的数不能被2整除的数是奇数
# 什么是 range(1, 101)？ range(1, 101) 是一个函数，表示从1到100的数字集合，1,100 只会包含整数 1-99不会生成的是100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)