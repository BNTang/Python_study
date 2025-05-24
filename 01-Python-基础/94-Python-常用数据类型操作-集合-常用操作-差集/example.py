# -*- coding: utf-8 -*-

# @Time    : 2025-5-24
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 94-Python-常用数据类型操作-集合-常用操作-差集

"""
差集操作说明：
假设有两个集合 a 和 b
a 相对于 b 的差集是指：属于 a 但不属于 b 的元素集合
如果用图表示，就是 a 中去掉与 b 重叠部分后剩余的部分
"""

print("=== Python 集合差集操作演示 ===")
print()

# 1. 创建两个集合
print("1. 创建两个集合：")
S1 = {1, 2, 3}
S2 = {3, 4, 5}
print(f"S1 = {S1}")
print(f"S2 = {S2}")
print()

# 2. 使用 difference() 方法计算差集
print("2. 使用 difference() 方法计算差集：")
result = S1.difference(S2)
print(f"S1.difference(S2) = {result}")
print(f"S1 本身 = {S1}")  # 原集合不变
print("说明：S1 相对于 S2 的差集是 {1, 2}，因为 3 在 S2 中")
print()

# 3. 使用减号操作符计算差集
print("3. 使用减号操作符计算差集：")
result2 = S1 - S2
print(f"S1 - S2 = {result2}")
print(f"S1 本身 = {S1}")  # 原集合不变
print("说明：减号操作符与 difference() 方法效果相同")
print()

# 4. 使用 difference_update() 方法（会修改原集合）
print("4. 使用 difference_update() 方法（会修改原集合）：")
S1_copy = S1.copy()  # 先复制一份用于演示
print(f"操作前 S1_copy = {S1_copy}")
result3 = S1_copy.difference_update(S2)  # 返回 None
print(f"S1_copy.difference_update(S2) 返回值 = {result3}")
print(f"操作后 S1_copy = {S1_copy}")
print("说明：difference_update() 直接修改原集合，返回 None")
print()

# 5. 更多差集示例
print("5. 更多差集示例：")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {2, 4, 6, 8}

print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print()

print(f"A - B = {A - B}")  # A 中不在 B 中的元素
print(f"B - A = {B - A}")  # B 中不在 A 中的元素
print(f"A - C = {A - C}")  # A 中不在 C 中的元素
print()

# 6. 空集合的差集操作
print("6. 空集合的差集操作：")
empty_set = set()
print(f"empty_set = {empty_set}")
print(f"A - empty_set = {A - empty_set}")  # 任何集合减去空集合等于自身
print(f"empty_set - A = {empty_set - A}")  # 空集合减去任何集合等于空集合
print()

print("=== 差集操作总结 ===")
print("1. difference() 方法：返回新集合，不修改原集合")
print("2. 减号操作符(-)：与 difference() 方法效果相同")
print("3. difference_update() 方法：直接修改原集合，返回 None")
print("4. 差集是不对称操作：A - B ≠ B - A（一般情况下）")
