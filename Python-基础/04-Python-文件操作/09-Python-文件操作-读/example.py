# -*- coding: utf-8 -*-

# @Time    : 2025-06-03
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 09-Python-文件操作-读

# 首先创建一个测试文件用于演示
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('1\n2\n3\n4\n5')

print("=== Python文件读操作三大核心方法 ===\n")

# ============================================
# 方法一：read() - 读取指定字节数或全部内容
# ============================================
print("1. read() 方法演示：")
print("-" * 30)

# 基本用法：读取全部内容
f = open('test.txt', 'r', encoding='utf-8')
content = f.read()  # 不传参数，读取全部内容
print(f"读取全部内容: '{content}'")
f.close()

# 指定字节数读取
f = open('test.txt', 'r', encoding='utf-8')
content = f.read(2)  # 读取2个字符
print(f"读取2个字符: '{content}'")
print(f"当前指针位置: {f.tell()}")  # 显示指针位置
f.close()

# 文件指针定位后读取
f = open('test.txt', 'r', encoding='utf-8')
f.seek(2)  # 将指针移动到位置2
content = f.read(2)  # 从位置2开始读取2个字符
print(f"从位置2读取2个字符: '{content}'")
print(f"读取后指针位置: {f.tell()}")
f.close()

print()

# ============================================
# 方法二：readline() - 逐行读取
# ============================================
print("2. readline() 方法演示：")
print("-" * 30)

f = open('test.txt', 'r', encoding='utf-8')
print("逐行读取演示：")
line1 = f.readline()
print(f"第1行: '{line1.strip()}'")  # strip()去除换行符
print(f"读取后指针位置: {f.tell()}")

line2 = f.readline()
print(f"第2行: '{line2.strip()}'")
print(f"读取后指针位置: {f.tell()}")

line3 = f.readline()
print(f"第3行: '{line3.strip()}'")
print(f"读取后指针位置: {f.tell()}")
f.close()

print()

# ============================================
# 方法三：readlines() - 读取所有行到列表
# ============================================
print("3. readlines() 方法演示：")
print("-" * 30)

f = open('test.txt', 'r', encoding='utf-8')
lines = f.readlines()  # 返回列表，每个元素是一行
print(f"readlines()返回类型: {type(lines)}")
print(f"列表内容: {lines}")
print(f"列表长度: {len(lines)}")

# 遍历每一行
print("遍历各行内容：")
for i, line in enumerate(lines):
    print(f"第{i+1}行: '{line.strip()}'")  # strip()去除换行符
f.close()

print()

# ============================================
# 三种方法对比总结
# ============================================
print("=== 三种读取方法对比总结 ===")
print("┌─────────────┬──────────────────┬─────────────────────┐")
print("│   方法名     │     返回类型      │       适用场景       │")
print("├─────────────┼──────────────────┼─────────────────────┤")
print("│ read()      │ 字符串(str)       │ 读取全部或指定字节   │")
print("│ readline()  │ 字符串(str)       │ 逐行处理大文件      │")  
print("│ readlines() │ 列表(list)        │ 一次性读取所有行    │")
print("└─────────────┴──────────────────┴─────────────────────┘")

print("\n=== 重要提醒 ===")
print("1. 读取文件时必须使用 'r' 模式")
print("2. 每次读取操作都会移动文件指针")
print("3. 记得使用 f.close() 关闭文件或使用 with 语句")
print("4. 推荐使用 with 语句自动管理文件资源")

# ============================================
# 推荐的最佳实践示例
# ============================================
print("\n=== 最佳实践示例 ===")

# 使用 with 语句安全读取文件
print("使用 with 语句读取：")
with open('test.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(f"文件内容: {repr(content)}")
# 文件会自动关闭，无需手动调用close()

# 清理测试文件
import os
if os.path.exists('test.txt'):
    os.remove('test.txt')
    print("\n测试文件已清理")
