# -*- coding: utf-8 -*-

# @Time    : 2025-5-28
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 14-Python-函数-高阶函数-使用场景

"""
=== 高阶函数学习重点 ===
1. 高阶函数定义：接收函数作为参数的函数
2. 函数可以像变量一样传递
3. 动态计算，灵活性强
"""

# ============= 核心：高阶函数定义 =============
def calculate(number1, number2, function):
    """
    高阶函数：动态计算两个数据
    
    参数:
        number1: 第一个数字
        number2: 第二个数字  
        function: 函数对象（注意：不是函数调用）
    
    返回:
        计算结果
    """
    print(f"📍 高阶函数接收参数: {number1}, {number2}, 函数: {function.__name__}")
    
    # 🔥 关键：调用传入的函数，传递两个数字参数
    result = function(number1, number2)
    print(f"🔥 函数 {function.__name__}({number1}, {number2}) = {result}")
    return result


# ============= 基础函数定义 =============
def sum_func(a, b):
    """加法函数"""
    return a + b

def sub_func(a, b):
    """减法函数"""  
    return a - b

def mul_func(a, b):
    """乘法函数"""
    return a * b

def div_func(a, b):
    """除法函数"""
    if b != 0:
        return a / b
    else:
        return "除数不能为0"


# ============= 高阶函数应用示例 =============
print("=" * 50)
print("🚀 高阶函数使用场景演示")
print("=" * 50)

# 示例1：使用加法函数
print("\n📌 示例1：传递加法函数")
result1 = calculate(6, 2, sum_func)  # 注意：传递的是函数本身，不是sum_func()
print(f"最终结果: {result1}")

print("\n" + "-" * 30)

# 示例2：使用减法函数  
print("\n📌 示例2：传递减法函数")
result2 = calculate(6, 2, sub_func)  # 传递减法函数
print(f"最终结果: {result2}")

print("\n" + "-" * 30)

# 示例3：使用乘法函数
print("\n📌 示例3：传递乘法函数")
result3 = calculate(6, 2, mul_func)
print(f"最终结果: {result3}")

print("\n" + "-" * 30)

# 示例4：使用除法函数
print("\n📌 示例4：传递除法函数")
result4 = calculate(6, 2, div_func)
print(f"最终结果: {result4}")

print("\n" + "=" * 50)

# ============= 进阶：使用lambda表达式 =============
print("\n🔥 进阶用法：使用lambda表达式")
print("=" * 50)

# 使用lambda表达式作为函数参数
power_result = calculate(6, 2, lambda x, y: x ** y)
print(f"📍 幂运算结果: {power_result}")

mod_result = calculate(6, 2, lambda x, y: x % y)
print(f"📍 取模运算结果: {mod_result}")

print("\n" + "=" * 50)
print("✅ 学习要点总结:")
print("1. 函数名不加括号 = 函数对象")
print("2. 函数名加括号 = 函数调用")  
print("3. 高阶函数提供了灵活的计算方式")
print("4. 可以动态改变计算逻辑，无需修改核心函数")
print("=" * 50)
