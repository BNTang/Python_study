# -*- coding: utf-8 -*-

# @Time    : 2025-5-20 14:18:34
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 55-Python-常用数据类型操作-字符串-函数操作-查找计算

# len
# name = "Python"
# num = len(name)
# print("字符串长度为：", num)

# name = "我是 Python"
# num = len(name)
# print("字符串长度为：", num)

# name = "我是 Python\n"
# num = len(name)
# print("字符串长度为：", num)

# name = "我是\nPython"
# num = len(name)
# print("字符串长度为：", num)

# find：查找子串索引（下标）的位置
# name = "wo shi sz"
# num = name.find("shi")
# print("子串索引位置为：", num)

# 注意点是从左往右进行查找
# name = "wo shi sz"
# num = name.find("s")
# print("子串索引位置为：", num)

# 如果没有找到，返回-1
# name = "wo shi sz"
# num = name.find("x")
# print("子串索引位置为：", num)

# 从指定位置开始查找
# name = "wo shi sz"
# num = name.find("s", 4)
# print("子串索引位置为：", num)

# name = "wo shi sz"
# num = name.find("s", 0, 4)
# print("子串索引位置为：", num)

# rfind：从右往左查找子串索引（下标）的位置
# name = "wo shi sz"
# num = name.rfind("s")
# print("子串索引位置为：", num)

# 注意点是从右往左进行查找
# name = "wo shi sz"
# num = name.rfind("shi")
# print("子串索引位置为：", num)

# 如果没有找到，返回-1
# name = "wo shi sz"
# num = name.rfind("x")
# print("子串索引位置为：", num)

# index：查找子串索引（下标）的位置
# name = "wo shi sz"
# num = name.index("shi")
# print("子串索引位置为：", num)

# 注意点是从左往右进行查找
# name = "wo shi sz"
# num = name.index("s")
# print("子串索引位置为：", num)

# 如果没有找到，抛出异常
# name = "wo shi sz"
# num = name.index("x")
# print("子串索引位置为：", num)

# rindex：从右往左查找子串索引（下标）的位置
# name = "wo shi sz"
# num = name.rindex("s")
# print("子串索引位置为：", num)

# 注意点是从右往左进行查找
# name = "wo shi sz"
# num = name.rindex("shi")
# print("子串索引位置为：", num)

# 如果没有找到，抛出异常
# name = "wo shi sz"
# num = name.rindex("x")
# print("子串索引位置为：", num)

# count：统计子串出现的次数
# name = "wo shi sz"
# num = name.count("s")
# print("子串出现的次数为：", num)

# name = "wo shi sz"
# num = name.count("shi")
# print("子串出现的次数为：", num)

# name = "wo shi sz"
# num = name.count("x")
# print("子串出现的次数为：", num)

# name = "wo shi sz"
# num = name.count("s", 0, 4)
# print("子串出现的次数为：", num)