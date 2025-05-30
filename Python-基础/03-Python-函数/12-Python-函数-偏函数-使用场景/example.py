# -*- coding: utf-8 -*-

# @Time    : 2025-5-28
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 12-Python-函数-偏函数-使用场景

import functools

print("=== 偏函数使用场景演示 ===")

# 场景：需要将多个二进制字符串转换为十进制数字
# int() 函数可以指定进制：int(string, base)

# 1. 传统方式：每次都要指定 base=2
numbers = "10010"
result = int(numbers, 2)  # 第二个参数指定二进制
print(f"传统方式: int('{numbers}', 2) = {result}")

# 2. 创建偏函数：固定 base=2 参数
# 关键概念：偏函数可以固定某些参数，简化函数调用
int2 = functools.partial(int, base=2)

# 使用偏函数（更简洁）
result2 = int2(numbers)  # 只需要传入字符串，base=2 已固定
print(f"偏函数方式: int2('{numbers}') = {result2}")

print("\n=== 批量处理演示 ===")
# 实际应用场景：批量转换多个二进制字符串
binary_strings = ["1010", "1111", "10010", "11000", "101"]

# 传统方式：需要重复写 base=2
print("传统方式（重复代码）:")
for binary in binary_strings:
    decimal = int(binary, 2)  # 每次都要写 base=2
    print(f"  {binary} -> {decimal}")

print("\n偏函数方式（简洁高效）:")
for binary in binary_strings:
    decimal = int2(binary)  # 只需要传入字符串
    print(f"  {binary} -> {decimal}")

print("\n=== 偏函数核心概念 ===")
print("1. 偏函数固定原函数的某些参数")
print("2. 创建新函数，减少重复代码")
print("3. 语法：functools.partial(原函数, 参数名=固定值)")
print("4. 适用场景：频繁调用同一函数且某些参数相同")
