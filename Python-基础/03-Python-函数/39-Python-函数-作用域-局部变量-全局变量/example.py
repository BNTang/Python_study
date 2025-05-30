# -*- coding: utf-8 -*-

# @Time    : 2025-5-30
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 39-Python-函数-作用域-局部变量-全局变量

# =============================================================================
# 变量作用域：局部变量与全局变量
# =============================================================================

# 推荐的全局变量命名规范：使用 g_ 前缀
g_global_var = 999
g_name = "全局变量"

print("=" * 60)
print("1. 局部变量演示")
print("=" * 60)

def test_local():
    """演示局部变量的特性"""
    # 局部变量：定义在函数体内部，只能在函数内部访问
    local_var = 1
    print(f"函数内部访问局部变量: {local_var}")
    
    # 可以修改局部变量
    local_var = 2
    print(f"修改后的局部变量: {local_var}")
    
    # 查看当前函数的局部变量
    print(f"局部变量列表: {locals()}")

test_local()

# 尝试在函数外访问局部变量（会报错）
try:
    print(local_var)  # NameError: name 'local_var' is not defined
except NameError as e:
    print(f"错误：{e}")

print("\n" + "=" * 60)
print("2. 变量查找顺序 LEGB 规则演示")
print("=" * 60)

def outer_function():
    """外层函数 - E (Enclosing) 作用域"""
    outer_var = "外层函数变量"
    
    def inner_function():
        """内层函数 - L (Local) 作用域"""
        # LEGB 查找顺序：Local → Enclosing → Global → Built-in
        print(f"内层函数访问外层变量: {outer_var}")
        print(f"内层函数访问全局变量: {g_global_var}")
        
        # 局部变量会屏蔽同名的外层变量
        outer_var = "内层函数的局部变量"
        print(f"内层函数的局部变量: {outer_var}")
    
    inner_function()
    print(f"外层函数的变量未被影响: {outer_var}")

outer_function()

print("\n" + "=" * 60)
print("3. 全局变量演示")
print("=" * 60)

def test_global_access():
    """演示全局变量的访问"""
    # 可以直接访问全局变量
    print(f"函数内访问全局变量: {g_global_var}")
    print(f"函数内访问全局变量: {g_name}")

test_global_access()

def test_global_modify_wrong():
    """错误的全局变量修改方式"""
    print(f"修改前全局变量: {g_global_var}")
    
    # 这样做会创建一个新的局部变量，而不是修改全局变量
    g_global_var = 100
    print(f"函数内的局部变量: {g_global_var}")

print(f"修改前全局变量值: {g_global_var}")
test_global_modify_wrong()
print(f"全局变量值未改变: {g_global_var}")

def test_global_modify_correct():
    """正确的全局变量修改方式"""
    global g_global_var  # 声明要修改全局变量
    
    print(f"修改前: {g_global_var}")
    g_global_var = 666
    print(f"修改后: {g_global_var}")

print(f"\n使用 global 关键字修改全局变量:")
test_global_modify_correct()
print(f"全局变量已被修改: {g_global_var}")

print("\n" + "=" * 60)
print("4. nonlocal 关键字演示")
print("=" * 60)

def outer_with_nonlocal():
    """演示 nonlocal 关键字的使用"""
    outer_var = "原始值"
    
    def inner_modify():
        nonlocal outer_var  # 声明要修改外层函数的变量
        outer_var = "被内层函数修改"
        print(f"内层函数修改外层变量: {outer_var}")
    
    print(f"修改前: {outer_var}")
    inner_modify()
    print(f"修改后: {outer_var}")

outer_with_nonlocal()

print("\n" + "=" * 60)
print("5. 变量查看函数演示")
print("=" * 60)

def demo_variables():
    """演示 locals() 和 globals() 函数"""
    local_a = 10
    local_b = 20
    
    print("局部变量:")
    for name, value in locals().items():
        print(f"  {name} = {value}")
    
    print("\n部分全局变量:")
    global_vars = {k: v for k, v in globals().items() 
                   if k.startswith('g_') or k in ['__name__', '__file__']}
    for name, value in global_vars.items():
        print(f"  {name} = {value}")

demo_variables()

print("\n" + "=" * 60)
print("6. 常见陷阱和最佳实践")
print("=" * 60)

# 陷阱1：变量定义的时机问题
def early_call():
    """在变量定义前调用函数"""
    print(f"early_var = {early_var}")

# early_call()  # 会报错，因为 early_var 还未定义
early_var = "现在定义了"
early_call()  # 现在可以正常调用

# 陷阱2：就近原则
def scope_trap():
    """演示变量访问的就近原则"""
    print(f"访问全局变量: {g_name}")
    
    # 如果在函数中定义同名变量，会屏蔽全局变量
    g_name = "局部变量"
    print(f"访问局部变量: {g_name}")

print(f"全局变量值: {g_name}")
scope_trap()
print(f"全局变量值未变: {g_name}")

print("\n" + "=" * 60)
print("7. 最佳实践总结")
print("=" * 60)

print("""
变量作用域最佳实践：

1. 命名规范：
   - 全局变量使用 g_ 前缀
   - 局部变量使用清晰的名称

2. 变量定义：
   - 全局变量定义在文件顶部
   - 避免在函数中修改全局变量
   - 必要时使用 global 关键字

3. 作用域规则：
   - LEGB 查找顺序：Local → Enclosing → Global → Built-in
   - 就近原则：优先访问最近作用域的变量
   - 使用 nonlocal 修改外层函数变量

4. 调试技巧：
   - 使用 locals() 查看局部变量
   - 使用 globals() 查看全局变量
   - 注意变量的生命周期和访问时机
""")
