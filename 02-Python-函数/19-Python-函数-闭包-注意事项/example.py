# -*- coding: utf-8 -*-

# @Time    : 2025-5-28
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 19-Python-函数-闭包-注意事项

print("=" * 60)
print("🔥 Python闭包注意事项 - 重要知识点")
print("=" * 60)

# ============================================================================
# 📌 注意事项1: 修改外部变量必须使用 nonlocal 关键字
# ============================================================================
print("\n【注意事项1】修改外部变量必须使用 nonlocal")
print("-" * 40)

def test():
    number = 10
    
    def test2():
        # ❌ 错误做法：直接赋值会创建新的局部变量
        # number = 666  # 这样写会创建新变量，不会修改外部变量
        
        # ✅ 正确做法：使用 nonlocal 声明
        nonlocal number  # 声明要修改外部的 number 变量
        print(f"修改前的number: {number}")
        number = 666     # 现在可以修改外部变量了
        print(f"修改后的number: {number}")
    
    return test2

print("🔍 测试 nonlocal 的使用:")
result = test()
result()

# ============================================================================
# 📌 注意事项2: 闭包中变量的延迟绑定问题
# ============================================================================
print("\n【注意事项2】闭包中变量的延迟绑定问题")
print("-" * 40)

print("❌ 错误示例 - 所有函数都引用同一个变量:")

def test_wrong():
    """错误示例：所有闭包函数都会打印相同的值"""
    funcs = []
    
    for i in range(1, 4):  # i = 1, 2, 3
        def inner():
            print(f"打印 i 的值: {i}")  # 所有函数都引用同一个 i
        funcs.append(inner)
    
    return funcs

# 测试错误示例
wrong_funcs = test_wrong()
print("执行结果（都是3，因为循环结束后 i=3）:")
for func in wrong_funcs:
    func()

print("\n" + "="*50)
print("✅ 正确示例 - 每个函数保存不同的值:")

def test_correct():
    """正确示例：通过参数传递保存当前值"""
    funcs = []
    
    for i in range(1, 4):
        def outer(num):  # 通过参数接收当前的 i 值
            def inner():
                print(f"打印保存的值: {num}")  # 使用参数中保存的值
            return inner
        
        funcs.append(outer(i))  # 立即调用 outer，传入当前的 i 值
    
    return funcs

# 测试正确示例
correct_funcs = test_correct()
print("执行结果（分别是1、2、3）:")
for func in correct_funcs:
    func()

# ============================================================================
# 📚 核心知识点总结
# ============================================================================
print("\n" + "="*60)
print("📚 核心知识点总结")
print("="*60)

print("""
🎯 闭包的两大注意事项：

1️⃣ 修改外部变量：
   ❌ 直接赋值 → 创建新的局部变量
   ✅ 使用 nonlocal → 修改外部变量

2️⃣ 变量延迟绑定：
   ❌ 循环中直接引用变量 → 所有闭包共享最终值
   ✅ 通过参数传递 → 每个闭包保存独立值

💡 记忆要点：
   - 函数定义时不确定变量值，只有调用时才确定
   - nonlocal 声明"我要修改外部变量"
   - 参数传递可以"冻结"当前变量值
""")

print("="*60)
print("🎉 学习完成！重点已标注，建议多练习加深理解")
print("="*60)
