# -*- coding: utf-8 -*-

# @Time    : 2025-5-21 12:07:16
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 59-Python-常用数据类型操作-字符串-函数操作-判定

# isalpha：判断字符串是否只包含字母
# 正确示范
# info = "neo"
# return_bool = info.isalpha()
# print(return_bool)

# 错误示范
# info = "neo123"
# return_bool = info.isalpha()
# print(return_bool)

# 注意事项：
# 1. isalpha()方法只会判断字母，不会判断数字和其他字符

# isdigit：判断字符串是否只包含数字
# 正确示范
# info = "123"
# return_bool = info.isdigit()
# print(return_bool)

# 错误示范
# info = "123abc"
# return_bool = info.isdigit()
# print(return_bool)

# isalnum：判断字符串是否只包含字母和数字
# 正确示范
# info = "neo123"
# return_bool = info.isalnum()
# print(return_bool)

# 错误示范
# info = "neo-123"
# return_bool = info.isalnum()
# print(return_bool)

# isspace：判断字符串是否只包含空格
# 正确示范
# info = " "
# return_bool = info.isspace()
# print(return_bool)

# 错误示范
# info = " 123 "
# return_bool = info.isspace()
# print(return_bool)

# startswith：判断字符串是否以指定的字符开头
# 正确示范
# info = "2018-09-02：某某文件.xlsx"
# return_bool = info.startswith("2018")
# print(return_bool)

# 错误示范
# info = "2018-09-02：某某文件.xlsx"
# return_bool = info.startswith("2019")
# print(return_bool)

# endswith：判断字符串是否以指定的字符结尾
# 正确示范
# info = "2018-09-02：某某文件.xlsx"
# return_bool = info.endswith(".xlsx")
# print(return_bool)

# 错误示范
# info = "2018-09-02：某某文件.xlsx"
# return_bool = info.endswith(".xls")
# print(return_bool)

# in：判断字符串是否包含指定的字符
# 正确示范
# info = "2018-09-02：某某文件.xlsx"
# return_bool = "2018" in info
# print(return_bool)

# 错误示范
# info = "2018-09-02：某某文件.xlsx"
# return_bool = "2019" in info
# print(return_bool)

# not in：判断字符串是否不包含指定的字符
# 正确示范
# info = "2018-09-02：某某文件.xlsx"
# return_bool = "2019" not in info
# print(return_bool)

# 错误示范
# info = "2018-09-02：某某文件.xlsx"
# return_bool = "2018" not in info
# print(return_bool)