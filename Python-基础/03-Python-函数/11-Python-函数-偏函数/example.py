# -*- coding: utf-8 -*-

# @Time    : 2025-5-28
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 11-Python-函数-偏函数

"""
偏函数 (Partial Function) 学习要点：
1. 当函数参数较多，某些参数在大部分场景下都是固定值时使用
2. 可以创建新函数，固定原函数的某些参数
3. 使用functools.partial()可以快速创建偏函数
"""

from functools import partial

# ==================== 基础示例：理解偏函数概念 ====================

def test(a, b, c, d=1):
    """原函数：四个参数的加法运算"""
    result = a + b + c + d
    print(f"计算结果: {a} + {b} + {c} + {d} = {result}")
    return result

print("=== 1. 原函数调用 ===")
test(1, 2, 3, 4)  # 输出: 10

# ==================== 手动创建偏函数 ====================

def test2(a, b, c, d=2):
    """手动创建的偏函数：固定d=2"""
    return test(a, b, c, d)

print("\n=== 2. 手动偏函数 ===")
test2(1, 2, 3)  # 相当于 test(1, 2, 3, 2)，输出: 8

# ==================== 使用functools.partial创建偏函数 ====================

print("\n=== 3. 使用functools.partial创建偏函数 ===")

# 创建偏函数：固定c=5
new_function = partial(test, c=5)
print(f"偏函数对象: {new_function}")
print(f"偏函数类型: {type(new_function)}")

# 调用偏函数
new_function(1, 2)  # 相当于 test(1, 2, c=5, d=1)，输出: 9

# ==================== 更多偏函数示例 ====================

print("\n=== 4. 更复杂的偏函数示例 ===")

def power_func(base, exponent, multiplier=1):
    """幂函数：base^exponent * multiplier"""
    result = (base ** exponent) * multiplier
    print(f"{base}^{exponent} * {multiplier} = {result}")
    return result

# 创建平方函数（固定指数为2）
square = partial(power_func, exponent=2)
print("平方函数:")
square(3)      # 3^2 * 1 = 9
square(4, 2)   # 4^2 * 2 = 32

# 创建立方函数（固定指数为3）
cube = partial(power_func, exponent=3)
print("\n立方函数:")
cube(2)        # 2^3 * 1 = 8
cube(3, 2)     # 3^3 * 2 = 54

# ==================== 实际应用场景 ====================

print("\n=== 5. 实际应用场景：日志函数 ===")

def log_message(level, module, message):
    """日志记录函数"""
    print(f"[{level}] {module}: {message}")

# 为不同模块创建专用的日志函数
db_logger = partial(log_message, module="DATABASE")
api_logger = partial(log_message, module="API")

# 为不同级别创建日志函数
error_log = partial(log_message, level="ERROR")
info_log = partial(log_message, level="INFO")

# 使用专用日志函数
db_logger("ERROR", "连接失败")
api_logger("INFO", "请求成功")
error_log("DATABASE", "查询超时")
info_log("API", "服务启动")

# ==================== 偏函数的优势总结 ====================

print("\n=== 偏函数的优势 ===")
print("1. 简化函数调用，减少重复参数传递")
print("2. 提高代码复用性")
print("3. 创建更具语义化的函数名称")
print("4. 适用于配置固定、业务逻辑相似的场景")

# ==================== 注意事项 ====================

print("\n=== 注意事项 ===")
print("1. partial()第一个参数必须是函数对象，不能是函数调用")
print("2. 可以固定位置参数和关键字参数")
print("3. 偏函数仍然是函数，可以继续传递其他参数")

# 错误示例（注释掉避免报错）
# wrong_partial = partial(test(1, 2, 3, 4))  # 错误：传入了函数调用结果

# 正确示例
correct_partial = partial(test, 1, 2)  # 正确：传入函数对象，固定前两个参数
print("固定前两个参数的偏函数:")
correct_partial(10)  # 相当于 test(1, 2, 10, 1)
