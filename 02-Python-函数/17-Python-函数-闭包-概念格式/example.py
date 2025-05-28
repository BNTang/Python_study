# -*- coding: utf-8 -*-

# @Time    : 2025-5-28
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 17-Python-函数-闭包-概念格式

"""
Python 闭包 (Closure) 学习重点：

闭包的三个条件：
1. 函数嵌套 - 外层函数包含内层函数
2. 内层函数引用外层函数的变量/参数
3. 外层函数返回内层函数对象（不是调用）

核心概念：内层函数 + 引用的外层变量 = 闭包
"""

# ==================== 基础闭包示例 ====================
def test():  # 外层函数
    a = 10   # 外层变量
    
    def test2():  # 内层函数
        print(a)  # 内层函数引用外层变量
    
    return test2  # 返回内层函数对象(不是调用)

# 使用闭包
new_function = test()  # 获取内层函数
new_function()  # 调用内层函数，输出: 10

print("=" * 50)

# ==================== 带参数的闭包 ====================
def outer_func(c):  # 外层函数接收参数
    a = 666  # 外层变量
    
    def inner_func():  # 内层函数
        print(f"外层变量 a = {a}")
        print(f"外层参数 c = {c}")
    
    return inner_func

# 创建闭包实例
closure1 = outer_func("Hello")
closure1()
# 输出:
# 外层变量 a = 666
# 外层参数 c = Hello

print("=" * 50)

# ==================== 闭包的实际应用 ====================
def multiplier(factor):
    """创建乘法器闭包"""
    def multiply(number):
        return number * factor
    return multiply

# 创建不同的乘法器
double = multiplier(2)    # 创建翻倍器
triple = multiplier(3)    # 创建三倍器

print(f"5 * 2 = {double(5)}")  # 输出: 5 * 2 = 10
print(f"5 * 3 = {triple(5)}")  # 输出: 5 * 3 = 15

print("=" * 50)

# ==================== 闭包保存状态 ====================
def counter():
    """计数器闭包 - 展示闭包保存状态的能力"""
    count = 0
    
    def increment():
        nonlocal count  # 修改外层变量需要 nonlocal
        count += 1
        return count
    
    return increment

# 创建两个独立的计数器
counter1 = counter()
counter2 = counter()

print(f"计数器1: {counter1()}")  # 1
print(f"计数器1: {counter1()}")  # 2
print(f"计数器2: {counter2()}")  # 1 (独立的状态)
print(f"计数器1: {counter1()}")  # 3

print("=" * 50)

# ==================== 检查闭包 ====================
def check_closure():
    x = "闭包变量"
    
    def inner():
        return x
    
    return inner

closure_func = check_closure()
print(f"闭包函数名: {closure_func.__name__}")
print(f"闭包变量: {closure_func.__closure__}")  # 显示闭包信息
print(f"调用结果: {closure_func()}")

"""
学习总结：
1. 闭包 = 内层函数 + 外层环境变量
2. 闭包可以保存和访问外层函数的状态
3. 每次调用外层函数都会创建新的闭包实例
4. 闭包常用于装饰器、工厂函数等场景
5. 使用 nonlocal 关键字可以修改外层变量
"""
