# -*- coding: utf-8 -*-

# @Time    : 2025-5-30
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 34-Python-函数-生成器-send方法

"""
生成器的send方法学习

重点知识：
1. send方法可以启动生成器（类似next）
2. send方法可以给yield语句传值
3. 第一次调用send必须传None
4. send的参数是上一次被挂起的yield语句的返回值
"""

def test_generator():
    """测试生成器函数"""
    print("生成器开始执行...")
    
    # 第一个yield语句
    res1 = yield 1
    print(f"res1的值是: {res1}")
    
    # 第二个yield语句  
    res2 = yield 2
    print(f"res2的值是: {res2}")
    
    return "生成器结束"

print("=" * 50)
print("演示1: 使用next方法启动生成器")
print("=" * 50)

# 创建生成器对象
g1 = test_generator()

# 使用next方法启动
print("第一次调用next():")
result1 = next(g1)  # 或者 g1.__next__()
print(f"返回值: {result1}")

print("\n第二次调用next():")
result2 = next(g1)
print(f"返回值: {result2}")

print("=" * 50)
print("演示2: 使用send方法启动生成器")
print("=" * 50)

# 重新创建生成器对象
g2 = test_generator()

# 【重点】第一次调用send必须传None，因为没有上一次的yield语句
print("第一次调用send(None):")
result1 = g2.send(None)
print(f"返回值: {result1}")

# 第二次可以传具体的值，会赋给上一次yield的返回值
print("\n第二次调用send('Hello'):")
result2 = g2.send("Hello")
print(f"返回值: {result2}")

# 第三次传入另一个值
print("\n第三次调用send(666):")
try:
    result3 = g2.send(666)
    print(f"返回值: {result3}")
except StopIteration as e:
    print(f"生成器结束，返回值: {e.value}")

print("=" * 50)
print("演示3: send方法的错误用法")
print("=" * 50)

# 创建新的生成器
g3 = test_generator()

# 【错误】第一次调用send时传入非None值会报错
try:
    print("尝试第一次调用send('error'):")
    g3.send("error")
except TypeError as e:
    print(f"错误信息: {e}")

print("=" * 50)
print("演示4: 实际应用场景 - 协程式数据处理")
print("=" * 50)

def data_processor():
    """数据处理器生成器"""
    total = 0
    count = 0
    
    while True:
        # 接收外部发送的数据
        data = yield f"当前总计: {total}, 平均值: {total/count if count > 0 else 0}"
        
        if data is None:
            break
            
        total += data
        count += 1
        print(f"接收到数据: {data}, 累计: {total}")

# 创建数据处理器
processor = data_processor()

# 启动处理器
print("启动处理器:")
status = processor.send(None)
print(status)

# 发送数据
print("\n发送数据 10:")
status = processor.send(10)
print(status)

print("\n发送数据 20:")
status = processor.send(20)
print(status)

print("\n发送数据 30:")
status = processor.send(30)
print(status)

# 结束处理器
print("\n结束处理器:")
try:
    processor.send(None)
except StopIteration:
    print("处理器已停止")

print("=" * 50)
print("总结:")
print("1. send()方法 = next()方法 + 传值功能")
print("2. 第一次调用send()必须传None")
print("3. send()的参数会成为上一次yield的返回值") 
print("4. 常用于协程和数据管道场景")
print("=" * 50)
