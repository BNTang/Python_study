# -*- coding: utf-8 -*-

# @Time    : 2025-5-23
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 87-Python-常用数据类型操作-集合-定义时注意事项

# 1.创建一个空集合时,需要使用set() 或者 frozenset(),不能使用s={}
print("=== 1.创建空集合的注意事项 ===")
# 错误的方式 - 会被识别成为字典
empty_dict = {}
print(f"empty_dict = {{}} 的类型: {type(empty_dict)}")

# 正确的方式 - 创建空集合
empty_set = set()
empty_frozenset = frozenset()
print(f"empty_set = set() 的类型: {type(empty_set)}")
print(f"empty_frozenset = frozenset() 的类型: {type(empty_frozenset)}")

print("\n=== 2.集合中的元素,必须是可哈希的值 ===")
# 如果一个对象在自己的生命周期中有一个哈希值(hash value)是不可改变的
# 那么它就是可哈希的(hashable)的
# 暂时理解为不可变类型

# 可哈希的值 - 可以作为集合元素
hashable_set = {1, 2.5, "hello", (1, 2), True}
print(f"可哈希元素的集合: {hashable_set}")

# 不可哈希的值 - 不能作为集合元素
print("尝试添加不可哈希的元素:")
try:
    # 列表是不可哈希的
    invalid_set = {1, 2, [3, 4]}
except TypeError as e:
    print(f"添加列表失败: {e}")

try:
    # 字典是不可哈希的
    invalid_set = {1, 2, {"key": "value"}}
except TypeError as e:
    print(f"添加字典失败: {e}")

try:
    # 集合本身也是不可哈希的
    invalid_set = {1, 2, {3, 4}}
except TypeError as e:
    print(f"添加集合失败: {e}")

print("\n=== 3.如果集合中的元素值出现重复,则会被合并为1个 ===")
# 重复元素会被自动去重
duplicate_set = {1, 2, 3, 2, 1, 4, 3, 5}
print(f"包含重复元素的集合: {{1, 2, 3, 2, 1, 4, 3, 5}}")
print(f"实际结果(去重后): {duplicate_set}")

# 不同类型但值相等的元素也会被去重
mixed_set = {1, 1.0, True, False, 0, 0.0}
print(f"混合类型的集合: {{1, 1.0, True, False, 0, 0.0}}")
print(f"实际结果(去重后): {mixed_set}")
print("注意: 1, 1.0, True 在Python中被认为是相等的")
print("注意: 0, 0.0, False 在Python中被认为是相等的")