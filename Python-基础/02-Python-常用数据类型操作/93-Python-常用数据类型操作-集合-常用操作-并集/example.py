# -*- coding: utf-8 -*-

# @Time    : 2025-5-24
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 93-Python-常用数据类型操作-集合-常用操作-并集

print("=" * 50)
print("Python集合并集操作详解")
print("=" * 50)

# 什么是并集？
# 并集是指两个或多个集合中所有元素的组合，重复元素只保留一个
# 例如：集合A = {1, 2, 3}，集合B = {3, 4, 5}
# A和B的并集 = {1, 2, 3, 4, 5}

print("\n1. 基本集合定义")
print("-" * 30)

# 定义两个集合
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(f"集合s1: {s1}")
print(f"集合s2: {s2}")
print(f"期望的并集结果: {1, 2, 3, 4, 5}")

print("\n2. 使用union()方法求并集")
print("-" * 30)

# 方法一：使用union()方法
result = s1.union(s2)
print(f"s1.union(s2) = {result}")
print(f"原集合s1未发生变化: {s1}")
print(f"原集合s2未发生变化: {s2}")

print("\n3. 使用逻辑或运算符|求并集")
print("-" * 30)

# 方法二：使用逻辑或运算符 |
result2 = s1 | s2
print(f"s1 | s2 = {result2}")
print(f"原集合s1未发生变化: {s1}")
print(f"原集合s2未发生变化: {s2}")

print("\n4. 不可变集合(frozenset)的并集操作")
print("-" * 30)

# 如果左侧是不可变集合，结果也是不可变集合
frozen_s1 = frozenset({1, 2, 3})
s3 = {3, 4, 5}

result3 = frozen_s1 | s3
print(f"frozen_s1: {frozen_s1} (类型: {type(frozen_s1).__name__})")
print(f"s3: {s3} (类型: {type(s3).__name__})")
print(f"frozen_s1 | s3 = {result3} (类型: {type(result3).__name__})")

print("\n5. 使用update()方法更新并集")
print("-" * 30)

# 方法三：使用update()方法（会修改原集合）
s4 = {1, 2, 3}
s5 = {3, 4, 5}

print(f"更新前s4: {s4}")
print(f"s5: {s5}")

# update()方法没有返回值，直接修改原集合
s4.update(s5)
print(f"s4.update(s5)后，s4变为: {s4}")

print("\n6. 多个集合的并集操作")
print("-" * 30)

# 多个集合求并集
set_a = {1, 2}
set_b = {2, 3}
set_c = {3, 4}

# 使用union()方法
multi_union1 = set_a.union(set_b, set_c)
print(f"set_a.union(set_b, set_c) = {multi_union1}")

# 使用|运算符
multi_union2 = set_a | set_b | set_c
print(f"set_a | set_b | set_c = {multi_union2}")

# 使用update()方法
set_d = {1, 2}
set_d.update(set_b, set_c)
print(f"update()方法更新后的set_d: {set_d}")

print("\n7. 性能对比和使用建议")
print("-" * 30)

import time

# 创建较大的集合进行性能测试
large_set1 = set(range(10000))
large_set2 = set(range(5000, 15000))

# 测试union()方法
start_time = time.time()
result_union = large_set1.union(large_set2)
union_time = time.time() - start_time

# 测试|运算符
start_time = time.time()
result_or = large_set1 | large_set2
or_time = time.time() - start_time

print(f"union()方法耗时: {union_time:.6f}秒")
print(f"|运算符耗时: {or_time:.6f}秒")
print(f"结果集合大小: {len(result_union)}")

print("\n8. 总结")
print("-" * 30)
print("集合并集操作的三种方法：")
print("1. union()方法：不修改原集合，返回新集合")
print("2. |运算符：不修改原集合，返回新集合，语法更简洁")
print("3. update()方法：直接修改原集合，适用于可变集合")
print("4. 如果左侧是frozenset，结果也是frozenset")
print("5. 性能上，|运算符通常略快于union()方法")

print("\n学习完成！")
