# -*- coding: utf-8 -*-

# @Time    : 2025-5-29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 21-Python-函数-装饰器-案例-2

"""
装饰器案例：功能函数与业务逻辑分离

重点学习内容：
1. 功能函数与业务逻辑分离的好处
2. 第一种方式的问题：代码冗余、维护性差
3. 装饰器的优势：代码复用性高、维护性好
"""

# ==================== 基础功能函数 ====================
def send_message():
    """发说说功能"""
    print("正在发送说说...")
    print("说说发送成功！")

def send_picture():
    """发图片功能"""
    print("正在发送图片...")
    print("图片发送成功！")

# ==================== 第一种方式：在业务逻辑中直接添加验证 ====================
print("=" * 50)
print("第一种方式演示（不推荐）：")
print("=" * 50)

def login_verify():
    """登录验证"""
    print("正在进行登录验证...")
    return True  # 假设验证通过

def business_logic_v1():
    """业务逻辑代码 - 第一种方式"""
    print("请选择功能：")
    print("1. 发说说")
    print("2. 发图片")
    
    choice = input("请输入选择(1或2): ")
    
    if choice == "1":
        # 问题：每次调用前都要手动添加登录验证
        login_verify()
        send_message()
    elif choice == "2":
        # 问题：重复的登录验证代码
        login_verify()
        send_picture()
    else:
        print("无效选择！")

# 第一种方式的问题分析
print("\n第一种方式的问题：")
print("1. 代码冗余度大 - 每个功能前都要写登录验证")
print("2. 复用性差 - 登录验证代码重复编写")
print("3. 维护性差 - 修改验证逻辑需要改多处")
print("4. 业务逻辑代码多时，修改工作量巨大")

# ==================== 第二种方式：使用装饰器 ====================
print("\n" + "=" * 50)
print("第二种方式演示（推荐）：使用装饰器")
print("=" * 50)

def login_required(func):
    """登录验证装饰器"""
    def wrapper(*args, **kwargs):
        print("正在进行登录验证...")
        # 这里可以添加实际的登录验证逻辑
        user_logged_in = True  # 假设验证通过
        
        if user_logged_in:
            print("登录验证通过！")
            return func(*args, **kwargs)
        else:
            print("登录验证失败，请先登录！")
            return None
    return wrapper

# 使用装饰器改造功能函数
@login_required
def send_message_v2():
    """发说说功能 - 带登录验证"""
    print("正在发送说说...")
    print("说说发送成功！")

@login_required
def send_picture_v2():
    """发图片功能 - 带登录验证"""
    print("正在发送图片...")
    print("图片发送成功！")

def business_logic_v2():
    """业务逻辑代码 - 第二种方式"""
    print("请选择功能：")
    print("1. 发说说")
    print("2. 发图片")
    
    choice = input("请输入选择(1或2): ")
    
    if choice == "1":
        # 优势：直接调用，登录验证自动执行
        send_message_v2()
    elif choice == "2":
        # 优势：代码简洁，无重复验证代码
        send_picture_v2()
    else:
        print("无效选择！")

# ==================== 对比演示 ====================
def demo_comparison():
    """对比演示两种方式"""
    print("\n" + "=" * 50)
    print("对比演示")
    print("=" * 50)
    
    print("\n--- 第一种方式运行 ---")
    # 模拟第一种方式
    login_verify()
    send_message()
    
    print("\n--- 第二种方式运行 ---")
    # 装饰器方式
    send_message_v2()

# ==================== 装饰器的优势总结 ====================
def advantages_summary():
    """装饰器优势总结"""
    print("\n" + "=" * 50)
    print("装饰器方式的优势：")
    print("=" * 50)
    print("1. 代码复用性高：")
    print("   - 登录验证逻辑只需要写一次")
    print("   - 通过@装饰器语法轻松应用到任何函数")
    
    print("\n2. 维护性好：")
    print("   - 修改验证逻辑只需要修改装饰器函数")
    print("   - 所有使用该装饰器的函数自动更新")
    
    print("\n3. 代码简洁：")
    print("   - 业务逻辑代码更清晰")
    print("   - 功能职责分离明确")
    
    print("\n4. 扩展性强：")
    print("   - 可以轻松添加多个装饰器")
    print("   - 可以创建不同类型的验证装饰器")

# ==================== 多界面复用演示 ====================
def multi_interface_demo():
    """多界面复用演示"""
    print("\n" + "=" * 50)
    print("多界面复用演示：")
    print("=" * 50)
    
    # 界面A
    def interface_a():
        print("界面A - 社交功能")
        send_message_v2()
        send_picture_v2()
    
    # 界面B
    def interface_b():
        print("界面B - 媒体分享")
        send_picture_v2()
        send_message_v2()
    
    # 界面C
    def interface_c():
        print("界面C - 快捷操作")
        send_message_v2()
    
    print("相同的功能函数可以在不同界面中复用：")
    interface_a()
    print("\n" + "-" * 30)
    interface_b()
    print("\n" + "-" * 30)
    interface_c()

# ==================== 主程序运行 ====================
if __name__ == "__main__":
    print("Python装饰器案例学习")
    print("=" * 50)
    
    # 运行对比演示
    demo_comparison()
    
    # 显示优势总结
    advantages_summary()
    
    # 多界面复用演示
    multi_interface_demo()
    
    print("\n" + "=" * 50)
    print("学习要点总结：")
    print("1. 功能函数与业务逻辑要分离")
    print("2. 装饰器是实现横切关注点的最佳方式")
    print("3. @语法让代码更简洁易读")
    print("4. 装饰器提高了代码的复用性和维护性")
    print("=" * 50)
    
    # 交互式演示（可选）
    print("\n是否要运行交互式演示？(y/n): ", end="")
    if input().lower() == 'y':
        business_logic_v2()
