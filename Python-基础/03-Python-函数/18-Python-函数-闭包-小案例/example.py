# -*- coding: utf-8 -*-

# @Time    : 2025-5-28
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 18-Python-函数-闭包-小案例

"""
闭包的应用场景案例：根据不同配置信息生成不同的分割线函数

闭包的标准格式：
1. 外部函数接收参数
2. 内部函数使用外部函数的变量/参数
3. 外部函数返回内部函数
4. 内部函数及其引用的外部环境构成闭包
"""

def line_configure(content, length):
    """
    外部函数：配置分割线参数
    
    Args:
        content (str): 分割线中间显示的内容
        length (int): 分割线总长度
        
    Returns:
        function: 返回生成分割线的内部函数（闭包）
    """
    
    def line():
        """
        内部函数：生成分割线
        使用外部函数的 content 和 length 参数
        """
        # 计算两边分割线的长度（总长度减去内容长度再除以2）
        side_length = (length - len(content)) // 2
        
        # 生成完整的分割线：左边 + 内容 + 右边
        separator = "-" * side_length + content + "-" * side_length
        
        print(separator)
    
    # 返回内部函数，形成闭包
    return line


# ========== 使用示例 ==========

print("=== 闭包应用案例：生成不同样式的分割线函数 ===\n")

# 1. 创建第一个分割线函数：内容为"闭包"，长度为20
print("1. 创建分割线函数1：内容='闭包'，长度=20")
line1 = line_configure("闭包", 20)
print("调用line1()三次：")
line1()
line1()
line1()

print()

# 2. 创建第二个分割线函数：内容为"XXX"，长度为80
print("2. 创建分割线函数2：内容='XXX'，长度=80")
line2 = line_configure("XXX", 80)
print("调用line2()两次：")
line2()
line2()

print()

# 3. 创建第三个分割线函数：内容为"Python学习"，长度为50
print("3. 创建分割线函数3：内容='Python学习'，长度=50")
line3 = line_configure("Python学习", 50)
print("调用line3()一次：")
line3()

print()

# ========== 闭包的优势说明 ==========
print("=== 闭包的优势 ===")
print("1. 避免重复传参：不用每次调用都传递相同的配置参数")
print("2. 代码复用：可以生成多个不同配置的函数")
print("3. 数据封装：配置信息被封装在闭包中，外部无法直接访问")
print("4. 函数工厂：根据不同参数生成不同功能的函数")

print("\n=== 对比普通函数调用 ===")
def normal_line(content, length):
    """普通函数：每次都需要传递参数"""
    side_length = (length - len(content)) // 2
    separator = "-" * side_length + content + "-" * side_length
    print(separator)

print("普通函数调用（每次都要传参）：")
normal_line("闭包", 20)
normal_line("闭包", 20)
normal_line("闭包", 20)

print("\n闭包函数调用（配置一次，多次使用）：")
line1()
line1()
line1()
