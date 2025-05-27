# -*- coding: utf-8 -*-

# @Time    : 2025-5-28
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 09-Python-函数-返回值

"""
函数返回值学习重点：
1. return 语句的作用
2. return 后续代码不会执行
3. 只能返回一次
4. 返回多个值的方法
5. 拆包接收返回值
"""

# ========== 1. 基础函数（无返回值）==========
def my_sum_basic():
    """基础函数：固定计算1+2，直接打印结果"""
    print(1 + 2)

print("=== 1. 基础函数调用 ===")
my_sum_basic()  # 输出: 3


# ========== 2. 带参数的函数（无返回值）==========
def my_sum_params(a, b):
    """带参数的函数：计算两个数的和，直接打印"""
    print(a + b)

print("\n=== 2. 带参数函数调用 ===")
my_sum_params(4, 5)  # 输出: 9
my_sum_params(6, 7)  # 输出: 13


# ========== 3. 带返回值的函数 ==========
def my_sum_return(a, b):
    """带返回值的函数：计算和并返回结果"""
    result = a + b
    return result  # 返回计算结果

print("\n=== 3. 带返回值函数调用 ===")
# 接收返回值
res = my_sum_return(6, 7)
print(res)  # 输出: 13

# 直接使用返回值
print(my_sum_return(8, 9))  # 输出: 17


# ========== 4. return的重要特性：后续代码不执行 ==========
def demo_return_stop(a, b):
    """演示return后续代码不会执行"""
    result = a + b
    return result
    print("这行代码永远不会被执行！")  # 这行不会执行
    return 666  # 这行也不会执行

print("\n=== 4. return特性演示 ===")
result = demo_return_stop(3, 4)
print(f"返回值: {result}")  # 只会得到第一个return的值


# ========== 5. 返回多个值 ==========
def calculate_sum_diff(a, b):
    """计算两个数的和与差，返回多个值"""
    sum_result = a + b
    diff_result = a - b
    # 返回元组（多个值）
    return sum_result, diff_result

print("\n=== 5. 返回多个值 ===")
# 方法1：接收整个元组
res = calculate_sum_diff(10, 3)
print(f"返回的元组: {res}")  # (13, 7)
print(f"和: {res[0]}, 差: {res[1]}")

# 方法2：拆包接收
sum_val, diff_val = calculate_sum_diff(10, 3)
print(f"和: {sum_val}, 差: {diff_val}")  # 和: 13, 差: 7


# ========== 6. 不同数据结构返回多个值 ==========
def calculate_multiple_ways(a, b):
    """用不同数据结构返回多个值"""
    sum_result = a + b
    diff_result = a - b
    product = a * b
    
    # 返回列表
    return [sum_result, diff_result, product]

def calculate_as_dict(a, b):
    """返回字典格式的计算结果"""
    return {
        'sum': a + b,
        'diff': a - b,
        'product': a * b
    }

print("\n=== 6. 不同返回格式 ===")
# 列表返回
list_result = calculate_multiple_ways(5, 2)
print(f"列表返回: {list_result}")  # [7, 3, 10]

# 字典返回
dict_result = calculate_as_dict(5, 2)
print(f"字典返回: {dict_result}")  # {'sum': 7, 'diff': 3, 'product': 10}
print(f"从字典取和: {dict_result['sum']}")


# ========== 7. 实际应用示例 ==========
def process_data(data):
    """数据处理函数：返回处理结果供外部不同业务使用"""
    # 假设进行某种数据处理
    processed = sum(data) / len(data)  # 计算平均值
    return processed

print("\n=== 7. 实际应用示例 ===")
numbers = [1, 2, 3, 4, 5]
average = process_data(numbers)

# 外部可以根据需要对结果进行不同处理
print(f"平均值: {average}")
print(f"平均值乘以4: {average * 4}")
print(f"平均值除以5: {average / 5}")

print("\n=== 总结 ===")
print("1. return 用于返回函数处理结果")
print("2. return 后的代码不会执行")
print("3. 可以返回单个值或多个值（元组、列表、字典）")
print("4. 使用拆包可以方便地接收多个返回值")
print("5. 返回值让函数更灵活，便于复用")
