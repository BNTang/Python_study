# -*- coding: utf-8 -*-

# @Time    : 2025-5-30
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 37-Python-函数-递归函数

"""
递归函数核心概念:
1. 递归不是一种函数类型，而是一种函数调用方式
2. 在函数内部调用函数自身
3. 包含两个重要过程：传递(递推)和回归(回溯)
4. 必须有终止条件，否则会无限循环

递归的两个关键要素:
- 传递：将问题分解为规模更小的同类问题
- 回归：从最小问题的解开始，逐层返回结果
"""

def factorial(n):
    """
    计算n的阶乘 (n!)
    
    阶乘定义：
    n! = n × (n-1) × (n-2) × ... × 2 × 1
    
    递归思路：
    n! = n × (n-1)!
    
    Args:
        n (int): 要计算阶乘的正整数
        
    Returns:
        int: n的阶乘结果
    """
    # 递归终止条件（基准情况）
    if n == 1:
        print(f"到达递归终点: {n}! = 1")
        return 1
    
    # 递归调用（传递过程）
    print(f"计算 {n}! = {n} × {n-1}!")
    result = n * factorial(n - 1)
    print(f"回归计算: {n}! = {result}")
    return result


def fibonacci(n):
    """
    计算斐波那契数列第n项
    
    斐波那契数列：1, 1, 2, 3, 5, 8, 13, 21, ...
    递归关系：F(n) = F(n-1) + F(n-2)
    
    Args:
        n (int): 要计算的项数
        
    Returns:
        int: 第n项的值
    """
    # 递归终止条件
    if n <= 2:
        return 1
    
    # 递归调用
    return fibonacci(n - 1) + fibonacci(n - 2)


def countdown(n):
    """
    递归实现倒计时
    演示递归的传递和回归过程
    """
    if n <= 0:
        print("倒计时结束！")
        return
    
    print(f"传递阶段: {n}")
    countdown(n - 1)  # 递归调用
    print(f"回归阶段: {n}")


def power(base, exp):
    """
    递归计算幂运算 base^exp
    
    递归思路：
    base^exp = base × base^(exp-1)
    """
    # 递归终止条件
    if exp == 0:
        return 1
    if exp == 1:
        return base
    
    # 递归调用
    return base * power(base, exp - 1)


# 测试递归函数
if __name__ == "__main__":
    print("=" * 50)
    print("递归函数演示")
    print("=" * 50)
    
    # 1. 阶乘演示
    print("\n【阶乘函数演示】")
    print("-" * 30)
    n = 5
    print(f"计算 {n}! 的过程：")
    result = factorial(n)
    print(f"最终结果：{n}! = {result}")
    
    # 验证结果
    print(f"\n验证：5! = 5×4×3×2×1 = {5*4*3*2*1}")
    
    # 2. 斐波那契数列演示
    print("\n【斐波那契数列演示】")
    print("-" * 30)
    for i in range(1, 11):
        print(f"F({i}) = {fibonacci(i)}")
    
    # 3. 倒计时演示（展示传递和回归）
    print("\n【递归传递和回归演示】")
    print("-" * 30)
    countdown(3)
    
    # 4. 幂运算演示
    print("\n【幂运算演示】")
    print("-" * 30)
    base, exp = 2, 4
    result = power(base, exp)
    print(f"{base}^{exp} = {result}")
    
    print("\n" + "=" * 50)
    print("递归函数要点总结:")
    print("1. 必须有明确的终止条件")
    print("2. 每次递归调用都要向终止条件靠近")
    print("3. 递归过程分为传递(分解问题)和回归(合并结果)")
    print("4. 适用于可以分解为相同子问题的场景")
    print("=" * 50)
