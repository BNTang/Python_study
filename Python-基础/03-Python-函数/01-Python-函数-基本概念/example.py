# -*- coding: utf-8 -*-

# @Time    : 2025-5-26
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 01-Python-函数-基本概念

"""
关于Python的函数基本概念

函数的定义：
- 写了一段代码来实现某些功能
- 把这些代码集中到一块，起一个名字
- 下次可以根据这个名字再次使用这个代码块

函数的重要作用：
1. 方便代码的重用
2. 分解任务，简化程序逻辑  
3. 使代码更加模块化
"""

print("=" * 50)
print("演示：不使用函数的问题")
print("=" * 50)

# 问题演示：代码重复的坏处
print("第一次打印1-9：")
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)

print("\n第二次打印1-9：")
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)

print("\n第三次打印1-9：")
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)

print("\n" + "=" * 50)
print("问题分析：")
print("1. 文件大小会变大")
print("2. 代码冗余度比较大") 
print("3. 重用性比较差")
print("4. 可维护性比较差")
print("=" * 50)

print("\n" + "=" * 50)
print("解决方案：使用函数")
print("=" * 50)

# 解决方案：定义函数
def print_func():
    """打印1-9的函数"""
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
    print(6)
    print(7)
    print(8)
    print(9)

# 使用函数
print("使用函数第一次调用：")
print_func()

print("\n使用函数第二次调用：")
print_func()

print("\n使用函数第三次调用：")
print_func()

print("\n" + "=" * 50)
print("函数的优势：")
print("1. 文件体积变小")
print("2. 代码冗余度基本没有")
print("3. 重用性好")
print("4. 可维护性高（只需修改一个地方）")
print("=" * 50)

# 演示可维护性
def print_func_improved():
    """改进版打印函数，偶数前加1"""
    print(1)
    print(1, 2)  # 偶数前加1
    print(3)
    print(1, 4)  # 偶数前加1
    print(5)
    print(1, 6)  # 偶数前加1
    print(7)
    print(1, 8)  # 偶数前加1
    print(9)

print("\n演示可维护性 - 偶数前加1：")
print_func_improved()

print("\n" + "=" * 50)
print("函数的分类")
print("=" * 50)

# 1. 内建函数（Python自带）
print("1. 内建函数示例：")
print(f"len('hello'): {len('hello')}")
print(f"max(1, 2, 3): {max(1, 2, 3)}")
print(f"type(123): {type(123)}")

# 2. 第三方函数（需要导入模块）
print("\n2. 第三方函数示例：")
import math
print(f"math.sqrt(16): {math.sqrt(16)}")
print(f"math.pi: {math.pi}")

import random
print(f"random.randint(1, 10): {random.randint(1, 10)}")

# 3. 自定义函数（我们自己写的）
print("\n3. 自定义函数示例：")

def greet(name):
    """自定义问候函数"""
    return f"Hello, {name}!"

def calculate_area(length, width):
    """计算矩形面积的自定义函数"""
    return length * width

def print_separator(char="=", length=30):
    """打印分隔线的自定义函数"""
    print(char * length)

# 使用自定义函数
print(greet("Python学习者"))
print(f"矩形面积: {calculate_area(5, 3)}")
print_separator("-", 40)

print("\n" + "=" * 50)
print("函数的其他作用演示")
print("=" * 50)

# 分解任务，简化程序逻辑
def step1():
    """任务步骤1"""
    print("执行步骤1：初始化数据")

def step2():
    """任务步骤2""" 
    print("执行步骤2：处理数据")

def step3():
    """任务步骤3"""
    print("执行步骤3：输出结果")

def main_task():
    """主任务：通过函数分解复杂任务"""
    print("开始执行主任务：")
    step1()
    step2() 
    step3()
    print("主任务完成！")

# 执行主任务
main_task()

print("\n" + "=" * 50)
print("总结：")
print("函数是Python编程的重要概念")
print("合理使用函数可以让代码更优雅、更易维护")
print("=" * 50)
