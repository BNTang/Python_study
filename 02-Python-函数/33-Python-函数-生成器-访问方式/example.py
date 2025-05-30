# -*- coding: utf-8 -*-

# @Time    : 2025-5-30
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 33-Python-函数-生成器-访问方式

print("=" * 50)
print("生成器的两种创建方式和访问方式")
print("=" * 50)

# 1. 生成器表达式 - 将列表推导式的[]改为()
print("\n1. 生成器表达式:")
# 列表推导式
list_comp = [x for x in range(5)]
print(f"列表推导式: {list_comp}")

# 生成器表达式 - 重点：中括号改成小括号
gen_exp = (x for x in range(5))
print(f"生成器表达式: {gen_exp}")
print(f"生成器类型: {type(gen_exp)}")

# 2. 生成器函数 - 包含yield语句的函数
print("\n2. 生成器函数:")

def simple_generator():
    """简单的生成器函数示例"""
    print("开始执行")
    yield 1
    print("第一次暂停后继续")
    yield 2
    print("第二次暂停后继续")
    yield 3
    print("函数执行结束")

# 生成器函数的执行结果是一个生成器对象
gen_func = simple_generator()
print(f"生成器函数返回: {gen_func}")
print(f"生成器类型: {type(gen_func)}")

# 3. 使用for循环的生成器函数
print("\n3. 使用for循环的生成器函数:")

def range_generator():
    """使用for循环的生成器函数"""
    for i in range(1, 6):
        print(f"生成值: {i}")
        yield i

gen_range = range_generator()
print(f"for循环生成器: {gen_range}")

print("\n" + "=" * 50)
print("生成器的访问方式")
print("=" * 50)

# 方式1: 使用next()函数访问
print("\n方式1: 使用next()函数逐个访问")
gen1 = simple_generator()
try:
    print(f"第1次调用next(): {next(gen1)}")
    print(f"第2次调用next(): {next(gen1)}")
    print(f"第3次调用next(): {next(gen1)}")
    print(f"第4次调用next(): {next(gen1)}")  # 这里会抛出StopIteration异常
except StopIteration:
    print("生成器已耗尽，抛出StopIteration异常")

# 方式2: 使用生成器.__next__()方法
print("\n方式2: 使用生成器.__next__()方法")
gen2 = range_generator()
try:
    print(f"第1次调用__next__(): {gen2.__next__()}")
    print(f"第2次调用__next__(): {gen2.__next__()}")
    print(f"第3次调用__next__(): {gen2.__next__()}")
except StopIteration:
    print("生成器已耗尽")

# 方式3: 使用for循环遍历（推荐方式）
print("\n方式3: 使用for循环遍历（推荐）")
gen3 = range_generator()
for value in gen3:
    print(f"for循环获取: {value}")

# 方式4: 转换为列表（一次性获取所有值）
print("\n方式4: 转换为列表")
gen4 = (x ** 2 for x in range(5))
result_list = list(gen4)
print(f"转换为列表: {result_list}")

print("\n" + "=" * 50)
print("生成器的特点和注意事项")
print("=" * 50)

print("\n生成器的重要特点:")
print("1. 惰性求值 - 只有在需要时才计算下一个值")
print("2. 内存高效 - 不会一次性生成所有值")
print("3. 只能遍历一次 - 一旦耗尽就不能重新开始")
print("4. yield语句会暂停函数执行并返回值")

# 演示生成器只能遍历一次的特点
print("\n演示：生成器只能遍历一次")
gen_once = (x for x in range(3))
print("第一次遍历:")
for val in gen_once:
    print(f"  {val}")

print("第二次遍历:")
for val in gen_once:
    print(f"  {val}")
print("  (没有输出，因为生成器已耗尽)")

# 如果需要多次遍历，需要重新创建生成器
print("\n如果需要多次遍历，重新创建生成器:")
def create_gen():
    return (x for x in range(3))

gen_new1 = create_gen()
gen_new2 = create_gen()

print("第一个生成器:")
for val in gen_new1:
    print(f"  {val}")

print("第二个生成器:")
for val in gen_new2:
    print(f"  {val}")

print("\n学习重点总结:")
print("• 生成器表达式：(表达式 for 变量 in 可迭代对象)")
print("• 生成器函数：包含yield语句的函数")
print("• 访问方式：next()函数、__next__()方法、for循环")
print("• 核心特点：惰性求值、内存高效、一次性遍历")
