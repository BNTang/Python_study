# -*- coding: utf-8 -*-

# @Time    : 2025-5-27
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 07-Python-函数-参数-不定长参数-缺省参数

# 1. 演示sorted函数的缺省参数使用
print("=== sorted函数演示 ===")

# 基本排序（升序，默认reverse=False）
my_list = [1, 3, 2, 5, 4]
result = sorted(my_list)
print(f"原列表: {my_list}")
print(f"升序排序: {result}")

# 指定reverse=True进行降序排序
result_desc = sorted(my_list, reverse=True)
print(f"降序排序: {result_desc}")

print("\n=== 自定义缺省参数函数 ===")

# 2. 定义带缺省参数的函数
def hit(somebody="豆豆"):
    """
    打某个人的函数
    :param somebody: 要打的人，默认是豆豆
    """
    print(f"我想打{somebody}")

# 传递参数调用
print("传递参数调用:")
hit("张三")

# 不传递参数调用（使用默认值）
print("不传递参数调用:")
hit()

print("\n=== 必填参数 vs 缺省参数对比 ===")

# 3. 必填参数的函数（没有默认值）
def hit_required(somebody):
    """
    必填参数版本的函数
    :param somebody: 必须传递的参数
    """
    print(f"我想打{somebody}")

# 正常调用必填参数函数
print("必填参数函数正常调用:")
hit_required("李四")

# 演示不传参数会报错（注释掉避免程序中断）
print("必填参数函数不传参数会报错:")
print("# hit_required()  # TypeError: hit_required() missing 1 required positional argument: 'somebody'")

print("\n=== 缺省参数的优势 ===")

# 4. 更复杂的缺省参数示例
def greet(name, greeting="你好", punctuation="!"):
    """
    问候函数，演示多个缺省参数
    :param name: 姓名（必填）
    :param greeting: 问候语（缺省参数，默认"你好"）
    :param punctuation: 标点符号（缺省参数，默认"!"）
    """
    message = f"{greeting}, {name}{punctuation}"
    print(message)

# 不同的调用方式
print("多种调用方式:")
greet("小明")  # 只传必填参数
greet("小红", "欢迎")  # 传递一个缺省参数
greet("小刚", "早上好", ".")  # 传递所有参数

print("\n=== 缺省参数的应用场景总结 ===")
print("1. 大多数情况下使用固定值的参数")
print("2. 主功能之外的可选小功能")
print("3. 提高函数的易用性和灵活性")
