# -*- coding: utf-8 -*-

# @Time    : 2025-5-30
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 31-Python-函数-生成器-创建方式-1

"""
生成器创建方式一：生成器表达式
核心概念：将列表推导式的中括号改为小括号即可创建生成器
"""

print("=" * 50)
print("1. 列表推导式回顾")
print("=" * 50)

# 列表推导式：生成1-100中的所有偶数
l = [i for i in range(1, 101) if i % 2 == 0]
print("列表推导式结果:", l[:10], "...(共", len(l), "个元素)")
print("列表类型:", type(l))

print("\n" + "=" * 50)
print("2. 大数据量列表的问题演示")
print("=" * 50)

# 演示大数据量列表的内存占用问题
print("创建1-10000的偶数列表...")
large_list = [i for i in range(1, 10001) if i % 2 == 0]
print("大列表创建完成，占用内存较大")
print("前10个元素:", large_list[:10])
print("总元素数:", len(large_list))

print("\n" + "=" * 50)
print("3. 生成器表达式 - 解决方案")
print("=" * 50)

# 生成器表达式：将中括号改为小括号
g = (i for i in range(1, 10001) if i % 2 == 0)
print("生成器对象:", g)
print("生成器类型:", type(g))
print("注意：Generator对象，不会立即计算所有值")

print("\n" + "=" * 50)
print("4. 访问生成器元素的方法")
print("=" * 50)

# 方法1：使用next()函数
print("方法1：使用next()函数逐个获取元素")
g1 = (i for i in range(1, 21) if i % 2 == 0)
print("第1个元素:", next(g1))
print("第2个元素:", next(g1))
print("第3个元素:", next(g1))

# 方法2：使用生成器的__next__()方法
print("\n方法2：使用__next__()方法")
g2 = (i for i in range(1, 21) if i % 2 == 0)
print("第1个元素:", g2.__next__())
print("第2个元素:", g2.__next__())
print("第3个元素:", g2.__next__())

print("\n" + "=" * 50)
print("5. 使用for循环遍历生成器")
print("=" * 50)

# 方法3：使用for循环遍历
print("方法3：使用for循环遍历生成器")
g3 = (i for i in range(1, 21) if i % 2 == 0)
print("生成器中的所有偶数:")
for i in g3:
    print(i, end=" ")
print()

print("\n" + "=" * 50)
print("6. 生成器的特性总结")
print("=" * 50)

print("✓ 惰性计算：不会一次性生成所有元素")
print("✓ 内存高效：只在需要时才计算下一个值")
print("✓ 状态记录：记住上次访问的位置")
print("✓ 一次性使用：遍历后生成器就被耗尽了")

# 演示生成器的一次性特性
print("\n演示生成器的一次性特性:")
g4 = (i for i in range(1, 11) if i % 2 == 0)
print("第一次遍历:")
for i in g4:
    print(i, end=" ")
print()

print("第二次遍历（生成器已耗尽）:")
for i in g4:
    print(i, end=" ")
print("(无输出，因为生成器已被耗尽)")

print("\n" + "=" * 50)
print("7. 实际应用示例")
print("=" * 50)

# 实际应用：处理大量数据时使用生成器
def process_large_data():
    """模拟处理大量数据的场景"""
    print("使用生成器处理1-1000000的平方数（仅取前5个）:")
    
    # 生成器表达式：计算平方数
    squares = (x**2 for x in range(1, 1000001))
    
    # 只取前5个，不会计算全部100万个数
    count = 0
    for square in squares:
        print(f"数字 {count+1} 的平方: {square}")
        count += 1
        if count >= 5:
            break
    
    print("优势：即使数据量很大，也只计算了需要的部分")

process_large_data()

print("\n" + "=" * 50)
print("核心要点")
print("=" * 50)
print("1. 生成器表达式语法：(表达式 for 变量 in 可迭代对象 if 条件)")
print("2. 与列表推导式的区别：中括号[] → 小括号()")
print("3. 生成器是特殊的迭代器，具有迭代器的所有特性")
print("4. 适用场景：大数据量处理、内存敏感的应用")
