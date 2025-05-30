# -*- coding: utf-8 -*-

# @Time    : 2025-5-29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 24-Python-函数-装饰器-案例-5 - 装饰器执行时间演示

"""
装饰器学习重点：
1. 装饰器的执行时间是立即执行（定义时执行，不是调用时）
2. 保证函数名不变
3. 保证函数体内部代码不变
4. 增加额外功能
"""

print("=== 装饰器执行时间演示 ===")


# 定义装饰器函数
def check(func):
    """
    登录验证装饰器
    重点：这个函数在装饰器应用时立即执行
    """
    print("XXX - 装饰器check函数被执行了！")  # 证明装饰器立即执行
    
    def inner():
        """
        内部包装函数
        重点：这个函数在被装饰的函数调用时才执行
        """
        print("登录验证操作")  # 额外功能
        func()  # 执行原函数
    
    return inner

# 原始函数
def fa_shuo_shuo():
    """发说说函数 - 原始业务逻辑"""
    print("发说说")

print("\n=== 方法1：手动装饰器 ===")
# 手动应用装饰器（等同于 @check）
fa_shuo_shuo = check(fa_shuo_shuo)
print("装饰器已应用，但函数还未调用")

print("\n现在调用装饰后的函数：")
fa_shuo_shuo()

print("\n=== 方法2：@语法糖装饰器 ===")

# 使用@语法糖的装饰器
@check
def fa_tu_pian():
    """发图片函数"""
    print("发图片")

print("@装饰器已应用（注意上面的XXX已经打印）")
print("现在调用装饰后的函数：")
fa_tu_pian()

print("\n=== 装饰器优势总结 ===")
print("✓ 函数名未改变：fa_shuo_shuo, fa_tu_pian")
print("✓ 函数体未改变：只有print语句")
print("✓ 增加了额外功能：登录验证操作")
print("✓ 装饰器在定义时执行，被装饰函数在调用时执行")

# 验证函数名确实没有改变
print(f"\n函数名验证：{fa_shuo_shuo.__name__}")  # 注意：这里显示的是inner，实际开发中可以用functools.wraps解决
