# -*- coding: utf-8 -*-

# @Time    : 2025-5-29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 23-Python-函数-装饰器-案例-4

"""
装饰器案例演示：
1. 开放封闭原则：已写好的代码尽可能不修改，新增功能通过扩展实现
2. 单一职责原则：一个函数只做一件事情
3. 装饰器模式：在不修改原函数的情况下，为函数添加额外功能
"""

print("=" * 50)
print("装饰器案例演示")
print("=" * 50)

# ==================== 第一阶段：基础功能函数 ====================
print("\n【第一阶段】基础功能函数")

def post_status():
    """发说说功能"""
    print("发说说")

def post_image():
    """发图片功能"""
    print("发图片")

print("原始功能测试：")
post_status()
post_image()

# ==================== 第二阶段：直接修改函数体（问题代码） ====================
print("\n【第二阶段】直接修改函数体 - 违反开放封闭原则和单一职责原则")

def post_status_v2():
    """发说说功能 - 添加了登录验证（问题：违反单一职责原则）"""
    print("登录验证")  # 额外添加的功能
    print("发说说")    # 原有功能

def post_image_v2():
    """发图片功能 - 添加了登录验证（问题：违反单一职责原则）"""
    print("登录验证")  # 额外添加的功能
    print("发图片")    # 原有功能

print("问题代码演示：")
print("问题1：违反单一职责原则 - 函数既要做原本的事，又要做验证")
print("问题2：违反开放封闭原则 - 修改了已有的函数体")
print("问题3：代码重复 - 每个函数都要添加相同的验证代码")
post_status_v2()
post_image_v2()

# ==================== 第三阶段：提取验证函数（仍有问题） ====================
print("\n【第三阶段】提取验证函数 - 仍需修改业务代码")

def login_check(func):
    """登录验证函数"""
    print("登录验证")
    func()  # 执行传入的函数

def login_check_status():
    """发说说前验证"""
    login_check(post_status)

def login_check_image():
    """发图片前验证"""
    login_check(post_image)

print("改进1：提取了公共验证逻辑")
print("问题：业务代码需要修改调用方式")
login_check_status()
login_check_image()

# ==================== 第四阶段：使用闭包实现装饰器 ====================
print("\n【第四阶段】使用闭包实现装饰器模式")

def decorator_login_check(func):
    """装饰器：为函数添加登录验证功能
    
    Args:
        func: 需要装饰的函数
        
    Returns:
        wrapper: 包装后的新函数
    """
    def wrapper():
        """内部包装函数"""
        print("登录验证")  # 添加的新功能
        func()            # 执行原函数
    return wrapper       # 返回包装后的函数

# 重新指向装饰后的函数
post_status = decorator_login_check(post_status)
post_image = decorator_login_check(post_image)

print("装饰器模式优势：")
print("1. 不修改原函数体")
print("2. 不修改业务调用代码")
print("3. 通过闭包动态添加功能")

# 模拟业务逻辑
s = 1
if s == 1:
    print("业务代码调用 - 发说说：")
    post_status()
else:
    print("业务代码调用 - 发图片：")
    post_image()

# ==================== 第五阶段：Python语法糖 ====================
print("\n【第五阶段】Python装饰器语法糖")

def auth_decorator(func):
    """认证装饰器 - 使用语法糖形式"""
    def wrapper():
        print("🔐 权限验证")
        func()
    return wrapper

@auth_decorator
def share_moment():
    """分享动态"""
    print("📝 分享动态")

@auth_decorator  
def upload_photo():
    """上传照片"""
    print("📷 上传照片")

print("语法糖形式装饰器：")
print("@auth_decorator 等价于 share_moment = auth_decorator(share_moment)")

share_moment()
upload_photo()

# ==================== 第六阶段：带参数的装饰器 ====================
print("\n【第六阶段】带参数的装饰器")

def permission_required(permission):
    """需要特定权限的装饰器工厂
    
    Args:
        permission: 需要的权限类型
        
    Returns:
        decorator: 实际的装饰器函数
    """
    def decorator(func):
        def wrapper():
            print(f"🔒 检查{permission}权限")
            print(f"✅ {permission}权限验证通过")
            func()
        return wrapper
    return decorator

@permission_required("管理员")
def delete_post():
    """删除帖子"""
    print("🗑️ 删除帖子")

@permission_required("用户")
def like_post():
    """点赞帖子"""
    print("👍 点赞帖子")

print("带参数的装饰器演示：")
delete_post()
like_post()

# ==================== 第七阶段：装饰器最佳实践 ====================
print("\n【第七阶段】装饰器最佳实践")

import functools

def advanced_decorator(func):
    """高级装饰器 - 保留原函数信息"""
    @functools.wraps(func)  # 保留原函数的元数据
    def wrapper(*args, **kwargs):
        """支持任意参数的包装器"""
        print(f"🚀 执行前置操作: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✨ 执行后置操作: {func.__name__}")
        return result
    return wrapper

@advanced_decorator
def send_message(message, user="匿名"):
    """发送消息
    
    Args:
        message: 消息内容
        user: 用户名
        
    Returns:
        bool: 发送是否成功
    """
    print(f"📧 {user}发送消息: {message}")
    return True

print("高级装饰器特性：")
print("1. 支持任意参数")
print("2. 保留原函数元数据") 
print("3. 支持返回值")
print(f"函数名: {send_message.__name__}")
print(f"函数文档: {send_message.__doc__}")

result = send_message("Hello World!", user="Alice")
print(f"返回值: {result}")

# ==================== 总结 ====================
print("\n" + "=" * 50)
print("装饰器核心概念总结")
print("=" * 50)
print("""
🎯 装饰器的本质：
   - 是一个接受函数作为参数并返回函数的函数
   - 利用Python的闭包特性实现
   - 在不修改原函数的前提下扩展功能

📚 设计原则：
   1. 开放封闭原则：对扩展开放，对修改封闭
   2. 单一职责原则：一个函数只做一件事

🔧 装饰器类型：
   1. 简单装饰器：@decorator
   2. 带参数装饰器：@decorator(args)
   3. 类装饰器：使用类实现装饰器
   4. 多层装饰器：@decorator1 @decorator2

💡 应用场景：
   - 权限验证、日志记录、性能监控
   - 缓存、重试机制、参数校验
   - AOP（面向切面编程）

⚠️ 注意事项：
   - 使用functools.wraps保留原函数信息
   - 考虑装饰器的执行顺序
   - 避免过度使用造成代码难以理解
""")
