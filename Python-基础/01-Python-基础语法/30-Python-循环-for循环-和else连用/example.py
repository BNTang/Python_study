# -*- coding: utf-8 -*-

# @Time    : 2025-5-17 12:30:06
# @Author  : NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 30-Python-循环-for循环-和else连用

# 1. 使用 for 循环遍历列表
# for x in xxx:
# 条件满足时的执行代码
# else:
# 与else连用
# 语法
# 注意
# 条件不满足时执行的语句
# 如果for派环可以顺利的执行完毕，则会执行else反之，使用了break则不会

name = ['NEO', 'BNTang', 'Python']

for x in name:
    print(x)
    break
else:
    print("循环结束")