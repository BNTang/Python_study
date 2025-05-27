# -*- coding: utf-8 -*-

# @Time    : 2025-5-28
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 10-Python函数-函数的使用描述

"""
函数的使用描述 - Function Documentation

本章重点：
1. 函数的三种类型：内建函数、第三方函数、自定义函数
2. 函数文档字符串(docstring)的重要性
3. 如何编写规范的函数文档
4. 使用help()函数查看函数文档
"""

# ==================== 函数分类说明 ====================
"""
函数按提供方分为三类：
1. 内建函数 - Python自带的函数，可直接使用
   示例：len(), print(), type()

2. 第三方函数 - 由第三方开发者提供的函数
   示例：numpy.array(), requests.get()

3. 自定义函数 - 我们自己编写的函数
   注意：自定义函数和第三方函数是相对概念
"""

# ==================== 错误示例：没有文档的函数 ====================
def bad_function(a, b, c, d):
    """这是一个没有清晰文档的函数示例"""
    return a + b - c * d

# 问题：
# 1. 不知道函数功能
# 2. 不知道参数含义和类型
# 3. 不知道返回值含义
# 4. 增加使用难度

# ==================== 正确示例：带有完整文档的函数 ====================
def calculate_sum_and_diff(a, b=1):
    """
    计算两个数值的和以及差
    
    这个函数演示了如何编写规范的函数文档字符串。
    
    Parameters:
    -----------
    a : int or float
        数值1，必需参数，用于计算的第一个数值
    b : int or float, optional
        数值2，可选参数，用于计算的第二个数值，默认值为1
        
    Returns:
    --------
    tuple
        返回计算结果的元组 (和, 差)
        - 第一个元素：a + b (和)
        - 第二个元素：a - b (差)
        
    Examples:
    ---------
    >>> calculate_sum_and_diff(5, 3)
    (8, 2)
    >>> calculate_sum_and_diff(10)
    (11, 9)
    """
    sum_result = a + b
    diff_result = a - b
    return (sum_result, diff_result)

# ==================== 函数文档编写规范 ====================
"""
函数文档应包含以下要素：

1. 功能描述：函数的作用和目的
2. 参数说明：
   - 参数名称和含义
   - 数据类型
   - 是否可选
   - 默认值
3. 返回值说明：
   - 返回值含义
   - 返回值类型
   - 返回值结构
4. 使用示例（可选但推荐）
"""

# ==================== 更多文档示例 ====================
def process_user_data(name, age, email=None, active=True):
    """
    处理用户数据并格式化输出
    
    Parameters:
    -----------
    name : str
        用户姓名，必需参数
    age : int
        用户年龄，必需参数，应大于0
    email : str, optional
        用户邮箱，可选参数，默认为None
    active : bool, optional
        用户状态，可选参数，默认为True
        
    Returns:
    --------
    dict
        格式化后的用户信息字典，包含以下键值：
        - 'name': 用户姓名
        - 'age': 用户年龄
        - 'email': 用户邮箱
        - 'status': '活跃' 或 '非活跃'
        
    Raises:
    -------
    ValueError
        当age小于等于0时抛出异常
        
    Examples:
    ---------
    >>> process_user_data("张三", 25)
    {'name': '张三', 'age': 25, 'email': None, 'status': '活跃'}
    
    >>> process_user_data("李四", 30, "lisi@example.com", False)
    {'name': '李四', 'age': 30, 'email': 'lisi@example.com', 'status': '非活跃'}
    """
    if age <= 0:
        raise ValueError("年龄必须大于0")
    
    return {
        'name': name,
        'age': age,
        'email': email,
        'status': '活跃' if active else '非活跃'
    }

# ==================== 查看函数文档的方法 ====================
def demo_help_function():
    """演示如何查看函数文档"""
    print("=" * 50)
    print("查看函数文档的方法：")
    print("=" * 50)
    
    # 方法1：使用help()函数
    print("1. 使用help()函数：")
    print("help(calculate_sum_and_diff)")
    print()
    
    # 方法2：直接访问__doc__属性
    print("2. 直接访问__doc__属性：")
    print("calculate_sum_and_diff.__doc__")
    print()
    
    # 方法3：在IDE中查看（按Ctrl+点击函数名）
    print("3. 在IDE中按Ctrl+点击函数名查看")

# ==================== 实际演示 ====================
if __name__ == "__main__":
    print("Python函数文档字符串演示")
    print("=" * 50)
    
    # 演示函数调用
    result1 = calculate_sum_and_diff(10, 3)
    print(f"calculate_sum_and_diff(10, 3) = {result1}")
    
    result2 = calculate_sum_and_diff(5)
    print(f"calculate_sum_and_diff(5) = {result2}")
    
    # 演示用户数据处理
    user1 = process_user_data("张三", 25)
    print(f"用户数据1: {user1}")
    
    user2 = process_user_data("李四", 30, "lisi@example.com", False)
    print(f"用户数据2: {user2}")
    
    print("\n" + "=" * 50)
    print("查看函数文档：")
    print("在Python交互环境中输入：help(calculate_sum_and_diff)")
    
    # 展示如何查看文档
    demo_help_function()
    
    print("\n" + "=" * 50)
    print("重点总结：")
    print("1. 编写第三方函数时必须添加文档字符串")
    print("2. 文档应包含功能、参数、返回值的详细说明")
    print("3. 使用help()函数可以查看任何函数的文档")
    print("4. 良好的文档能大大提高代码的可读性和可维护性")

# ==================== 补充：查看内建函数文档示例 ====================
"""
查看内建函数文档的示例：

在Python交互环境中尝试：
>>> help(len)
>>> help(print)
>>> help(str.split)

这些都会显示详细的函数文档说明。
"""
