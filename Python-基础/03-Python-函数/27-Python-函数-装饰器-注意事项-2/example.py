# -*- coding: utf-8 -*-

# @Time    : 2025-5-30
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 27-Python-函数-装饰器-注意事项-2

print("=" * 50)
print("装饰器处理有参数函数的注意事项")
print("=" * 50)

# 基础装饰器（有问题的版本）
def zsq_basic(func):
    """基础装饰器 - 只能装饰无参数函数"""
    def inner():
        print("-" * 30)
        func()
    return inner

# 无参数函数测试
@zsq_basic
def p_no_param():
    """无参数函数"""
    print("我是无参数函数")

print("\n1. 装饰无参数函数：")
p_no_param()

# 有参数函数（使用基础装饰器会报错）
def p_with_param(number):
    """有参数函数"""
    print(f"参数值：{number}")

print("\n2. 直接调用有参数函数：")
p_with_param(123)

# 改进版装饰器 - 固定参数版本
def zsq_fixed(func):
    """固定参数装饰器 - 只能处理固定数量参数"""
    def inner(a):
        print("-" * 30)
        func(a)
    return inner

@zsq_fixed
def p_one_param(number):
    """单参数函数"""
    print(f"单参数值：{number}")

print("\n3. 装饰单参数函数：")
p_one_param(123)

# 改进版装饰器 - 多参数固定版本
def zsq_multi_fixed(func):
    """多参数固定装饰器"""
    def inner(a, b):
        print("-" * 30)
        func(a, b)
    return inner

@zsq_multi_fixed
def p_two_params(number, number2):
    """双参数函数"""
    print(f"参数1：{number}")
    print(f"参数2：{number2}")

print("\n4. 装饰双参数函数：")
p_two_params(123, 222)

# 单参数函数（无法使用多参数装饰器）
def p_single(number):
    """单参数函数 - 无法使用多参数装饰器"""
    print(f"单参数：{number}")

# 通用装饰器 - 使用不定长参数（最终解决方案）
def zsq(func):
    """通用装饰器 - 可以装饰任意参数的函数"""
    def inner(*args, **kwargs):
        print("-" * 30)
        print(f"接收到的位置参数：{args}")
        print(f"接收到的关键字参数：{kwargs}")
        # 使用拆包将参数传递给原函数
        return func(*args, **kwargs)
    return inner

print("\n" + "=" * 50)
print("通用装饰器测试")
print("=" * 50)

@zsq
def p_number(number):
    """单参数函数"""
    print(f"number = {number}")

@zsq
def p_number2(number):
    """另一个单参数函数"""
    print(f"number = {number}")

@zsq
def p_multiple(number, number2, number3):
    """多参数函数"""
    print(f"number = {number}")
    print(f"number2 = {number2}")
    print(f"number3 = {number3}")

print("\n5. 通用装饰器 - 单参数测试：")
p_number(123)

print("\n6. 通用装饰器 - 另一个单参数测试：")
p_number2(999)

print("\n7. 通用装饰器 - 多参数测试（位置参数）：")
p_multiple(123, 222, 333)

print("\n8. 通用装饰器 - 多参数测试（关键字参数）：")
p_multiple(123, 222, number3=666)

print("\n" + "=" * 50)
print("重点总结：")
print("1. 装饰器的内部函数需要接收与被装饰函数相同的参数")
print("2. 使用 *args, **kwargs 可以创建通用装饰器")
print("3. 调用原函数时需要使用拆包：func(*args, **kwargs)")
print("4. *args 收集位置参数，**kwargs 收集关键字参数")
print("=" * 50)
