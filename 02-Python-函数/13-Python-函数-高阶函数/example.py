# -*- coding: utf-8 -*-

# @Time    : 2025-5-28
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 13-Python-函数-高阶函数

"""
高阶函数学习要点：
1. 函数名本身就是一个变量，可以赋值给其他变量
2. 函数可以作为参数传递给另一个函数
3. 当一个函数的参数接收另一个函数时，这个函数就是高阶函数
"""

# ================ 1. 函数基础概念演示 ================
def test(a, b):
    """基础函数示例"""
    return a + b

# 演示函数名作为变量
print("函数本身:", test)
print("函数的ID:", id(test))

# 函数可以赋值给另一个变量
test2 = test
print("test2调用结果:", test2(1, 2))  # 输出: 3

print("=" * 50)

# ================ 2. 高阶函数概念 ================
"""
高阶函数定义：当一个函数A的参数接收的是另外一个函数时，
那么就把这个函数A称之为高阶函数
"""

# ================ 3. sorted()函数作为高阶函数示例 ================
# 复杂数据结构
l = [
    {"name": "SZ1", "age": 18},
    {"name": "SZ2", "age": 19}, 
    {"name": "SZ3", "age": 18.5}
]

print("原始列表:")
for item in l:
    print(item)

# 定义关键字函数 - 按age排序
def get_age_key(x):
    """提取age作为排序关键字"""
    return x["age"]

# 使用高阶函数sorted()，传入函数作为参数
result_age = sorted(l, key=get_age_key)
print("\n按age排序后:")
for item in result_age:
    print(item)

# 定义关键字函数 - 按name排序  
def get_name_key(x):
    """提取name作为排序关键字"""
    return x["name"]

result_name = sorted(l, key=get_name_key)
print("\n按name排序后:")
for item in result_name:
    print(item)

print("=" * 50)

# ================ 4. 更多高阶函数示例 ================
# 自定义高阶函数
def apply_operation(num_list, operation_func):
    """
    高阶函数示例：对列表中每个元素应用指定操作
    参数：
    - num_list: 数字列表
    - operation_func: 操作函数
    """
    return [operation_func(x) for x in num_list]

# 定义操作函数
def square(x):
    """平方函数"""
    return x ** 2

def double(x):
    """双倍函数"""
    return x * 2

# 测试数据
numbers = [1, 2, 3, 4, 5]

# 使用高阶函数
squared_result = apply_operation(numbers, square)
doubled_result = apply_operation(numbers, double)

print("原始数字:", numbers)
print("平方结果:", squared_result)
print("双倍结果:", doubled_result)

print("=" * 50)

# ================ 5. 使用lambda表达式简化 ================
print("使用lambda表达式简化:")

# 直接使用lambda作为参数
result_age_lambda = sorted(l, key=lambda x: x["age"])
result_name_lambda = sorted(l, key=lambda x: x["name"])

print("lambda按age排序:", result_age_lambda)
print("lambda按name排序:", result_name_lambda)

# ================ 学习总结 ================
"""
高阶函数重点总结：
1. 【核心概念】函数可以作为参数传递
2. 【实用价值】提高代码复用性和灵活性
3. 【常见应用】sorted(), map(), filter(), reduce()等内置函数
4. 【简化方式】可以使用lambda表达式替代简单函数
5. 【理解要点】函数名就是变量，变量可以传递和赋值
"""
