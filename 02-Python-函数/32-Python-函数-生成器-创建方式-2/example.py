# -*- coding: utf-8 -*-

# @Time    : 2025-5-30
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 32-Python-函数-生成器-创建方式-2

"""
生成器创建方式2：通过生成器函数创建

重点知识：
1. 生成器函数必须包含yield语句
2. 函数执行结果是一个生成器对象，而不是直接执行函数体
3. yield语句会暂停函数执行，并返回状态值
4. 使用next()函数可以让生成器继续执行到下一个yield
5. 生成器执行完毕后会抛出StopIteration异常
"""

def test_generator():
    """
    生成器函数示例
    包含多个yield语句，演示生成器的暂停和恢复机制
    """
    print("xxx")  # 函数开始执行标记
    
    yield 1  # 第一个状态值
    print("a")  # 第一次恢复执行后的代码
    
    yield 2  # 第二个状态值
    print("b")  # 第二次恢复执行后的代码
    
    yield 3  # 第三个状态值
    print("c")  # 第三次恢复执行后的代码
    
    yield 4  # 第四个状态值
    print("d")  # 第四次恢复执行后的代码
    
    yield 5  # 第五个状态值
    print("e")  # 第五次恢复执行后的代码

def demonstrate_generator():
    """演示生成器的基本使用"""
    print("=== 生成器创建演示 ===")
    
    # 调用生成器函数，返回生成器对象
    g = test_generator()
    print(f"生成器对象类型: {type(g)}")
    print(f"生成器对象: {g}")
    
    print("\n=== 生成器执行演示 ===")
    
    # 第一次调用next() - 执行到第一个yield
    print("第一次调用next():")
    result1 = next(g)
    print(f"返回值: {result1}")
    
    # 第二次调用next() - 从上次暂停位置继续，执行到第二个yield
    print("\n第二次调用next():")
    result2 = next(g)
    print(f"返回值: {result2}")
    
    # 第三次调用next()
    print("\n第三次调用next():")
    result3 = next(g)
    print(f"返回值: {result3}")
    
    # 第四次调用next()
    print("\n第四次调用next():")
    result4 = next(g)
    print(f"返回值: {result4}")
    
    # 第五次调用next()
    print("\n第五次调用next():")
    result5 = next(g)
    print(f"返回值: {result5}")
    
    # 第六次调用next() - 会抛出StopIteration异常
    print("\n第六次调用next() - 生成器已耗尽:")
    try:
        result6 = next(g)
        print(f"返回值: {result6}")
    except StopIteration:
        print("捕获到StopIteration异常 - 生成器已执行完毕")

def generator_with_loop():
    """使用循环创建生成器"""
    print("\n=== 使用循环的生成器示例 ===")
    
    def number_generator(n):
        """生成0到n-1的数字"""
        print(f"开始生成0到{n-1}的数字")
        for i in range(n):
            print(f"即将yield: {i}")
            yield i
            print(f"yield {i}之后继续执行")
    
    # 创建生成器
    gen = number_generator(3)
    
    # 使用next()逐个获取值
    for i in range(4):  # 故意多调用一次来演示异常
        try:
            value = next(gen)
            print(f"获取到值: {value}")
        except StopIteration:
            print("生成器执行完毕")
            break

def generator_vs_function():
    """对比普通函数和生成器函数的区别"""
    print("\n=== 普通函数 vs 生成器函数对比 ===")
    
    def normal_function():
        """普通函数"""
        print("普通函数开始执行")
        print("普通函数执行中...")
        print("普通函数执行完毕")
        return "普通函数返回值"
    
    def generator_function():
        """生成器函数"""
        print("生成器函数开始执行")
        yield "第一个值"
        print("生成器函数继续执行")
        yield "第二个值"
        print("生成器函数执行完毕")
    
    print("调用普通函数:")
    result = normal_function()
    print(f"普通函数返回: {result}")
    
    print("\n调用生成器函数:")
    gen = generator_function()
    print(f"生成器函数返回: {gen}")
    print("注意：生成器函数体此时还没有执行！")
    
    print("\n开始迭代生成器:")
    print("第一次next():", next(gen))
    print("第二次next():", next(gen))

if __name__ == "__main__":
    # 基本生成器演示
    demonstrate_generator()
    
    # 循环生成器演示
    generator_with_loop()
    
    # 对比演示
    generator_vs_function()
    
    print("\n" + "="*50)
    print("生成器重点总结:")
    print("1. 生成器函数包含yield语句")
    print("2. 调用生成器函数返回生成器对象，不会立即执行函数体")
    print("3. yield暂停函数执行并返回状态值")
    print("4. next()函数让生成器从上次暂停位置继续执行")
    print("5. 生成器耗尽时抛出StopIteration异常")
    print("6. 生成器是一种特殊的迭代器，节省内存")
