# -*- coding: utf-8 -*-

# @Time    : 2025-5-28
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 16-Python-函数-匿名函数(lambda函数)

"""
Lambda函数（匿名函数）学习指南

什么是Lambda函数？
- 匿名函数：没有名字的函数
- 语法简洁：只能写一个表达式
- 返回值：表达式的结果就是返回值
- 适用场景：简单的操作处理

基本语法：
lambda 参数: 表达式
"""

print("=" * 50)
print("1. Lambda函数基础语法")
print("=" * 50)

# 1.1 最简单的lambda函数
simple_lambda = lambda x, y: x + y
print(f"lambda x, y: x + y")
print(f"结果: {simple_lambda(1, 2)}")  # 输出: 3

# 1.2 直接调用lambda函数（不推荐，但可以理解原理）
result = (lambda x, y: x + y)(4, 5)
print(f"直接调用: (lambda x, y: x + y)(4, 5) = {result}")  # 输出: 9

print("\n" + "=" * 50)
print("2. Lambda函数与普通函数对比")
print("=" * 50)

# 普通函数
def normal_add(x, y):
    return x + y

# Lambda函数
lambda_add = lambda x, y: x + y

print(f"普通函数: normal_add(3, 4) = {normal_add(3, 4)}")
print(f"Lambda函数: lambda_add(3, 4) = {lambda_add(3, 4)}")

print("\n" + "=" * 50)
print("3. 实际应用场景 - 配合内置函数使用")
print("=" * 50)

# 3.1 与map()函数配合使用
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"原数据: {numbers}")
print(f"平方后: {squared}")

# 3.2 与filter()函数配合使用
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"原数据: {numbers}")
print(f"偶数: {even_numbers}")

# 3.3 与sorted()函数配合使用
students = [
    {"name": "张三", "age": 20, "score": 85},
    {"name": "李四", "age": 19, "score": 92},
    {"name": "王五", "age": 21, "score": 78}
]

print(f"\n原始学生数据:")
for student in students:
    print(f"  {student}")

# 按年龄排序
sorted_by_age = sorted(students, key=lambda x: x["age"])
print(f"\n按年龄排序:")
for student in sorted_by_age:
    print(f"  {student}")

# 按分数排序（降序）
sorted_by_score = sorted(students, key=lambda x: x["score"], reverse=True)
print(f"\n按分数排序（降序）:")
for student in sorted_by_score:
    print(f"  {student}")

print("\n" + "=" * 50)
print("4. Lambda函数的限制")
print("=" * 50)

# Lambda函数只能包含表达式，不能包含语句
# 错误示例（注释掉，仅供理解）
# wrong_lambda = lambda x: print(x)  # 这样会报错，因为print是语句不是表达式

# 正确的方式是使用普通函数
def print_value(x):
    print(x)
    return x

print("Lambda函数限制:")
print("- 只能写一个表达式")
print("- 不能包含语句（如print、赋值等）")
print("- 适用于简单逻辑")

print("\n" + "=" * 50)
print("5. 更多实用示例")
print("=" * 50)

# 5.1 字符串操作
words = ["hello", "world", "python", "programming"]
capitalized = list(map(lambda x: x.capitalize(), words))
print(f"原单词: {words}")
print(f"首字母大写: {capitalized}")

# 5.2 条件表达式
# lambda中使用三元运算符
check_even = lambda x: "偶数" if x % 2 == 0 else "奇数"
print(f"\n数字类型判断:")
for i in range(1, 6):
    print(f"{i} 是 {check_even(i)}")

# 5.3 多个条件
grade_level = lambda score: "优秀" if score >= 90 else "良好" if score >= 80 else "及格" if score >= 60 else "不及格"
scores = [95, 85, 75, 55]
print(f"\n成绩等级:")
for score in scores:
    print(f"{score}分: {grade_level(score)}")

print("\n" + "=" * 50)
print("学习总结")
print("=" * 50)
print("Lambda函数要点:")
print("1. 语法: lambda 参数: 表达式")
print("2. 主要用途: 作为参数传递给其他函数")
print("3. 常用场合: map(), filter(), sorted()等")
print("4. 优点: 代码简洁，适合简单逻辑")
print("5. 缺点: 只能写表达式，复杂逻辑还是用普通函数")
