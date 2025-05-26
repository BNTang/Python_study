# -*- coding: utf-8 -*-

# @Time    : 2025-5-26
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 03-Python-函数-参数-单一参数

# 1. 无参数函数示例
def calc1():
    """计算2的1次方、2次方、3次方"""
    print("2的1次方:", 2 ** 1)
    print("2的2次方:", 2 ** 2) 
    print("2的3次方:", 2 ** 3)

def calc2():
    """计算3的1次方、2次方、3次方"""
    print("3的1次方:", 3 ** 1)
    print("3的2次方:", 3 ** 2)
    print("3的3次方:", 3 ** 3)

# 2. 单参数函数示例 - 更加灵活的实现
def calc(number):
    """
    计算指定数字的1次方、2次方、3次方
    参数说明:
    - number: 形参(形式参数) - 函数定义时的参数名称
    - 调用时传入的具体值称为实参(实际参数)
    """
    print(f"{number}的1次方:", number ** 1)
    print(f"{number}的2次方:", number ** 2)
    print(f"{number}的3次方:", number ** 3)

# 函数调用和测试
if __name__ == "__main__":
    print("=== 无参数函数示例 ===")
    print("调用calc1():")
    calc1()
    
    print("\n调用calc2():")
    calc2()
    
    print("\n=== 单参数函数示例 ===")
    print("调用calc(3): (这里的3是实参)")
    calc(3)  # 3是实参(实际参数)
    
    print("\n调用calc(2): (这里的2是实参)")
    calc(2)  # 2是实参(实际参数)
    
    print("\n调用calc(5): (这里的5是实参)")
    calc(5)  # 5是实参(实际参数)
    
    print("\n=== 参数概念说明 ===")
    print("形参(形式参数): 函数定义时的参数名称，如 def calc(number) 中的 number")
    print("实参(实际参数): 函数调用时传入的具体值，如 calc(3) 中的 3")
    print("当函数需要动态调整处理的数据时，就可以使用参数来接收相关数据")
