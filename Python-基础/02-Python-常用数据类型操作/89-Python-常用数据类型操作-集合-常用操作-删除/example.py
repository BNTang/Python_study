# -*- coding: utf-8 -*-

# @Time    : 2025-5-24
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 89-Python-常用数据类型操作-集合-常用操作-删除

"""
可变集合的删除操作
主要包含以下几种方法：
1. remove() - 删除指定元素，元素不存在时抛出KeyError
2. discard() - 删除指定元素，元素不存在时不做任何操作
3. pop() - 随机删除并返回一个元素
4. clear() - 清空集合中的所有元素
"""

print("=== 集合删除操作示例 ===\n")

# 1. remove() 方法 - 删除指定元素，不存在则报错
print("1. remove() 方法示例：")
s = {1, 2, 3}
print(f"原始集合: {s}")
result = s.remove(3)  # 删除元素3
print(f"remove(3)返回值: {result}")  # 返回None
print(f"删除后的集合: {s}")  # {1, 2}

# 演示remove()删除不存在元素的情况
print("\n尝试删除不存在的元素:")
s2 = {1, 2, 3}
try:
    s2.remove(13)  # 尝试删除不存在的元素
except KeyError as e:
    print(f"KeyError: {e}")

print()

# 2. discard() 方法 - 删除指定元素，不存在则不做任何操作
print("2. discard() 方法示例：")
s = {1, 2, 3}
print(f"原始集合: {s}")
result = s.discard(3)  # 删除元素3
print(f"discard(3)返回值: {result}")  # 返回None
print(f"删除后的集合: {s}")  # {1, 2}

# 演示discard()删除不存在元素的情况
print("\n尝试删除不存在的元素:")
s3 = {1, 2, 3}
result = s3.discard(13)  # 删除不存在的元素，不会报错
print(f"discard(13)返回值: {result}")
print(f"集合保持不变: {s3}")

print()

# 3. pop() 方法 - 随机删除并返回一个元素
print("3. pop() 方法示例：")
s = {1, 2, 3}
print(f"原始集合: {s}")

# 连续执行pop操作
result1 = s.pop()
print(f"第一次pop()返回: {result1}, 剩余集合: {s}")

result2 = s.pop()
print(f"第二次pop()返回: {result2}, 剩余集合: {s}")

result3 = s.pop()
print(f"第三次pop()返回: {result3}, 剩余集合: {s}")

# 演示从空集合pop的情况
print("\n尝试从空集合pop:")
try:
    s.pop()  # 从空集合pop
except KeyError as e:
    print(f"KeyError: pop from an empty set")

print()

# 4. clear() 方法 - 清空集合中所有元素
print("4. clear() 方法示例：")
s = {1, 2, 3}
print(f"原始集合: {s}")
result = s.clear()  # 清空集合
print(f"clear()返回值: {result}")  # 返回None
print(f"清空后的集合: {s}")  # set()空集合
print(f"集合是否还存在: {s is not None}")  # True，集合对象仍然存在

# 可以继续向清空后的集合添加元素
s.add(100)
print(f"向清空后的集合添加元素100: {s}")

print()

# 补充：使用del删除整个集合变量
print("5. 使用del删除整个集合变量：")
temp_set = {1, 2, 3}
print(f"删除前: temp_set = {temp_set}")
del temp_set  # 删除整个变量
try:
    print(temp_set)  # 尝试访问已删除的变量
except NameError:
    print("NameError: temp_set已被删除，无法访问")

print("\n=== 集合删除操作总结 ===")
print("- remove(): 删除指定元素，不存在时抛出异常")
print("- discard(): 删除指定元素，不存在时静默忽略")
print("- pop(): 随机删除并返回元素，空集合时抛出异常")
print("- clear(): 清空所有元素，保留集合对象")
print("- del: 删除整个集合变量")
