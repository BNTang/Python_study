# -*- coding: utf-8 -*-

# @Time    : 2025-5-30
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 36-Python-函数-生成器-注意事项

"""
生成器的两个重要注意事项：
1. 生成器遇到return语句的处理方式
2. 生成器只能迭代一次的特性
"""

def demo_generator():
    """演示生成器基本功能"""
    print("a")
    yield 1
    print("b") 
    yield 2
    print("c")
    yield 3

def generator_with_return():
    """演示带return语句的生成器"""
    print("a")
    yield 1
    print("b")
    yield 2
    # return语句会抛出StopIteration异常，并将返回值作为异常的value
    return 10
    print("c")  # 这行代码永远不会执行
    yield 3

print("=" * 50)
print("注意事项1：生成器遇到return语句的处理")
print("=" * 50)

# 正常的生成器
print("正常生成器演示：")
g1 = demo_generator()
print(f"第一次调用: {next(g1)}")  # 输出: a 和 1
print(f"第二次调用: {next(g1)}")  # 输出: b 和 2  
print(f"第三次调用: {next(g1)}")  # 输出: c 和 3

print("\n带return语句的生成器演示：")
g2 = generator_with_return()
print(f"第一次调用: {next(g2)}")  # 输出: a 和 1
print(f"第二次调用: {next(g2)}")  # 输出: b 和 2

# 第三次调用会遇到return语句，抛出StopIteration异常
try:
    print(f"第三次调用: {next(g2)}")
except StopIteration as e:
    print(f"遇到return语句，抛出StopIteration异常，返回值: {e.value}")

print("\n" + "=" * 50)
print("注意事项2：生成器只能迭代一次")
print("=" * 50)

# 创建生成器
g = demo_generator()

print("第一次遍历生成器：")
for i in g:
    print(f"获取到值: {i}")

print("\n第二次遍历同一个生成器：")
for i in g:
    print(f"获取到值: {i}")
print("没有任何输出，因为生成器已经耗尽")

print("\n" + "-" * 30)

print("重新创建生成器进行第二次遍历：")
g = demo_generator()  # 重新创建生成器
for i in g:
    print(f"获取到值: {i}")

print("\n" + "=" * 50)
print("总结")
print("=" * 50)
print("1. 生成器遇到return语句时：")
print("   - 立即终止生成器")
print("   - 抛出StopIteration异常")
print("   - return的值作为异常的value属性")
print("   - return后的代码不会执行")
print("\n2. 生成器只能迭代一次：")
print("   - 生成器是一次性的迭代器")
print("   - 迭代完成后，生成器就耗尽了")
print("   - 如果需要再次迭代，必须重新创建生成器")

# 额外演示：通过异常捕获获取return值
print("\n" + "=" * 50)
print("额外演示：手动捕获return值")
print("=" * 50)

def generator_return_demo():
    yield "开始"
    yield "中间"
    return "结束值"

g3 = generator_return_demo()
try:
    while True:
        value = next(g3)
        print(f"yield值: {value}")
except StopIteration as e:
    print(f"生成器结束，return值: {e.value}")
