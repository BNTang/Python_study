# -*- coding: utf-8 -*-

# @Time    : 2025-5-28
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 15-Python-函数-返回函数

"""
【重点概念】返回函数 (Returning Functions)
- 高级函数：函数可以作为参数传递，也可以作为返回值
- 返回函数：函数内部返回另一个函数的操作
- 应用场景：根据不同参数获取不同的操作函数
"""

def get_function(flag):
    """
    根据不同的标识符返回不同的计算函数
    
    【重点】：
    1. 函数内部可以定义其他函数
    2. 返回的是函数对象本身，不是函数调用结果
    3. 外界无法直接访问内部定义的函数（作用域限制）
    """
    
    # 在函数内部定义多个计算函数
    def sum_func(a, b, c):
        """加法函数"""
        return a + b + c
    
    def subtract_func(a, b, c):
        """减法函数"""
        return a - b - c
    
    def multiply_func(a, b, c):
        """乘法函数"""
        return a * b * c
    
    def divide_func(a, b, c):
        """除法函数"""
        if b != 0 and c != 0:
            return a / b / c
        else:
            return "除数不能为0"
    
    # 根据flag参数返回对应的函数对象
    if flag == "+":
        return sum_func          # 【重点】返回函数对象，不是sum_func()
    elif flag == "-":
        return subtract_func     # 【重点】返回函数对象，不是subtract_func()
    elif flag == "*":
        return multiply_func
    elif flag == "/":
        return divide_func
    else:
        return None

# ================================= 测试演示 =================================

print("=" * 50)
print("【演示1】获取加法函数")
print("=" * 50)

# 获取加法函数
result = get_function("+")
print(f"返回的结果: {result}")
print(f"结果类型: {type(result)}")
print(f"函数名称: {result.__name__}")

# 调用返回的函数
calculation_result = result(1, 3, 5)
print(f"调用 result(1, 3, 5) 的结果: {calculation_result}")

print("\n" + "=" * 50)
print("【演示2】获取减法函数")
print("=" * 50)

# 获取减法函数
result = get_function("-")
print(f"返回的结果: {result}")
print(f"结果类型: {type(result)}")
print(f"函数名称: {result.__name__}")

# 调用返回的函数
calculation_result = result(1, 3, 5)
print(f"调用 result(1, 3, 5) 的结果: {calculation_result}")

print("\n" + "=" * 50)
print("【演示3】一步到位的调用方式")
print("=" * 50)

# 直接调用返回的函数（链式调用）
print("乘法运算 2 * 3 * 4 =", get_function("*")(2, 3, 4))
print("除法运算 24 / 2 / 3 =", get_function("/")(24, 2, 3))

print("\n" + "=" * 50)
print("【演示4】动态选择计算方式")
print("=" * 50)

# 实际应用：根据用户输入动态选择计算方式
operations = ["+", "-", "*", "/"]
values = (10, 2, 1)

for op in operations:
    func = get_function(op)
    if func:
        result = func(*values)
        print(f"运算 {values[0]} {op} {values[1]} {op} {values[2]} = {result}")

print("\n" + "=" * 50)
print("【总结】返回函数的关键点")
print("=" * 50)
print("1. 函数内部可以定义其他函数")
print("2. 可以返回函数对象（不加括号）")
print("3. 返回的函数可以被调用")
print("4. 实现了代码的模块化和动态选择")
