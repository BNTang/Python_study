# -*- coding: utf-8 -*-

# @Time    : 2025-5-29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 22-Python-函数-装饰器-案例-3

"""
装饰器案例：给发说说和发图片功能添加登录验证

需求：在发说说和发图片之前增加登录验证操作

三种实现方式对比：
方式一：直接在业务代码中修改（不推荐 - 代码冗余、维护困难）
方式二：在功能函数中添加验证（改进 - 代码复用性更好）  
方式三：使用装饰器（最佳 - 代码解耦、可维护性强）
"""

# ==================== 公共函数 ====================
def check_login():
    """登录验证功能"""
    print("登录验证")

# ==================== 方式一：直接在业务代码中修改（不推荐）====================
print("=" * 50)
print("方式一：直接在业务代码中修改（不推荐）")
print("缺点：代码冗余度高，使用价值差，维护困难")

def post_message_v1():
    """发说说功能 - 方式一"""
    print("发说说")

def post_image_v1():
    """发图片功能 - 方式一"""
    print("发图片")

# 业务逻辑代码 - 方式一（需要在每个地方都添加验证）
def business_logic_v1():
    choice = input("请选择操作 (1-发说说, 2-发图片): ")
    
    if choice == "1":
        check_login()  # 每个地方都要添加验证
        post_message_v1()
    elif choice == "2":
        check_login()  # 每个地方都要添加验证  
        post_image_v1()

# ==================== 方式二：在功能函数中添加验证（改进）====================
print("=" * 50)
print("方式二：在功能函数中添加验证（改进）")
print("优点：代码复用性好，只需修改一个地方")
print("缺点：功能函数和验证逻辑耦合")

def post_message_v2():
    """发说说功能 - 方式二：在功能函数中添加验证"""
    check_login()  # 在功能函数中添加验证
    print("发说说")

def post_image_v2():
    """发图片功能 - 方式二：在功能函数中添加验证"""
    check_login()  # 在功能函数中添加验证
    print("发图片")

# 业务逻辑代码 - 方式二（业务代码简洁）
def business_logic_v2():
    choice = input("请选择操作 (1-发说说, 2-发图片): ")
    
    if choice == "1":
        post_message_v2()  # 直接调用，验证已内置
    elif choice == "2":
        post_image_v2()    # 直接调用，验证已内置

# ==================== 方式三：使用装饰器（最佳实践）====================
print("=" * 50)
print("方式三：使用装饰器（最佳实践）")
print("优点：代码解耦、可维护性强、可重用性高")

def login_required(func):
    """登录验证装饰器"""
    def wrapper(*args, **kwargs):
        check_login()  # 执行验证
        return func(*args, **kwargs)  # 执行原函数
    return wrapper

@login_required
def post_message_v3():
    """发说说功能 - 方式三：使用装饰器"""
    print("发说说")

@login_required  
def post_image_v3():
    """发图片功能 - 方式三：使用装饰器"""
    print("发图片")

@login_required
def post_video():
    """发视频功能 - 新增功能，自动具备验证能力"""
    print("发视频")

# 业务逻辑代码 - 方式三（最简洁）
def business_logic_v3():
    choice = input("请选择操作 (1-发说说, 2-发图片, 3-发视频): ")
    
    if choice == "1":
        post_message_v3()  # 自动带验证
    elif choice == "2":
        post_image_v3()    # 自动带验证
    elif choice == "3":
        post_video()       # 自动带验证

# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("\n🔥 重点学习内容：")
    print("1. 装饰器解决了代码冗余和耦合问题")
    print("2. @装饰器语法让代码更简洁优雅") 
    print("3. 装饰器可以给任意函数添加相同功能")
    print("4. 遵循开闭原则：对扩展开放，对修改封闭")
    
    print("\n演示装饰器效果：")
    print("-" * 30)
    
    # 演示方式三的效果
    print("测试发说说：")
    post_message_v3()
    
    print("\n测试发图片：")  
    post_image_v3()
    
    print("\n测试发视频：")
    post_video()
    
    print("\n💡 学习要点：")
    print("装饰器 = 高阶函数 + 闭包 + 语法糖")
    print("核心思想：在不修改原函数的前提下，为函数添加新功能")
