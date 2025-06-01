# -*- coding: utf-8 -*-

# @Time    : 2025-06-01
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 07-Python-文件操作-操作模式-+组

"""
🔥 Python文件操作模式 - +组详解 🔥

+组模式特点：
1. 将单一模式改为读写模式
2. 保持原模式的其他特性不变
3. 总共6种组合：r+, w+, a+, rb+, wb+, ab+

重点对比：
- r+: 读写模式，文件必须存在，指针在开头，部分覆盖写入
- w+: 读写模式，清空文件内容，指针在开头，完全覆盖写入  
- a+: 读写模式，指针在末尾，只能追加写入
"""

import os

# 准备测试文件
def prepare_test_file(filename, content="123456789"):
    """准备测试文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 准备测试文件: {filename}, 内容: {content}")

def show_file_content(filename):
    """显示文件内容"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"📄 文件内容: {content}")
        return content
    except FileNotFoundError:
        print(f"❌ 文件不存在: {filename}")
        return None

print("=" * 60)
print("🚀 Python文件操作模式 +组 测试演示")
print("=" * 60)

# ========== r+ 模式详细测试 =========
print("\n🔍 r+ 模式测试 (读写模式，文件必须存在)")
print("-" * 40)

# 测试1: 文件不存在时的行为
print("📝 测试1: 文件不存在时r+模式的行为")
test_file = "test_r_plus.txt"
if os.path.exists(test_file):
    os.remove(test_file)

try:
    with open(test_file, 'r+', encoding='utf-8') as f:
        pass
except FileNotFoundError as e:
    print(f"❌ r+模式：文件不存在会报错 - {e}")

# 测试2: r+模式的读写功能
print("\n📝 测试2: r+模式的读写功能")
prepare_test_file(test_file, "ABCDEFG")

# 先读后写的情况
print("🔸 情况1: 先读后写")
with open(test_file, 'r+', encoding='utf-8') as f:
    # 读取内容
    content = f.read()
    print(f"读取到的内容: {content}")
    
    # 写入新内容(会追加到末尾)
    f.write("12345")
    print("写入内容: 12345")

show_file_content(test_file)

# 测试3: r+模式的覆盖写入
print("\n🔸 情况2: 直接写入(覆盖开头)")
prepare_test_file(test_file, "ABCDEFG")
show_file_content(test_file)

with open(test_file, 'r+', encoding='utf-8') as f:
    # 直接写入会从开头覆盖
    f.write("XYZ")
    print("从开头写入: XYZ")

show_file_content(test_file)
print("💡 重点: r+模式写入是部分覆盖，不会清空整个文件")

# ========== w+ 模式测试 =========
print("\n🔍 w+ 模式测试 (读写模式，清空原内容)")
print("-" * 40)

prepare_test_file(test_file, "ABCDEFG")
print("原文件内容:")
show_file_content(test_file)

with open(test_file, 'w+', encoding='utf-8') as f:
    # w+会清空文件
    print("使用w+模式打开...")
    
    # 写入内容
    f.write("NEW CONTENT")
    print("写入: NEW CONTENT")
    
    # 移动指针到开头进行读取
    f.seek(0)
    content = f.read()
    print(f"读取内容: {content}")

show_file_content(test_file)
print("💡 重点: w+模式会完全清空原文件内容")

# ========== a+ 模式测试 =========
print("\n🔍 a+ 模式测试 (读写模式，只能追加)")
print("-" * 40)

prepare_test_file(test_file, "HELLO")
print("原文件内容:")
show_file_content(test_file)

with open(test_file, 'a+', encoding='utf-8') as f:
    # 写入内容(追加到末尾)
    f.write(" WORLD")
    print("追加内容: WORLD")
    
    # 移动指针到开头读取
    f.seek(0)
    content = f.read()
    print(f"读取全部内容: {content}")

show_file_content(test_file)
print("💡 重点: a+模式只能在文件末尾追加，不能覆盖")

# ========== 二进制+组模式简要说明 =========
print("\n🔍 二进制+组模式 (rb+, wb+, ab+)")
print("-" * 40)
print("rb+ = r+ 的二进制版本")
print("wb+ = w+ 的二进制版本") 
print("ab+ = a+ 的二进制版本")
print("💡 重点: 二进制模式不需要指定encoding参数")

# 示例：rb+模式
prepare_test_file(test_file, "Binary Test")
with open(test_file, 'rb+') as f:
    content = f.read()
    print(f"rb+读取(字节): {content}")
    f.write(b" Added")
    print("rb+追加字节内容")

show_file_content(test_file)

# ========== 总结对比表 =========
print("\n📊 +组模式总结对比")
print("=" * 60)
print("模式  | 文件存在要求 | 指针位置 | 写入方式     | 读写能力")
print("-" * 60)
print("r+   | 必须存在     | 开头     | 部分覆盖     | 可读可写")
print("w+   | 可不存在     | 开头     | 完全覆盖     | 可读可写")
print("a+   | 可不存在     | 末尾     | 只能追加     | 可读可写")
print("rb+  | 必须存在     | 开头     | 部分覆盖     | 可读可写(二进制)")
print("wb+  | 可不存在     | 开头     | 完全覆盖     | 可读可写(二进制)")
print("ab+  | 可不存在     | 末尾     | 只能追加     | 可读可写(二进制)")
print("=" * 60)

print("\n🎯 学习要点:")
print("1. +号的作用：让单一模式变成读写模式")
print("2. 保持原模式特性：除了增加读写能力，其他特性不变")
print("3. 实际应用：根据需求选择合适的+组模式")
print("4. 注意指针位置：读写操作会影响指针位置")

# 清理测试文件
if os.path.exists(test_file):
    os.remove(test_file)
    print(f"\n🧹 清理测试文件: {test_file}")

print("\n✅ +组模式学习完成！")
