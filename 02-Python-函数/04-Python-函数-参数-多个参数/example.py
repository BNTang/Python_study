# -*- coding: utf-8 -*-

# @Time    : 2025-5-26
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 04-Python-函数-参数-多个参数

# 多个参数情况
# 当一个场景需要动态的调整函数体当中多个的处理信息时
# 就可以接收多个参数

# 1. 最初版本 - 硬编码版本（不灵活）
def my_sum():
    """计算1+2的和"""
    return 1 + 2

# 调用硬编码版本
print("硬编码版本结果:", my_sum())  # 结果: 3

# 2. 单个参数版本 - 动态改变一个值
def my_sum_one_param(number1):
    """计算number1+2的和"""
    return number1 + 2

# 调用单个参数版本
print("单个参数版本(3+2):", my_sum_one_param(3))  # 结果: 5
print("单个参数版本(4+2):", my_sum_one_param(4))  # 结果: 6

# 3. 多个参数版本 - 动态改变两个值
def my_sum_two_params(number1, number2):
    """计算两个数的和"""
    print(f"number1: {number1}")
    print(f"number2: {number2}")
    return number1 + number2

# 调用方式1: 位置参数（按顺序一一对应）
print("位置参数调用(4+5):", my_sum_two_params(4, 5))  # 结果: 9

# 调用方式2: 关键字参数（不必严格按照顺序）
print("关键字参数调用:")
result = my_sum_two_params(number2=5, number1=6)  # 注意顺序不同
print("关键字参数结果:", result)  # 结果: 11

# 4. 混合使用位置参数和关键字参数
def calculate(a, b, c):
    """计算三个数的和"""
    return a + b + c

# 混合调用示例
print("混合参数调用:", calculate(1, c=3, b=2))  # 结果: 6

# 5. 更多参数的例子
def multiply_numbers(num1, num2, num3=1):
    """计算多个数的乘积，num3有默认值"""
    return num1 * num2 * num3

print("乘法运算(2*3):", multiply_numbers(2, 3))  # 结果: 6
print("乘法运算(2*3*4):", multiply_numbers(2, 3, 4))  # 结果: 24
print("乘法运算(关键字):", multiply_numbers(num2=5, num1=2, num3=3))  # 结果: 30

# 总结:
# 1. 多个参数应该以逗号作为分割
# 2. 调用时有两种方式:
#    - 位置参数: 按照顺序一一对应
#    - 关键字参数: 直接指定形参名称，不必严格按照顺序
# 3. 关键字参数类似字典的key-value对应关系
