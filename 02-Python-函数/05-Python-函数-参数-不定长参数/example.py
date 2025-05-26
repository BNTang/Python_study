# -*- coding: utf-8 -*-

# @Time    : 2025-5-26
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 05-Python-函数-参数-不定长参数

# 不定长参数的引入
# 当我们需要处理不确定数量的参数时，固定参数的函数就显得不够灵活
# 比如计算多个数的和，我们不知道用户会传入几个数

# 1. 回顾：固定参数的局限性
def my_sum_fixed(number1, number2):
    """计算两个数的和"""
    return number1 + number2

print("固定参数版本(4+5):", my_sum_fixed(4, 5))  # 结果: 9

# 如果想计算三个数的和，需要重新定义函数
def my_sum_three(number1, number2, number3):
    """计算三个数的和"""
    return number1 + number2 + number3

print("三个参数版本(4+5+6):", my_sum_three(4, 5, 6))  # 结果: 15

# 2. 使用容器类型传参的方式
def my_sum_container(t):
    """通过传入元组或列表来计算多个数的和"""
    print(f"接收到的参数: {t}")
    print(f"参数类型: {type(t)}")
    
    # 遍历容器中的每个元素并求和
    result = 0
    for v in t:
        print(f"当前值: {v}")
        result += v
    
    return result

# 使用元组传参
print("容器方式(元组):", my_sum_container((4, 5, 6)))  # 结果: 15
print("容器方式(列表):", my_sum_container([4, 5, 6, 7]))  # 结果: 22

# 3. 方式一：*args - 不定长位置参数
def my_sum_args(*args):
    """使用*args接收不定数量的位置参数"""
    print(f"接收到的参数: {args}")
    print(f"参数类型: {type(args)}")
    
    # args是一个元组，可以直接遍历
    result = 0
    for value in args:
        result += value
    
    return result

# 调用*args版本 - 可以传入任意数量的参数
print("*args版本(4,5):", my_sum_args(4, 5))  # 结果: 9
print("*args版本(4,5,6):", my_sum_args(4, 5, 6))  # 结果: 15
print("*args版本(4,5,6,7):", my_sum_args(4, 5, 6, 7))  # 结果: 22
print("*args版本(1,2,3,4,5):", my_sum_args(1, 2, 3, 4, 5))  # 结果: 15

# 4. 方式二：**kwargs - 不定长关键字参数
def my_sum_kwargs(**kwargs):
    """使用**kwargs接收不定数量的关键字参数"""
    print(f"接收到的参数: {kwargs}")
    print(f"参数类型: {type(kwargs)}")
    
    # kwargs是一个字典，可以遍历值
    result = 0
    for key, value in kwargs.items():
        print(f"键: {key}, 值: {value}")
        result += value
    
    return result

# 调用**kwargs版本 - 必须使用关键字参数
print("**kwargs版本:")
result = my_sum_kwargs(name=5, age=12, score=8)
print(f"结果: {result}")  # 结果: 25

# 如果直接传位置参数会报错
# print(my_sum_kwargs(1, 2, 3))  # TypeError: my_sum_kwargs() takes 0 positional arguments but 3 were given

# 5. 混合使用：普通参数、*args、**kwargs
def complex_function(name, age=18, *args, **kwargs):
    """演示混合使用各种参数类型"""
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    print(f"额外位置参数: {args}")
    print(f"额外关键字参数: {kwargs}")
    
    # 计算args中数值的和
    args_sum = sum(args) if args else 0
    
    # 计算kwargs中数值的和
    kwargs_sum = sum(kwargs.values()) if kwargs else 0
    
    return args_sum + kwargs_sum

# 调用混合参数函数
print("\n混合参数示例:")
result = complex_function("张三", 25, 10, 20, 30, math=95, english=87)
print(f"数值总和: {result}")

# 6. 实际应用示例：格式化输出函数
def print_info(title, *items, **details):
    """格式化输出信息"""
    print(f"\n=== {title} ===")
    
    if items:
        print("项目列表:")
        for i, item in enumerate(items, 1):
            print(f"  {i}. {item}")
    
    if details:
        print("详细信息:")
        for key, value in details.items():
            print(f"  {key}: {value}")

# 使用格式化输出函数
print_info("学生信息", "数学", "物理", "化学", 
           姓名="李四", 班级="三年级", 成绩=95)

# 7. 参数解包：将容器类型的数据传给不定长参数
def calculate_sum(*args):
    """计算所有参数的和"""
    return sum(args)

# 正常调用
print("\n参数解包示例:")
print("正常调用:", calculate_sum(1, 2, 3, 4))

# 解包元组
numbers_tuple = (1, 2, 3, 4)
print("解包元组:", calculate_sum(*numbers_tuple))

# 解包列表
numbers_list = [1, 2, 3, 4, 5]
print("解包列表:", calculate_sum(*numbers_list))

# 8. 关键字参数解包
def student_info(**kwargs):
    """显示学生信息"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n关键字参数解包:")
info_dict = {"name": "王五", "age": 20, "grade": "大二"}
student_info(**info_dict)

# 总结：
# 1. *args: 接收任意数量的位置参数，在函数内部是元组类型
# 2. **kwargs: 接收任意数量的关键字参数，在函数内部是字典类型
# 3. 参数顺序: 普通参数 -> 默认参数 -> *args -> **kwargs
# 4. 元组前加*可以解包为位置参数，字典前加**可以解包为关键字参数
# 5. 不定长参数让函数更加灵活，可以处理不确定数量的输入
