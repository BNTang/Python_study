# -*- coding: utf-8 -*-

# @Time    : 2025-5-30
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 29-Python-函数-装饰器-注意事项-4

"""
装饰器进阶：带参数的装饰器

重点理解：
1. 普通装饰器的局限性
2. 带参数装饰器的实现原理
3. @符号后面的内容必须是一个装饰器函数

核心原理：@decorator_name 等价于 func = decorator_name(func)
"""

# ============== 第一部分：基础示例 - 要装饰的函数 ==============
def f1():
    """要被装饰的目标函数"""
    print("666")


# ============== 第二部分：普通装饰器示例 ==============
def zsq(func):
    """普通装饰器 - 在函数执行前打印横线"""
    def inner():
        print("-" * 30)  # 打印30个横线
        func()  # 执行原函数
    return inner


def zsq1(func):
    """另一个装饰器 - 在函数执行前打印等号"""
    def inner():
        print("=" * 30)  # 打印30个等号
        func()  # 执行原函数
    return inner


def zsqs(func):
    """第三个装饰器 - 在函数执行前打印星号"""
    def inner():
        print("*" * 30)  # 打印30个星号
        func()  # 执行原函数
    return inner


# ============== 第三部分：问题演示 ==============
print("=" * 50)
print("问题演示：多个相似装饰器造成代码重复")
print("=" * 50)

# 使用不同装饰器装饰函数（演示代码重复问题）
@zsq
def demo1():
    print("666")

@zsq1  
def demo2():
    print("666")

@zsqs
def demo3():
    print("666")

print("使用横线装饰器：")
demo1()

print("\n使用等号装饰器：")
demo2()

print("\n使用星号装饰器：")
demo3()


# ============== 第四部分：解决方案 - 带参数的装饰器 ==============
print("\n" + "=" * 50)
print("解决方案：带参数的装饰器")
print("=" * 50)

def get_decorator(char):
    """
    带参数的装饰器工厂函数
    
    参数说明：
    char: 要打印的字符（如：'-', '=', '*'等）
    
    返回值：
    返回一个装饰器函数
    
    关键理解：
    - 这是一个"装饰器工厂"，用来生成装饰器
    - 外层函数接收参数，内层函数是真正的装饰器
    - 最内层函数是被装饰后的函数
    """
    def decorator(func):  # 这才是真正的装饰器
        def inner():     # 这是装饰后的函数
            print(char * 30)  # 使用传入的字符
            func()           # 执行原函数
        return inner
    return decorator  # 返回装饰器


# ============== 第五部分：使用带参数的装饰器 ==============

# 重要理解：@get_decorator("-") 等价于：
# 1. decorator = get_decorator("-")  # 先调用工厂函数获取装饰器
# 2. f2 = decorator(f2)             # 再用装饰器装饰函数

@get_decorator("-")  # 生成打印横线的装饰器
def f2():
    print("666")

@get_decorator("=")  # 生成打印等号的装饰器  
def f3():
    print("666")

@get_decorator("*")  # 生成打印星号的装饰器
def f4():
    print("666")

@get_decorator("#")  # 生成打印井号的装饰器
def f5():
    print("666")

# 测试带参数的装饰器
print("\n使用带参数装饰器 - 横线：")
f2()

print("\n使用带参数装饰器 - 等号：")
f3()

print("\n使用带参数装饰器 - 星号：")
f4()

print("\n使用带参数装饰器 - 井号：")
f5()


# ============== 第六部分：原理解析 ==============
print("\n" + "=" * 50)
print("原理解析")
print("=" * 50)

# 等价写法演示
print("@get_decorator('-') 的等价写法：")

def f6():
    print("666")

# 手动执行装饰过程
decorator = get_decorator("-")  # 1.先获取装饰器
f6 = decorator(f6)             # 2.再装饰函数

print("手动装饰的结果：")
f6()


# ============== 第七部分：进阶示例 - 更复杂的参数 ==============
print("\n" + "=" * 50)
print("进阶示例：更复杂的参数装饰器")
print("=" * 50)

def advanced_decorator(char, count, prefix=""):
    """
    更复杂的参数装饰器
    
    参数：
    char: 装饰字符
    count: 字符重复次数  
    prefix: 前缀文本
    """
    def decorator(func):
        def inner():
            if prefix:
                print(f"{prefix}:")
            print(char * count)
            func()
            print(char * count)
        return inner
    return decorator


@advanced_decorator("*", 20, "开始执行")
def f7():
    print("这是一个重要的函数")

@advanced_decorator("=", 15, "DEBUG")  
def f8():
    print("调试信息")

print("复杂参数装饰器示例1：")
f7()

print("\n复杂参数装饰器示例2：")
f8()


# ============== 总结 ==============
print("\n" + "=" * 60)
print("重点总结")
print("=" * 60)
print("""
1. 装饰器语法糖原理：
   @decorator 等价于 func = decorator(func)

2. 带参数装饰器的三层结构：
   - 外层：参数接收函数（装饰器工厂）
   - 中层：真正的装饰器函数  
   - 内层：装饰后的函数

3. 核心理解：
   @get_decorator(param) 会先调用 get_decorator(param) 
   获取装饰器，然后用这个装饰器去装饰下面的函数

4. 优势：
   - 避免重复代码
   - 提高代码复用性
   - 参数化配置装饰行为
""")
