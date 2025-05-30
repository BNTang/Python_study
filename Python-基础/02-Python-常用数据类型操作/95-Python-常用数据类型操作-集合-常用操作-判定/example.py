# -*- coding: utf-8 -*-

# @Time    : 2025-5-24
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 95-Python-常用数据类型操作-集合-常用操作-判定

# 集合的判定操作
# 主要包括以下几种判定操作：
# 1. 判定两个集合是否不相交 (isdisjoint)
# 2. 判定一个集合是否包含另外一个集合 (issuperset)
# 3. 判定一个集合是否是另外一个集合的子集 (issubset)

print("=== 集合判定操作演示 ===")

# 创建两个集合
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(f"集合s1: {s1}")
print(f"集合s2: {s2}")

print("\n--- 1. isdisjoint() 判定两个集合是否不相交 ---")
# isdisjoint() 判断两个集合是否不相交（没有公共元素）
# 如果没有公共元素返回True，有公共元素返回False
result = s1.isdisjoint(s2)
print(f"s1.isdisjoint(s2): {result}")  # False，因为有公共元素3

# 修改s2，去掉公共元素3
s2 = {4, 5}
print(f"修改后的s2: {s2}")
result = s1.isdisjoint(s2)
print(f"s1.isdisjoint(s2): {result}")  # True，因为没有公共元素

print("\n--- 2. issuperset() 判定一个集合是否包含另外一个集合 ---")
# issuperset() 判断当前集合是否是另一个集合的超集（完全包含另一个集合）
s1 = {1, 2, 3}
s2 = {4, 5}
print(f"集合s1: {s1}")
print(f"集合s2: {s2}")
result = s1.issuperset(s2)
print(f"s1.issuperset(s2): {result}")  # False，s1不包含s2的所有元素

# 修改s1，使其包含s2的所有元素
s1 = {1, 2, 3, 4, 5}
print(f"修改后的s1: {s1}")
result = s1.issuperset(s2)
print(f"s1.issuperset(s2): {result}")  # True，s1包含s2的所有元素

print("\n--- 3. issubset() 判定一个集合是否是另外一个集合的子集 ---")
# issubset() 判断当前集合是否是另一个集合的子集
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5}
print(f"集合s1: {s1}")
print(f"集合s2: {s2}")
result = s2.issubset(s1)
print(f"s2.issubset(s1): {result}")  # True，s2是s1的子集

# 修改s2，添加s1中没有的元素
s2 = {3, 4, 5, 6}
print(f"修改后的s2: {s2}")
result = s2.issubset(s1)
print(f"s2.issubset(s1): {result}")  # False，s2不是s1的子集，因为6不在s1中

print("\n--- 总结 ---")
print("1. isdisjoint(): 判断两个集合是否不相交（没有公共元素）")
print("2. issuperset(): 判断当前集合是否包含另一个集合的所有元素")
print("3. issubset(): 判断当前集合是否是另一个集合的子集")
print("这些方法都返回布尔值True或False")
