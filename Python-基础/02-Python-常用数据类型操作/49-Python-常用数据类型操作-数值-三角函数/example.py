# -*- coding: utf-8 -*-

# @Time    : 2025-5-19 13:23:53
# @Author  : NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 49-Python-常用数据类型操作-数值-三角函数

# sin(x)正弦

# 三角函数

# cos(x)

# 。 余弦

# tan(x)

# 正切

# 反正弦

# asin(x)

# 反余弦

# acos(x)

# 反正切

# atan(x)

# math模块

# degrees(x)· 弧度 ->角度

# 角度 ->弧度

# radians(x)

# 数学常量

# pi N

# 数学中的π · 3.14...
import math

# sin：正弦，接收一个弧度值（角度），返回一个正弦值
# print(math.sin(30))  # 0.49999999999999994

# pi = 180
# hudu = 30 / 180 * pi
# hudu = 1 / 6 * math.pi
hudu = math.radians(30)  # 30° -> 弧度
result = math.sin(hudu)
print(result)  # 0.49999999999999994