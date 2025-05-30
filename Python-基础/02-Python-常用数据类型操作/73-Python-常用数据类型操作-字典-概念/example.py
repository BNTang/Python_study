# -*- coding: utf-8 -*-

# @Time    : 2025-5-22 12:58:29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 73-Python-常用数据类型操作-字典-概念

# 表示一个人的一些信息，比如姓名、年龄、性别、身高、体重、地址等

# str1 = "neo,20,男,180,70,北京"
# infos = str1.split(",")
# print(infos)

# l = ["neo", 20, "男", 180, 70, "北京"]
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])
# print(l[5])

# t = ("neo", 20, "男", 180, 70, "北京")
# print(t[0])
# print(t[1])
# print(t[2])
# print(t[3])
# print(t[4])
# print(t[5])

# 字典
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中。
# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

# person = {"name": "neo", "age": 20, "gender": "男", "height": 180, "weight": 70, "address": "北京"}
# print(type(person))
# print(person["name"])
# print(person["age"])
# print(person["gender"])
# print(person["height"])
# print(person["weight"])
# print(person["address"])

# fromkeys：创建一个字典
# 语法：dict.fromkeys(seq, value)
# 参数：seq：一个序列，用于指定字典的键
# value：用于指定字典的值，默认为None
# 返回值：一个字典

# 正确示例
# keys = ["name", "age", "gender", "height", "weight", "address"]
# person = dict.fromkeys(keys, "未知")
# print(person)