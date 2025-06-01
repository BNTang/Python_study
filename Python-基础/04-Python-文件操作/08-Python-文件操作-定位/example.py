# -*- coding: utf-8 -*-

# @Time    : 2025-06-01
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 08-Python-文件操作-定位

"""
文件操作 - 定位以及读写操作

重点知识：
1. 文件指针：类似一个游标，指示当前读写位置
2. tell() 方法：查看当前文件指针位置
3. seek() 方法：移动文件指针到指定位置
4. seek(offset, whence) 参数说明：
   - offset: 偏移量
   - whence: 参照点 (0=开头, 1=当前位置, 2=末尾)
5. 文本模式只能使用 whence=0，二进制模式可以使用 0,1,2
"""

print("=" * 50)
print("文件定位操作演示")
print("=" * 50)

# 首先创建一个测试文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("12345678")

print("\n1. 基本文件读取（默认从开头开始）")
print("-" * 30)
# 打开文件进行读取
f = open("test.txt", "r", encoding="utf-8")

# 查看初始文件指针位置
print(f"初始文件指针位置: {f.tell()}")

# 读取文件内容
content = f.read()
print(f"读取的内容: {content}")

# 查看读取后的文件指针位置
print(f"读取后文件指针位置: {f.tell()}")

f.close()

print("\n2. 使用 seek() 移动文件指针")
print("-" * 30)
f = open("test.txt", "r", encoding="utf-8")

print(f"打开后文件指针位置: {f.tell()}")

# 移动文件指针到位置2（从开头算起）
f.seek(2)
print(f"执行 seek(2) 后文件指针位置: {f.tell()}")

# 从当前位置读取剩余内容
content = f.read()
print(f"从位置2开始读取的内容: {content}")

# 查看读取完成后的文件指针位置
print(f"读取完成后文件指针位置: {f.tell()}")

f.close()

print("\n3. seek() 方法的完整参数演示（二进制模式）")
print("-" * 30)

# 二进制模式可以使用所有参照点
f = open("test.txt", "rb")

print(f"二进制模式打开后文件指针位置: {f.tell()}")

# whence=0: 相对于文件开头（默认值）
f.seek(2, 0)
print(f"seek(2, 0) - 相对开头偏移2: {f.tell()}")

# whence=1: 相对于当前位置
f.seek(1, 1)
print(f"seek(1, 1) - 相对当前位置偏移1: {f.tell()}")

# whence=2: 相对于文件末尾
f.seek(-2, 2)
print(f"seek(-2, 2) - 相对末尾偏移-2: {f.tell()}")

# 从当前位置读取
content = f.read()
print(f"从当前位置读取的内容: {content}")

print(f"最终文件指针位置: {f.tell()}")

f.close()

print("\n4. 文本模式的限制演示")
print("-" * 30)

try:
    f = open("test.txt", "r", encoding="utf-8")
    # 文本模式只能使用 whence=0
    f.seek(2, 1)  # 这会引发错误
except Exception as e:
    print(f"文本模式使用 whence=1 的错误: {e}")
finally:
    if 'f' in locals() and not f.closed:
        f.close()

print("\n5. 实际应用场景演示")
print("-" * 30)

# 创建一个更大的测试文件
with open("large_test.txt", "w", encoding="utf-8") as f:
    for i in range(1, 101):
        f.write(f"Line {i}: This is line number {i}\n")

# 场景1: 读取文件的最后几行
print("场景1: 读取文件末尾内容")
with open("large_test.txt", "rb") as f:
    # 移动到文件末尾前100个字节
    f.seek(-100, 2)
    content = f.read().decode('utf-8')
    print("文件末尾100字节内容:")
    print(content)

# 场景2: 跳过文件头，从特定位置开始读取
print("\n场景2: 跳过前面内容，从中间开始读取")
with open("large_test.txt", "r", encoding="utf-8") as f:
    # 跳过前500个字符
    f.seek(500)
    lines = f.readlines()[:5]  # 读取5行
    print("从500字符位置开始的5行:")
    for line in lines:
        print(line.strip())

print("\n" + "=" * 50)
print("重要知识点总结:")
print("=" * 50)
print("1. tell() - 获取当前文件指针位置")
print("2. seek(offset, whence) - 移动文件指针")
print("   - whence=0: 文件开头（默认）")
print("   - whence=1: 当前位置（仅二进制模式）")
print("   - whence=2: 文件末尾（仅二进制模式）")
print("3. 文本模式只能使用 whence=0")
print("4. 二进制模式支持所有 whence 值")
print("5. 读写操作会改变文件指针位置")

# 清理测试文件
import os
try:
    os.remove("test.txt")
    os.remove("large_test.txt")
    print("\n测试文件已清理")
except:
    pass
