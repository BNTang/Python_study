# -*- coding: utf-8 -*-

# @Time    : 2025-5-17 12:30:06
# @Author  : NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 36-Python-循环-循环和分支嵌套-和循环嵌套

# 1. 36-Python-循环-循环和分支嵌套-和循环嵌套
# 循环内嵌套循环
# 外循环循环一次内循环,循环所有
# 案例

# 示例1: 简单的嵌套循环 - 打印乘法表
print("示例1: 乘法表")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} × {i} = {i * j}", end="\t")
    print()  # 换行

print("\n" + "-" * 50)

# 示例2: 循环中嵌套分支 - 打印奇偶数
print("示例2: 循环中嵌套分支")
for i in range(1, 10):
    if i % 2 == 0:
        print(f"{i} 是偶数")
    else:
        print(f"{i} 是奇数")

print("\n" + "-" * 50)

# 示例3: 嵌套循环与分支结合 - 打印特定图案
print("示例3: 嵌套循环与分支结合")
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\n" + "-" * 50)

# 示例4: break和continue在嵌套循环中的使用
print("示例4: break和continue在嵌套循环中的使用")
for i in range(1, 6):
    print(f"外循环第 {i} 次")
    for j in range(1, 6):
        if j == 3:
            print(f"  遇到j=={j}，跳过本次内循环")
            continue
        if i == 4 and j == 4:
            print(f"  遇到i=={i}, j=={j}，提前结束内循环")
            break
        print(f"  内循环: i={i}, j={j}")

print("\n" + "-" * 50)

# 示例5: 实际应用 - 查找两个列表中的所有组合
print("示例5: 实际应用 - 查找组合")
fruits = ["苹果", "香蕉", "橙子"]
colors = ["红色", "黄色", "橙色"]

print("水果和颜色的组合:")
for fruit in fruits:
    for color in colors:
        print(f"{color}的{fruit}")