# -*- coding: utf-8 -*-

# @Time    : 2025-5-26
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 02-Python-函数-简单定义

"""
看到函数概念之后，再来看一下关于函数的基本使用
此处我们先讲一个最简单的定义方式：
- 没有参数
- 没有返回值的形式

函数的基本定义格式：
def 函数名():
    函数体（代码片段）

函数的调用：
函数名()
"""

print("=" * 50)
print("Python函数的简单定义和调用")
print("=" * 50)

# 函数定义语法说明
print("1. 函数定义语法：")
print("   def 函数名():")
print("       函数体")
print("   ")
print("2. 函数调用语法：")
print("   函数名()")
print()

print("=" * 50)
print("实际演示：定义一个简单函数")
print("=" * 50)

# 定义一个最简单的函数
# def 是关键字
# test 是函数名称（可以参照变量名的命名方式）
# () 小括号表示这是一个函数
# : 冒号代表函数体的开始
def test():
    """这是一个简单的测试函数，没有参数，没有返回值"""
    print("2的1次方:", 2**1)
    print("2的2次方:", 2**2) 
    print("2的3次方:", 2**3)

print("函数已定义，但还没有执行...")
print("注意：函数定义后不会自动执行，需要调用才会执行")
print()

print("=" * 30)
print("开始调用函数：")
print("=" * 30)

# 调用函数：直接写函数名称 + 小括号
test()

print()
print("=" * 50)
print("多次调用同一个函数")
print("=" * 50)

print("第一次调用：")
test()

print("\n第二次调用：")
test()

print("\n第三次调用：")
test()

print()
print("=" * 50)
print("定义更多示例函数")
print("=" * 50)

# 定义打印个人信息的函数
def print_info():
    """打印个人信息"""
    print("姓名: 程序员NEO")
    print("职业: Python开发者")
    print("爱好: 编程、学习")

# 定义打印分隔线的函数  
def print_line():
    """打印分隔线"""
    print("-" * 40)

# 定义问候函数
def greet():
    """简单的问候函数"""
    print("Hello, 欢迎学习Python函数!")
    print("今天是学习函数定义的第一天")

print("调用个人信息函数：")
print_info()

print("\n调用分隔线函数：")
print_line()

print("\n调用问候函数：")
greet()

print()
print("=" * 50)
print("函数的重要概念总结")
print("=" * 50)

def summary():
    """总结函数的重要概念"""
    print("1. 函数定义使用 def 关键字")
    print("2. 函数名后面必须有小括号 ()")
    print("3. 冒号 : 表示函数体开始")
    print("4. 函数体需要缩进")
    print("5. 函数定义后不会自动执行")
    print("6. 需要调用函数才会执行：函数名()")
    print("7. 同一个函数可以被多次调用")

print("函数概念总结：")
summary()

print()
print("=" * 50)
print("函数执行流程演示")
print("=" * 50)

def step_demo():
    """演示函数执行流程"""
    print("→ 进入函数")
    print("→ 执行函数体代码")
    print("→ 函数执行完毕")

print("调用前：准备执行函数")
step_demo()
print("调用后：函数执行完成")

print()
print("=" * 50)
print("学习小结")
print("=" * 50)
print("✓ 学会了函数的基本定义语法")
print("✓ 理解了函数定义与调用的区别") 
print("✓ 掌握了最简单的无参数无返回值函数")
print("✓ 体验了函数的重复使用特性")
print("=" * 50)
