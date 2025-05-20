# -*- coding: utf-8 -*-

# @Time    : 2025-5-20 14:18:34
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 53-Python-常用数据类型操作-字符串-字符串切片

# 概念

# 获取一个字符串的某个片段

# name[下标]

# 字符串切片

# 获取某一个字符

# 下标

# 字符串中每个字符的编号

# 座位编号

# 下标越界

# 注意

# 负数下标

# 如果为负数,则会从尾部开始定位

# 最后一个字符为 -1

# name = "abcdefg"
# print(name[2])  # c
# print(name)

# name = "abcdefg"
# print(name[28])  # IndexError: string index out of range

# name = "abcdefg"
# print(name[-1])  # g
# print(name[-2])  # f
# print(name[-3])  # e
# print(name[-4])  # d

# name[起始:结束:步长]

# 获取范围

# [起始,结束)

# 起始包含

# 结束不包含

# 起始默认值:0

# 获取一个字符串片段

# 注意

# 默认值

# 结束默认值:len(name)·

# 整个字符串的长度

# 步长默认值:1

# 步长>0

# 从左边到右

# 获取顺序

# 步长<0· 从右往左

# 注意: 不能从头部跳到尾部,或者从尾部跳到头部

# 特殊案例

# 反转字符串

# 字符串[:.-1]

# name = "abcdefg"
# print(name[0:3])  # abc

# name = "abcdefg"
# print(name[::])
# print(name[0:len(name):1])
# print(len(name))

# print(name[0:len(name):2])

# name = "abcdefg"
# print(name[4:1:-1])  # edc
# print(name[-1:-4:-1])  # gfe

# print(name[::-1])  # gfedcba