# -*- coding: utf-8 -*-

# @Time    : 2025-5-24
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 92-Python-常用数据类型操作-集合-常用操作-交集补充

"""
集合交集操作补充说明
重点：intersection() 方法可以接收可迭代对象作为参数
但是可迭代对象内部的元素必须是可哈希的
"""

print("=" * 60)
print("集合交集操作补充说明")
print("=" * 60)

# 1. 集合与数字字符串的交集（注意类型问题）
print("\n1. 集合与数字的交集演示:")
s1 = {1, 2, 3}
print(f"集合 s1 = {s1}")

# 错误示例：数字字符串与数字集合
print(f"\ns1.intersection('123') = {s1.intersection('123')}")
print("结果为空集，因为字符串'123'被拆分为字符'1','2','3'，与数字1,2,3不相等")

# 正确示例：字符串集合与字符串的交集
s1_str = {'1', '2', '3'}
print(f"\n字符串集合 s1_str = {s1_str}")
print(f"s1_str.intersection('123') = {s1_str.intersection('123')}")
print("结果正确，因为字符串'123'被拆分为字符'1','2','3'，与字符串集合元素匹配")

# 2. 集合与列表的交集
print("\n" + "=" * 40)
print("2. 集合与列表的交集:")
s2 = {1, 2, 3, 4, 5}
list1 = [1, 2, 6]
print(f"集合 s2 = {s2}")
print(f"列表 list1 = {list1}")
print(f"s2.intersection(list1) = {s2.intersection(list1)}")
print("列表中的元素1,2在集合中存在，所以交集为{1, 2}")

# 3. 集合与字典的交集（注意：字典的键参与运算）
print("\n" + "=" * 40)
print("3. 集合与字典的交集:")
s3 = {1, 2, 3, 4, 5}
dict1 = {1: 'abc', 2: '12', 6: 10}
print(f"集合 s3 = {s3}")
print(f"字典 dict1 = {dict1}")
print(f"s3.intersection(dict1) = {s3.intersection(dict1)}")
print("注意：字典参与交集运算时，使用的是字典的键，不是值")
print("字典的键1,2在集合中存在，所以交集为{1, 2}")

# 4. 可迭代对象元素必须可哈希的限制
print("\n" + "=" * 40)
print("4. 不可哈希元素的错误示例:")
s4 = {1, 2, 3}
list_with_list = [1, 2, [1, 2]]  # 列表中包含列表（不可哈希）

print(f"集合 s4 = {s4}")
print(f"包含列表的列表 list_with_list = {list_with_list}")

try:
    result = s4.intersection(list_with_list)
    print(f"交集结果: {result}")
except TypeError as e:
    print(f"错误: {e}")
    print("原因: 列表[1, 2]是不可哈希的，不能作为集合元素")

print("\n" + "=" * 40)
print("错误原因分析:")
print("1. intersection()方法会将传入的可迭代对象转换为集合")
print("2. 转换过程中遇到不可哈希的元素（如列表）就会报错")
print("3. 虽然逻辑上可能有交集，但在类型转换阶段就失败了")

# 5. 更多可迭代对象的交集示例
print("\n" + "=" * 40)
print("5. 其他可迭代对象的交集:")

# 与元组的交集
s5 = {1, 2, 3, 4}
tuple1 = (2, 3, 5, 6)
print(f"集合与元组: s5.intersection({tuple1}) = {s5.intersection(tuple1)}")

# 与range对象的交集
range1 = range(1, 5)
print(f"集合与range: s5.intersection(range(1, 5)) = {s5.intersection(range1)}")

# 与集合的交集
set2 = {3, 4, 5, 6}
print(f"集合与集合: s5.intersection({set2}) = {s5.intersection(set2)}")

print("\n" + "=" * 60)
print("总结:")
print("1. intersection()方法的参数必须是可迭代对象")
print("2. 可迭代对象包括：字符串、列表、元组、字典、集合、range等")
print("3. 字典参与交集运算时使用的是键，不是值")
print("4. 可迭代对象内的所有元素必须是可哈希的")
print("5. 方法内部会先将可迭代对象转换为集合，再进行交集运算")
print("6. 不可哈希的元素（如列表、字典）会导致转换失败")
print("=" * 60)
