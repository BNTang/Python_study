# -*- coding: utf-8 -*-

# @Time    : 2025-5-17 12:30:06
# @Author  : NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 31-Python-循环-for循环-反转字符串

# 1. 31-Python-循环-for循环-反转字符串
# 反转字符串，源字符串："社会我NEO哥，人狠话不多"，反转后："多不话狠人，哥NEO我会社"
# notice = "社会我NEO哥，人狠话不多"

# 拆字
# result = ""
# for c in notice:
    # result += c
    # print(c)

# print(result)

notice = "社会我NEO哥，人狠话不多"
result = ""
for c in notice:
    result = c + result

print(result)