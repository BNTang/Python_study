# -*- coding: utf-8 -*-

# @Time    : 2025-5-24
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 90-Python-常用数据类型操作-集合-常用操作-查询遍历

# 集合的查询和遍历操作
# 集合不支持索引访问，但可以进行遍历操作

print("=== 可变集合(set)的遍历操作 ===")

# 创建一个可变集合
s = {1, 2, 3}
print(f"集合s: {s}")
print(f"集合类型: {type(s)}")

# 方法1: 使用for循环遍历集合
print("\n1. 使用for循环遍历:")
for v in s:
    print(v)

print("\n2. 使用迭代器遍历:")
# 第一步：生成迭代器
its = iter(s)
print(f"迭代器对象: {its}")

# 使用next()函数访问迭代器
print("使用next()函数访问:")
print(next(its))  # 第一个元素
print(next(its))  # 第二个元素
print(next(its))  # 第三个元素

# 注意：迭代器用完后不能重复使用
# 如果继续调用next()会抛出StopIteration异常
# print(next(its))  # 这行会报错

print("\n" + "-" * 30)

# 重新创建迭代器进行for循环遍历
its = iter(s)
print("使用for循环遍历迭代器:")
for v in its:
    print(v)

print("\n=== 不可变集合(frozenset)的遍历操作 ===")

# 创建不可变集合
fs = frozenset([1, 2, 3])
print(f"不可变集合fs: {fs}")
print(f"集合类型: {type(fs)}")

# 不可变集合的遍历方式和可变集合完全一样
print("\n遍历不可变集合:")
for v in fs:
    print(v)

# 使用迭代器遍历不可变集合
print("\n使用迭代器遍历不可变集合:")
its_frozen = iter(fs)
for v in its_frozen:
    print(v)

print("\n=== 集合的查询操作 ===")

# 集合不支持索引访问，但可以检查元素是否存在
test_set = {1, 2, 3, 4, 5}
print(f"测试集合: {test_set}")

# 检查元素是否在集合中
print(f"3 是否在集合中: {3 in test_set}")
print(f"6 是否在集合中: {6 in test_set}")

# 获取集合长度
print(f"集合长度: {len(test_set)}")

# 集合为空检查
empty_set = set()
print(f"空集合: {empty_set}")
print(f"集合是否为空: {len(empty_set) == 0}")

print("\n程序执行完毕!")
