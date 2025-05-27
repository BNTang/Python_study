# -*- coding: utf-8 -*-

# @Time    : 2025-5-26
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 06-Python-函数-参数-参数的拆包和装包

"""
参数的装包和拆包：
1. 装包：把传递的参数包装成一个集合（元组或字典）
2. 拆包：把集合参数分解成单独的个体
"""

# 1. 使用 *args 进行装包（接收多个位置参数）
def test(*constants):
    """演示参数装包：多个参数被装包成元组"""
    print("装包结果:", constants)
    print("类型:", type(constants))

# 调用函数，传入多个参数
print("=== 参数装包示例 ===")
test(1, 2, 3, 4)

print("\n=== 参数拆包示例 ===")
# 拆包操作：使用 * 将元组拆解成独立元素
args_tuple = (1, 2, 3, 4)
print("拆包:", *args_tuple)

# 2. 实际应用场景：求和函数
def my_sum(a, b, c, d):
    """计算四个数的和"""
    result = a + b + c + d
    print(f"计算结果: {a} + {b} + {c} + {d} = {result}")
    return result

print("\n=== 拆包在函数调用中的应用 ===")
# 方法1：直接传入元组会报错
# my_sum(args_tuple)  # 这样会报错，因为只传了一个参数

# 方法2：手动取出每个元素（繁琐）
print("方法1 - 手动取出:")
my_sum(args_tuple[0], args_tuple[1], args_tuple[2], args_tuple[3])

# 方法3：使用拆包操作（推荐）
print("方法2 - 使用拆包:")
my_sum(*args_tuple)

# 3. 使用 **kwargs 进行装包（接收多个关键字参数）
def test2(**kwargs):
    """演示关键字参数装包：多个关键字参数被装包成字典"""
    print("关键字参数装包结果:", kwargs)
    print("类型:", type(kwargs))

print("\n=== 关键字参数装包示例 ===")
test2(a=1, b=2, c=3)

# 4. 关键字参数拆包示例
def my_sum2(a, b):
    """计算两个数的和"""
    print(f"a = {a}")
    print(f"b = {b}")
    return a + b

print("\n=== 关键字参数拆包示例 ===")
kwargs_dict = {'a': 1, 'b': 2}

# 错误方式：直接传字典
# my_sum2(kwargs_dict)  # 这样会报错

# 正确方式：使用 ** 拆包
print("使用 ** 拆包:")
my_sum2(**kwargs_dict)

# 等价于：my_sum2(a=1, b=2)
print("等价调用:")
my_sum2(a=1, b=2)

# 5. 注意事项：参数名必须匹配
def func_with_specific_params(a, c):  # 注意这里是 a, c
    print(f"a = {a}, c = {c}")

print("\n=== 参数名匹配注意事项 ===")
# 这会报错，因为字典中有 'b' 键，但函数参数中没有
# func_with_specific_params(**kwargs_dict)

# 正确的做法：
correct_kwargs = {'a': 1, 'c': 3}
func_with_specific_params(**correct_kwargs)

# 6. 综合示例：同时使用 *args 和 **kwargs
def flexible_function(*args, **kwargs):
    """可以接收任意数量的位置参数和关键字参数"""
    print("位置参数 (args):", args)
    print("关键字参数 (kwargs):", kwargs)

print("\n=== 综合示例 ===")
flexible_function(1, 2, 3, name="Python", version=3.9)

# 7. 拆包传递给灵活函数
print("\n=== 拆包传递给灵活函数 ===")
args_data = (1, 2, 3)
kwargs_data = {'name': 'Python', 'version': 3.9}

flexible_function(*args_data, **kwargs_data)

print("\n=== 总结 ===")
print("装包：* 用于位置参数，** 用于关键字参数")
print("拆包：* 拆解序列，** 拆解字典")
print("注意：拆包时参数名必须与函数定义匹配")
