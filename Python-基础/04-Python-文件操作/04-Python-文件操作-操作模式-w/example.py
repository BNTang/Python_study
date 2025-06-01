# -*- coding: utf-8 -*-

# @Time    : 2025-06-01
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 04-Python-文件操作-操作模式-w

"""
Python文件操作 - w模式详解

w模式的三个重要特性：
1. 如果文件不存在，则会自动创建一个新文件
2. 以只写的方式打开文件（只能写，不能读）
3. 文件指针将放在文件的开头（会覆盖原有内容）
"""

print("=== Python文件操作 - w模式演示 ===\n")

# =====================================================
# 特性1：文件不存在时自动创建
# =====================================================
print("1. 测试文件不存在时的行为")
print("-" * 30)

# 尝试打开一个不存在的文件（确保先删除该文件进行测试）
try:
    with open("test_new_file.txt", "w", encoding="utf-8") as file:
        print("✓ 文件成功创建并打开")
        file.write("这是新创建的文件")
        print("✓ 内容写入成功")
except Exception as e:
    print(f"✗ 错误: {e}")

print()

# =====================================================
# 特性2：只写模式（不能读取）
# =====================================================
print("2. 测试w模式的只写特性")
print("-" * 30)

# 先写入一些内容
with open("test_write_only.txt", "w", encoding="utf-8") as file:
    file.write("123456")
    print("✓ 写入操作成功")

# 尝试在w模式下读取（会报错）
print("尝试在w模式下读取文件...")
try:
    with open("test_write_only.txt", "w", encoding="utf-8") as file:
        content = file.read()  # 这里会报错
        print(f"读取内容: {content}")
except Exception as e:
    print(f"✗ 读取失败: {e}")
    print("✓ 证明w模式确实不支持读取操作")

print()

# =====================================================
# 特性3：文件指针在开头（覆盖原内容）
# =====================================================
print("3. 测试文件指针位置和内容覆盖")
print("-" * 30)

# 先创建一个包含内容的文件
with open("test_overwrite.txt", "w", encoding="utf-8") as file:
    file.write("ABCDEFG")
    print("✓ 原始内容写入: ABCDEFG")

# 读取并显示原始内容
with open("test_overwrite.txt", "r", encoding="utf-8") as file:
    original_content = file.read()
    print(f"✓ 原始文件内容: {original_content}")

# 再次以w模式打开，写入新内容
with open("test_overwrite.txt", "w", encoding="utf-8") as file:
    file.write("123456")
    print("✓ 新内容写入: 123456")

# 读取最终内容
with open("test_overwrite.txt", "r", encoding="utf-8") as file:
    final_content = file.read()
    print(f"✓ 最终文件内容: {final_content}")
    print("✓ 原内容被完全覆盖")

print()

# =====================================================
# w模式总结
# =====================================================
print("=== w模式特性总结 ===")
print("1. 文件不存在 → 自动创建新文件")
print("2. 访问权限 → 只写（write-only）")
print("3. 文件指针 → 位于文件开头")
print("4. 内容处理 → 覆盖原有内容")
print("\n注意：w模式会清空文件原有内容！")

# =====================================================
# 实际应用示例
# =====================================================
print("\n=== 实际应用示例 ===")

# 创建配置文件
config_data = """# 应用配置文件
app_name = MyApp
version = 1.0.0
debug = True
"""

with open("app_config.txt", "w", encoding="utf-8") as config_file:
    config_file.write(config_data)
    print("✓ 配置文件创建成功")

# 生成日志文件
import datetime
log_entry = f"[{datetime.datetime.now()}] 应用启动\n"

with open("app_log.txt", "w", encoding="utf-8") as log_file:
    log_file.write(log_entry)
    print("✓ 日志文件创建成功")

print("\n学习要点：")
print("• w模式适合创建新文件或完全重写文件")
print("• 使用w模式前要确认是否需要保留原有内容")
print("• 如需追加内容，应使用a模式")
print("• 如需读写，应使用r+或w+模式")
