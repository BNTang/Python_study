# -*- coding: utf-8 -*-

# @Time    : 2025-5-21 12:07:16
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 58-Python-常用数据类型操作-字符串-函数操作-分割拼接

# info = "neo-18-男-程序员"
# return_list = info.split("-")
# print(return_list)

# info = "neo-18-男-程序员-IT"
# return_list = info.split("-", 3)
# print(return_list)

# partition
# info = "neo-18-男-程序员"
# return_list = info.partition("-")
# print(return_list)

# info = "neo-18-男-程序员"
# return_list = info.partition("|")
# print(return_list)

# rpartition：根据分隔符从右侧进行分割
# info = "neo-18-男-程序员"
# return_list = info.rpartition("-")
# print(return_list)

# splitlines：根据换行符进行分割
# info = "neo-18-男-程序员\nIT"
# return_list = info.splitlines()
# print(return_list)

# info = "neo-18-男-程序员\nIT"
# return_list = info.splitlines(keepends=True)
# print(return_list)

# join：将列表中的元素拼接成字符串
# info = ["neo", "18", "男", "程序员"]
# return_str = "-".join(info)
# print(return_str)