# -*- coding: utf-8 -*-

# @Time    : 2025-5-30
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 28-Python-函数-装饰器-注意事项-3

"""
装饰器注意事项3：如何处理有返回值的函数

重点知识：
1. 装饰器内部函数必须与被装饰函数格式保持一致
2. 使用可变参数(*args, **kwargs)保证通用性
3. 必须返回被装饰函数的执行结果
4. 通用装饰器可以同时处理有返回值和无返回值的函数
"""

def my_decorator(function):
    """通用装饰器 - 可以处理有返回值和无返回值的函数"""
    def wrapper(*args, **kwargs):
        print("=" * 30)
        print("装饰器：函数执行前的处理")
        
        # 关键点：保存被装饰函数的执行结果
        result = function(*args, **kwargs)
        
        print("装饰器：函数执行后的处理")
        print("=" * 30)
        
        # 关键点：必须返回被装饰函数的结果
        return result
    
    return wrapper

# 测试函数1：有返回值的函数
@my_decorator
def add_numbers(number1, number2, number3):
    """有返回值的函数"""
    print(f"计算：{number1} + {number2} + {number3}")
    return number1 + number2 + number3

# 测试函数2：无返回值的函数
@my_decorator
def print_hello():
    """无返回值的函数"""
    print("Hello, World!")

if __name__ == "__main__":
    print("【演示1：不使用装饰器时的效果】")
    
    # 临时移除装饰器进行对比
    def temp_add_numbers(number1, number2, number3):
        print(f"计算：{number1} + {number2} + {number3}")
        return number1 + number2 + number3
    
    def temp_print_hello():
        print("Hello, World!")
    
    result1 = temp_add_numbers(10, 20, 30)
    result2 = temp_print_hello()
    
    print(f"result1: {result1}")  # 60
    print(f"result2: {result2}")  # None
    
    print("\n【演示2：使用装饰器后的效果】")
    
    # 使用装饰器
    result1 = add_numbers(10, 20, 30)
    result2 = print_hello()
    
    print(f"result1: {result1}")  # 60（保持原有返回值）
    print(f"result2: {result2}")  # None（保持原有返回值）
    
    print("\n【重点总结】")
    print("1. 装饰器内部必须返回被装饰函数的执行结果")
    print("2. 使用可变参数确保装饰器的通用性")
    print("3. 有返回值的函数装饰后仍有返回值")
    print("4. 无返回值的函数装饰后仍返回None")
