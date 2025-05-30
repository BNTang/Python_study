# -*- coding: utf-8 -*-

# @Time    : 2025-5-24
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 91-Python-常用数据类型操作-集合-常用操作-交集

"""
集合的交集操作
交集是指两个集合中共同存在的元素组成的集合
"""

print("=" * 50)
print("集合交集操作演示")
print("=" * 50)

# 1. 基本交集操作 - intersection() 方法
print("\n1. 使用 intersection() 方法求交集:")
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6}

result = s1.intersection(s2)
print(f"s1 = {s1}")
print(f"s2 = {s2}")
print(f"s1.intersection(s2) = {result}")
print(f"结果类型: {type(result)}")

# 2. 使用 & 运算符求交集
print("\n2. 使用 & 运算符求交集:")
result2 = s1 & s2
print(f"s1 & s2 = {result2}")
print(f"结果类型: {type(result2)}")

# 3. 可变集合与不可变集合的交集操作
print("\n3. 可变集合与不可变集合的交集:")

# 不可变集合在前面
s1_frozen = frozenset({1, 2, 3, 4, 5})
s2_normal = {4, 5, 6}

result3 = s1_frozen.intersection(s2_normal)
print(f"不可变集合 s1_frozen = {s1_frozen}")
print(f"可变集合 s2_normal = {s2_normal}")
print(f"s1_frozen.intersection(s2_normal) = {result3}")
print(f"结果类型: {type(result3)} (以左侧为准)")

# 可变集合在前面
result4 = s2_normal.intersection(s1_frozen)
print(f"\ns2_normal.intersection(s1_frozen) = {result4}")
print(f"结果类型: {type(result4)} (以左侧为准)")

# 使用 & 运算符的情况
print("\n使用 & 运算符:")
result5 = s1_frozen & s2_normal
print(f"s1_frozen & s2_normal = {result5}")
print(f"结果类型: {type(result5)}")

result6 = s2_normal & s1_frozen
print(f"s2_normal & s1_frozen = {result6}")
print(f"结果类型: {type(result6)}")

# 4. intersection_update() 方法 - 就地修改
print("\n4. intersection_update() 方法 - 就地修改:")

# 注意：frozenset 没有 intersection_update 方法，因为它是不可变的
s1_copy = {1, 2, 3, 4, 5}
s2_copy = {4, 5, 6}

print(f"修改前 s1_copy = {s1_copy}")
print(f"修改前 s2_copy = {s2_copy}")

# intersection_update 会修改调用它的集合
result7 = s1_copy.intersection_update(s2_copy)
print(f"\ns1_copy.intersection_update(s2_copy) 返回值: {result7}")
print(f"返回值类型: {type(result7)}")
print(f"修改后 s1_copy = {s1_copy}")  # s1_copy 被修改了
print(f"修改后 s2_copy = {s2_copy}")  # s2_copy 没有变化

# 5. 演示 frozenset 不能使用 intersection_update
print("\n5. frozenset 不支持 intersection_update:")
try:
    s1_frozen.intersection_update(s2_normal)
except AttributeError as e:
    print(f"错误: {e}")
    print("原因: frozenset 是不可变的，没有 intersection_update 方法")

# 6. 多个集合的交集
print("\n6. 多个集合的交集:")
s1_multi = {1, 2, 3, 4, 5}
s2_multi = {3, 4, 5, 6, 7}
s3_multi = {4, 5, 7, 8, 9}

result_multi = s1_multi.intersection(s2_multi, s3_multi)
print(f"s1_multi = {s1_multi}")
print(f"s2_multi = {s2_multi}")
print(f"s3_multi = {s3_multi}")
print(f"三个集合的交集: {result_multi}")

print("\n" + "=" * 50)
print("总结:")
print("1. intersection() 方法和 & 运算符都可以求交集")
print("2. 返回结果的类型以运算符左侧的集合类型为准")
print("3. intersection_update() 会就地修改调用者，返回 None")
print("4. frozenset 不支持 intersection_update() 方法")
print("5. intersection() 可以接受多个参数求多个集合的交集")
print("=" * 50)
