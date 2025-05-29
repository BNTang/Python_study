# -*- coding: utf-8 -*-

# @Time    : 2025-5-29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 25-Python-函数-装饰器-注意事项-1

"""
装饰器的重要概念和注意事项：
1. 装饰器的叠加：从上到下装饰，从下到上执行
2. 对有参数函数的装饰
"""

# ================== 1. 装饰器叠加示例 ==================

# 基础被装饰函数
def print_content():
    """被装饰的基础函数"""
    print("社会我顺哥，人狠话不多")

# 横线装饰器
def line_decorator(func):
    """添加横线装饰器"""
    def inner():
        print("-" * 30)  # 先打印横线
        func()  # 执行原函数
    return inner

# 星星装饰器
def star_decorator(func):
    """添加星星装饰器"""
    def inner():
        print("*" * 30)  # 先打印星星
        func()  # 执行原函数
    return inner

# 单个装饰器示例
@line_decorator
def content_with_line():
    print("社会我顺哥，人狠话不多")

print("=== 单个装饰器效果 ===")
content_with_line()

print("\n=== 星星装饰器效果 ===")
@star_decorator
def content_with_star():
    print("社会我顺哥，人狠话不多")

content_with_star()

# 装饰器叠加示例（重点）
print("\n=== 装饰器叠加效果 ===")
@line_decorator    # 外层装饰器（后执行）
@star_decorator    # 内层装饰器（先执行）
def content_with_both():
    print("社会我顺哥，人狠话不多")

content_with_both()

print("\n装饰器叠加原理解释：")
print("1. 从上到下装饰：line_decorator(star_decorator(content_with_both))")
print("2. 从下到上执行：先执行星星装饰，再执行横线装饰")

# ================== 2. 对有参数函数的装饰 ==================

print("\n" + "="*50)
print("对有参数函数的装饰示例")
print("="*50)

# 普通的有参数函数
def print_number():
    """无参数函数"""
    print("number: 10")

print("\n=== 无参数函数调用 ===")
print_number()

# 有参数的函数
def print_param_number(num):
    """有参数函数"""
    print(f"number: {num}")

print("\n=== 有参数函数调用 ===")
print_param_number(20)

# 用于装饰有参数函数的装饰器
def param_decorator(func):
    """装饰有参数函数的装饰器"""
    def inner(*args, **kwargs):  # 接收任意参数
        print("--- 开始执行函数 ---")
        result = func(*args, **kwargs)  # 传递参数给原函数
        print("--- 函数执行完毕 ---")
        return result
    return inner

# 装饰有参数的函数
@param_decorator
def add_numbers(a, b):
    """加法函数"""
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

print("\n=== 装饰有参数函数 ===")
add_numbers(5, 3)

# 装饰有多种参数的函数
@param_decorator
def greet(name, age=18, **other_info):
    """问候函数，支持多种参数类型"""
    print(f"Hello {name}, age: {age}")
    if other_info:
        print(f"Other info: {other_info}")

print("\n=== 装饰复杂参数函数 ===")
greet("Alice", age=25, city="Beijing", hobby="coding")

# ================== 3. 综合示例：带参数的函数叠加装饰器 ==================

print("\n" + "="*50)
print("综合示例：有参数函数的装饰器叠加")
print("="*50)

def log_decorator(func):
    """日志装饰器"""
    def inner(*args, **kwargs):
        print(f"📝 调用函数: {func.__name__}")
        print(f"📝 参数: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"📝 返回值: {result}")
        return result
    return inner

def timer_decorator(func):
    """计时装饰器"""
    def inner(*args, **kwargs):
        print("⏰ 开始计时...")
        result = func(*args, **kwargs)
        print("⏰ 执行完毕")
        return result
    return inner

@log_decorator     # 外层：后执行
@timer_decorator   # 内层：先执行
def calculate(operation, a, b):
    """计算函数"""
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    else:
        return "未知操作"

print("\n=== 多装饰器叠加执行 ===")
result = calculate("add", 10, 5)
print(f"最终结果: {result}")

print("\n=== 关键知识点总结 ===")
print("1. 装饰器叠加：从上到下装饰，从下到上执行")
print("2. 参数传递：使用 *args, **kwargs 接收和传递任意参数")
print("3. 执行顺序：外层装饰器包装内层装饰器的结果")
print("4. 返回值处理：确保装饰器正确传递返回值")
