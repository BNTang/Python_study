# -*- coding: utf-8 -*-

# @Time    : 2025-5-30
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 35-Python-函数-生成器-close方法

"""
生成器的close()方法学习
重点：
1. 生成器只能生成固定次数的值
2. 超出次数会抛出StopIteration异常
3. close()方法可以提前关闭生成器
4. 关闭后再次调用next()会抛出StopIteration异常
"""

def test():
    """生成器函数，包含3个yield语句"""
    yield 1
    print("a")
    yield 2
    print("b")
    yield 3
    print("c")

print("=== 正常使用生成器 ===")
# 创建生成器对象
g = test()

# 正常访问3次
print("第1次调用next():", next(g))
print("第2次调用next():", next(g))
print("第3次调用next():", next(g))

print("\n=== 超出次数访问会报错 ===")
try:
    # 第4次调用会报错，因为生成器只有3个值
    print("第4次调用next():", next(g))
except StopIteration:
    print("❌ 抛出StopIteration异常 - 生成器已耗尽")

print("\n=== 使用close()方法关闭生成器 ===")
# 重新创建生成器
g = test()

# 正常访问前2次
print("第1次调用next():", next(g))
print("第2次调用next():", next(g))

# 关闭生成器
print("调用g.close()关闭生成器...")
g.close()

# 关闭后再次访问会报错
try:
    print("关闭后调用next():", next(g))
except StopIteration:
    print("❌ 抛出StopIteration异常 - 生成器已被关闭")

print("\n=== close()方法的实际应用场景 ===")
def large_data_generator():
    """模拟大数据生成器"""
    for i in range(1000000):
        print(f"生成数据: {i}")
        yield i

# 创建大数据生成器
big_gen = large_data_generator()

# 只需要前5个数据
for i, value in enumerate(big_gen):
    if i >= 5:
        print("已获取足够数据，关闭生成器...")
        big_gen.close()  # 提前关闭，节省资源
        break
    print(f"获取到: {value}")

print("\n总结：")
print("✅ close()方法用于提前关闭生成器")
print("✅ 关闭后生成器无法继续使用")
print("✅ 适用于不需要完整遍历的场景")
print("✅ 可以节省资源，特别是处理大数据时")
