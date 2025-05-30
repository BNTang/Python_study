# -*- coding: utf-8 -*-

# @Time    : 2025-5-29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 26-Python-函数-装饰器-注意事项-装饰器的执行图解

"""
装饰器的执行流程图解
重点：理解装饰器如何替换原函数，以及执行顺序
"""

print("=" * 60)
print("装饰器执行流程详解")
print("=" * 60)

# ===== 第一部分：基础函数定义 =====
print("\n1. 基础函数定义（未装饰前）")
print("-" * 30)

def p_number():
    """原始函数：简单打印数字"""
    print("10")

print("原始函数调用:")
p_number()  # 输出: 10

# ===== 第二部分：装饰器定义 =====
print("\n2. 装饰器定义")
print("-" * 30)

def 装饰器(func):
    """
    装饰器函数
    参数: func - 被装饰的函数
    返回: inner - 内部包装函数
    """
    print(f"装饰器被调用，接收函数: {func.__name__}")
    
    def inner():
        """内部包装函数：添加额外功能"""
        print("-" * 30)  # 装饰：添加分隔线
        func()            # 调用原函数
        print("-" * 30)  # 装饰：添加分隔线
    
    print(f"返回内部函数: {inner.__name__}")
    return inner

# ===== 第三部分：装饰器应用过程图解 =====
print("\n3. 装饰器应用过程图解")
print("-" * 30)

print("步骤1: 定义新的被装饰函数")
@装饰器
def p_number_decorated():
    """被装饰的函数"""
    print("10")

print("\n步骤2: 执行被装饰后的函数")
p_number_decorated()

# ===== 第四部分：手动装饰过程详解 =====
print("\n4. 手动装饰过程详解（等价于@装饰器）")
print("-" * 30)

# 重新定义原函数
def p_number_manual():
    print("10")

print("原函数地址:", id(p_number_manual))
print("原函数名称:", p_number_manual.__name__)

# 手动应用装饰器（等价于 @装饰器）
print("\n执行: p_number_manual = 装饰器(p_number_manual)")
p_number_manual = 装饰器(p_number_manual)

print("装饰后函数地址:", id(p_number_manual))
print("装饰后函数名称:", p_number_manual.__name__)

print("\n调用装饰后的函数:")
p_number_manual()

# ===== 第五部分：带参数的函数装饰 =====
print("\n5. 带参数函数的装饰")
print("-" * 30)

def 通用装饰器(func):
    """支持任意参数的装饰器"""
    def inner(*args, **kwargs):
        print("🎯 函数调用开始")
        print(f"📝 调用函数: {func.__name__}")
        print(f"📋 参数: args={args}, kwargs={kwargs}")
        
        result = func(*args, **kwargs)
        
        print("✅ 函数调用结束")
        return result
    
    return inner

@通用装饰器
def greet(name, age=None):
    """带参数的函数"""
    if age:
        print(f"Hello, {name}! You are {age} years old.")
    else:
        print(f"Hello, {name}!")

print("调用带参数的装饰函数:")
greet("Alice")
greet("Bob", age=25)

# ===== 第六部分：执行流程总结 =====
print("\n6. 装饰器执行流程总结")
print("-" * 30)

print("""
🔄 装饰器执行流程:

1️⃣ 定义阶段：
   - 定义装饰器函数
   - 定义被装饰函数
   
2️⃣ 装饰阶段（@装饰器 或 func = 装饰器(func)）：
   - 调用装饰器，传入原函数
   - 装饰器内部定义包装函数
   - 返回包装函数，替换原函数引用
   
3️⃣ 调用阶段：
   - 调用被装饰函数时，实际调用的是包装函数
   - 包装函数内部调用原函数，并添加额外功能

💡 关键理解点：
   - 装饰器改变了函数的引用，但不改变调用方式
   - 被装饰函数 = 包装函数（内部调用原函数）
   - 闭包机制保持对原函数的引用
""")

# ===== 第七部分：多重装饰器示例 =====
print("\n7. 多重装饰器执行顺序")
print("-" * 30)

def 装饰器A(func):
    def wrapper():
        print("装饰器A - 开始")
        func()
        print("装饰器A - 结束")
    return wrapper

def 装饰器B(func):
    def wrapper():
        print("装饰器B - 开始")
        func()
        print("装饰器B - 结束")
    return wrapper

@装饰器A
@装饰器B
def test_func():
    print("原始函数执行")

print("多重装饰器调用结果:")
test_func()

print("\n执行顺序说明：")
print("@装饰器A")
print("@装饰器B")
print("等价于: test_func = 装饰器A(装饰器B(test_func))")
print("调用顺序: A外 -> B外 -> 原函数 -> B内 -> A内")

print("\n" + "=" * 60)
print("学习重点总结")
print("=" * 60)
print("1. 装饰器本质是函数替换")
print("2. @语法糖等价于手动赋值")
print("3. 闭包保持对原函数的引用")
print("4. 多重装饰器从内到外应用")
print("5. 装饰器在定义时立即执行")
