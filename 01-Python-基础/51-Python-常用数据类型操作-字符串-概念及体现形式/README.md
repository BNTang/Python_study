# -*- coding: utf-8 -*-

# @Time    : 2025-5-19 13:23:53
# @Author  : NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 51-Python-常用数据类型操作-字符串-概念及体现形式

# 概念

# 由单个字符组成的一个集合

# 使用单引号包含的

# 'abc'

# e

# 非原始字符串

# 使用双引号包含的

# "abcr

# " abc "

# 使用3个单引号

# 使用3个双引号 。

# """ abC

# # H H

# 形式

# 原始字符串

# 4

# 概念

# 通过转换某个指定的字符,使它具备特殊的含义

# e

# 字符串

# 转义符

# 概念补充

# 常见转义符

# \(在行尾时)

# 单引号

# 双引号

# \n

# 换行

# 续行符

# 工的些上

# 向制表符

# 非原始字符串
# 使用单引号包含的
# str = 'aaa'
# print(str, type(str))

# 使用双引号包含的
# str = "aaa"
# print(str, type(str))

# 使用3个单引号
# str = '''aaa'''
# print(str, type(str))

# 使用3个双引号
# str = """aaa"""
# print(str, type(str))

# 转义符

# 概念补充

# 概念

# 通过转换某个指定的字符,使它具备特殊的含义

# ((在行尾时)

# 续行符

# 单引号

# 常见转义符

# 双引号

# 换行

# 横向制表符

# 为什么称之为原始字符串
# 原始字符串是指在字符串中不对反斜杠进行转义的字符串
# 例如：在字符串中使用反斜杠时，反斜杠后面的字符不会被解释为转义字符，而是作为普通字符处理
# str = """a\naa"""
# print(str, type(str))

# str = """a\taa"""
# print(str, type(str))

# 我是 "sz"
# print("我是 \"sz\"")
# print("我是 \'sz\'")

# 续行符
# str = "aaa" \
    #   "bbb"

# print(str, type(str))

# 我是 \n
# print("我是 \\n")

# 原始字符串
# str = r"aaa\n"
# print(str, type(str))

# 原始字符串

# 使用单引号包含的

# r'abc

# r"abc"

# 使用双引号包含的

# r"" abc "

# 使用3个单引号

# r""" abc """

# 使用3个双引号 。

