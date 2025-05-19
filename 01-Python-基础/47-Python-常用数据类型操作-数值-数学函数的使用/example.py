# -*- coding: utf-8 -*-

# @Time    : 2025-5-19 13:23:53
# @Author  : NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 47-Python-常用数据类型操作-数值-数学函数的使用

# 适用于几乎所有Pvthon运算符

# 导入对应模块

# 例如: import math

# 部分函数使用前注意

# 使用函数时

# 模块名.函数名(参数)

# math.fabs(-10)

# abs(num)

# max(num1, num2...)

# min(num1, num2...)

# 内建函数

# round(numl, n])

# 常用操作

# 数学函数

# powix, y)

# -----------分割线

# ceil(num)

# +

# floor(num)

# sqrt(num)

# math模块函数

# 随机函数

# log(x, base)

# 内建函数
# 绝对值函数
# num = -10
# print(abs(num))  # 10

# 最大值
# print(max(1, 2, 3, 4, 5))  # 5
# 最小值
# print(min(1, 2, 3, 4, 5))  # 1
# print(min([1, 2, 3, 4, 5]))  # 1
# 四舍五入
# print(round(1.5))  # 2
# round 第二个参数表示四舍五入的位数，什么意思呢，假如我想保留两位，直接写一个2就行了
# 例如：3.147，通过round(3.147, 2)就可以保留两位小数了，运行过程是
# 3.147 * 100 =314.7，314.7四舍五入为315，315/100=3.15
# print(round(3.147, 2))  # 3.15
# print(round(3.147, 1))  # 3.1

# pow：幂运算，返回 x的y次方，x ** y
# print(pow(2, 3))  # 8
# print(2 ** 3)  # 8

# math模块函数
# 导入math模块
# import math
# math模块函数

# math.ceil：向上取整
# print(math.ceil(3.1))  # 4

# math.floor：向下取整
# print(math.floor(3.9))  # 3

# math.sqrt：开平方
# print(math.sqrt(9))  # 3.0

# math.log：对数
# x: 对数的底数
# base: 对数的底数
# 例如：log(100, 10) = 2
# 10的2次方等于100
# print(math.log(100, 10))  # 2.0