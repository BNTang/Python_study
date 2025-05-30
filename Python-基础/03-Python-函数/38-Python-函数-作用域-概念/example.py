# -*- coding: utf-8 -*-

# @Time    : 2025-5-30
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 38-Python-函数-作用域-概念

"""
Python作用域概念学习
=====================

主要内容：
1. 变量作用域的基本概念
2. LEGB规则详解
3. 命名空间的概念
4. 不同作用域的访问规则
5. Python没有块级作用域的特点
"""

print("=" * 50)
print("1. 变量作用域基本概念演示")
print("=" * 50)

# 全局变量 - 在文件最外层定义，全局可访问
b = 10

def test_scope():
    """演示函数内外变量访问规则"""
    # 局部变量 - 只能在函数内部访问
    a = 1
    print(f"函数内部访问局部变量 a: {a}")
    print(f"函数内部访问全局变量 b: {b}")

# 调用函数
test_scope()

# 尝试在函数外访问局部变量（会报错）
try:
    print(a)  # 这里会报错：NameError: name 'a' is not defined
except NameError as e:
    print(f"错误演示 - 在函数外访问局部变量: {e}")

print(f"在函数外访问全局变量 b: {b}")

print("\n" + "=" * 50)
print("2. LEGB规则详解")
print("=" * 50)

"""
LEGB规则：
L - Local（局部作用域）：函数内的作用域
E - Enclosing（嵌套作用域）：外部嵌套函数的作用域
G - Global（全局作用域）：当前模块（文件）的作用域
B - Built-in（内建作用域）：Python内建模块的作用域
"""

# Built-in（内建作用域）示例
print(f"内建函数示例 - len: {len}")
print(f"内建变量示例 - __name__: {__name__}")

# Global（全局作用域）变量
global_var = "我是全局变量"

def outer_function():
    """外部函数 - 演示Enclosing作用域"""
    # Enclosing（嵌套作用域）变量
    enclosing_var = "我是嵌套作用域变量"
    
    def inner_function():
        """内部函数 - 演示Local作用域和LEGB查找顺序"""
        # Local（局部作用域）变量
        local_var = "我是局部变量"
        
        print(f"L - 局部变量: {local_var}")
        print(f"E - 嵌套作用域变量: {enclosing_var}")
        print(f"G - 全局变量: {global_var}")
        print(f"B - 内建变量: {__name__}")
        
        # 演示LEGB查找顺序
        test_var = "局部优先"
        print(f"变量查找顺序演示: {test_var}")
    
    # 在嵌套作用域中也定义同名变量
    test_var = "嵌套作用域"
    
    print("外部函数中：")
    print(f"E - 嵌套作用域变量: {enclosing_var}")
    print(f"G - 全局变量: {global_var}")
    
    # 调用内部函数
    inner_function()

# 在全局作用域中也定义同名变量
test_var = "全局作用域"

print("调用嵌套函数演示：")
outer_function()

print("\n" + "=" * 50)
print("3. 命名空间概念演示")
print("=" * 50)

"""
命名空间是作用域的具体体现形式
就像不同班级的学生，即使同名也不会冲突
"""

# 模拟不同命名空间
class ClassA:
    """模拟A班级命名空间"""
    student_name = "张三"
    
class ClassB:
    """模拟B班级命名空间"""
    student_name = "张三"

print(f"A班的张三: {ClassA.student_name}")
print(f"B班的张三: {ClassB.student_name}")
print("通过命名空间区分同名变量，避免冲突")

# 模块命名空间示例
import os
import sys

print(f"os模块的remove函数: {os.remove}")
print("不同模块的同名函数通过模块名进行区分")

print("\n" + "=" * 50)
print("4. 变量查找顺序演示")
print("=" * 50)

def demonstrate_lookup_order():
    """演示变量查找的LEGB顺序"""
    
    def outer():
        x = "Enclosing"
        
        def inner():
            # x = "Local"  # 如果注释掉这行，会查找外层的x
            print(f"查找到的x: {x}")  # 会按LEGB顺序查找
        
        inner()
    
    outer()

# 全局变量x
x = "Global"

print("演示变量查找顺序：")
demonstrate_lookup_order()

print("\n" + "=" * 50)
print("5. Python没有块级作用域")
print("=" * 50)

"""
重要特点：Python没有块级作用域
if、while、for等代码块不会创建新的作用域
"""

# 演示if块中的变量在外部仍可访问
if True:
    block_var = "在if块中定义的变量"

print(f"if块外访问块内变量: {block_var}")  # 在其他语言中可能报错，但Python可以访问

# 演示for循环中的变量
for i in range(3):
    loop_var = f"循环变量_{i}"

print(f"for循环外访问循环内变量: {loop_var}")  # Python中可以访问

print("\n" + "=" * 50)
print("6. 作用域修改演示")
print("=" * 50)

# global关键字使用
counter = 0

def increment_global():
    """使用global关键字修改全局变量"""
    global counter
    counter += 1
    print(f"全局计数器: {counter}")

def increment_local():
    """不使用global，创建局部变量"""
    counter = 100  # 这是局部变量，不会影响全局counter
    print(f"局部计数器: {counter}")

print("演示global关键字：")
print(f"初始全局counter: {counter}")
increment_global()
increment_local()
print(f"最终全局counter: {counter}")

# nonlocal关键字使用
def outer_with_nonlocal():
    """演示nonlocal关键字"""
    x = 10
    
    def inner():
        nonlocal x
        x += 1
        print(f"使用nonlocal修改外层变量: {x}")
    
    print(f"修改前: {x}")
    inner()
    print(f"修改后: {x}")

print("\n演示nonlocal关键字：")
outer_with_nonlocal()

print("\n" + "=" * 50)
print("学习总结")
print("=" * 50)
print("""
重点掌握：
1. LEGB规则：Local -> Enclosing -> Global -> Built-in
2. 变量查找顺序：从内向外逐层查找
3. Python没有块级作用域（if/for/while块不创建新作用域）
4. global关键字：在函数内修改全局变量
5. nonlocal关键字：在嵌套函数内修改外层函数变量
6. 命名空间用于区分不同作用域的同名变量
""")
