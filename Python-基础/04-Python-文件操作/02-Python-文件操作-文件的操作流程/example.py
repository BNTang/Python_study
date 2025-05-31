# -*- coding: utf-8 -*-

# @Time    : 2025-5-30
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 02-Python-文件操作-文件的操作流程

"""
文件操作流程 - 核心知识点整理
===============================

文件操作三大步骤：
1. 打开文件 - 建立文件句柄(管道)
2. 读写操作 - 通过句柄进行数据操作
3. 关闭文件 - 释放资源，断开连接

文件句柄概念：
- 类似于连接程序和文件的"管道"
- 不同类型的管道有不同的权限(只读/只写/读写)
- 通过文件句柄进行所有文件操作
"""

# ==================== 第一步：打开文件 ====================
print("=" * 50)
print("第一步：打开文件 - 建立文件句柄")
print("=" * 50)

# 文件打开模式说明
"""
常用文件打开模式：
- 'r'  : 只读模式(默认) - 只能读取，不能写入
- 'w'  : 只写模式 - 只能写入，会覆盖原文件
- 'a'  : 追加模式 - 只能写入，在文件末尾追加
- 'r+' : 读写模式 - 既可读又可写
- 'rb' : 二进制只读模式
- 'wb' : 二进制只写模式
"""

# 示例：不同模式打开文件
try:
    # 只读模式打开（管道类型：单向向外）
    file_r = open('test.txt', 'r', encoding='utf-8')
    print("✓ 只读模式文件打开成功")
    file_r.close()
except FileNotFoundError:
    print("✗ 文件不存在，创建一个测试文件")
    # 创建测试文件
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write("这是测试文件内容\n第二行内容\n第三行内容")

# 只写模式打开（管道类型：单向向内）
file_w = open('test_write.txt', 'w', encoding='utf-8')
print("✓ 只写模式文件打开成功")
file_w.close()

# 读写模式打开（管道类型：双向）
file_rw = open('test.txt', 'r+', encoding='utf-8')
print("✓ 读写模式文件打开成功")
file_rw.close()

# ==================== 第二步：读写操作 ====================
print("\n" + "=" * 50)
print("第二步：读写操作 - 定位、读取、写入")
print("=" * 50)

# 2.1 定位操作
print("\n--- 定位操作 ---")
with open('test.txt', 'r+', encoding='utf-8') as file:
    print(f"当前指针位置: {file.tell()}")  # 获取当前指针位置
    
    # 移动指针到文件开头
    file.seek(0)
    print(f"移动到开头后位置: {file.tell()}")
    
    # 移动指针到文件末尾
    file.seek(0, 2)  # 2表示从文件末尾开始
    print(f"移动到末尾后位置: {file.tell()}")
    
    # 移动指针到指定位置
    file.seek(5)
    print(f"移动到位置5后: {file.tell()}")

# 2.2 读取操作
print("\n--- 读取操作 ---")
with open('test.txt', 'r', encoding='utf-8') as file:
    # 读取全部内容
    file.seek(0)  # 重置到开头
    content_all = file.read()
    print("读取全部内容:")
    print(content_all)
    
    # 读取一行
    file.seek(0)
    line_one = file.readline()
    print(f"读取第一行: {line_one.strip()}")
    
    # 读取所有行到列表
    file.seek(0)
    lines_all = file.readlines()
    print("读取所有行到列表:")
    for i, line in enumerate(lines_all):
        print(f"  第{i+1}行: {line.strip()}")

# 2.3 写入操作
print("\n--- 写入操作 ---")
# 覆盖写入
with open('test_write.txt', 'w', encoding='utf-8') as file:
    file.write("这是新写入的内容\n")
    file.write("第二行新内容\n")
    print("✓ 覆盖写入完成")

# 追加写入
with open('test_write.txt', 'a', encoding='utf-8') as file:
    file.write("这是追加的内容\n")
    print("✓ 追加写入完成")

# 读写模式的综合操作
print("\n--- 读写模式综合操作 ---")
with open('test_write.txt', 'r+', encoding='utf-8') as file:
    # 先读取当前内容
    current_content = file.read()
    print("当前文件内容:")
    print(current_content)
    
    # 在末尾追加内容
    file.write("通过r+模式追加的内容\n")
    print("✓ 追加写入完成")
    
    # 重新读取验证
    file.seek(0)
    new_content = file.read()
    print("追加后的文件内容:")
    print(new_content)

# ==================== 第三步：关闭文件 ====================
print("\n" + "=" * 50)
print("第三步：关闭文件 - 释放资源")
print("=" * 50)

# 方式1：手动关闭（需要记住关闭）
print("--- 方式1：手动关闭 ---")
file = open('test.txt', 'r', encoding='utf-8')
content = file.read()
file.close()  # ⚠️ 切记要关闭！
print("✓ 手动关闭文件完成")

# 方式2：with语句自动关闭（推荐）
print("\n--- 方式2：with语句自动关闭（推荐） ---")
with open('test.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    # 自动关闭，无需手动调用close()
print("✓ with语句自动关闭文件完成")

# ==================== 完整示例 ====================
print("\n" + "=" * 50)
print("完整文件操作示例")
print("=" * 50)

def file_operation_example():
    """文件操作完整流程示例"""
    filename = 'complete_example.txt'
    
    # 第一步：打开文件（写入模式）
    print("1. 打开文件...")
    with open(filename, 'w', encoding='utf-8') as file:
        print("   ✓ 文件句柄建立成功")
        
        # 第二步：写入操作
        print("2. 执行写入操作...")
        file.write("文件操作示例\n")
        file.write("第一行：打开文件\n")
        file.write("第二行：读写操作\n")
        file.write("第三行：关闭文件\n")
        print("   ✓ 写入操作完成")
    
    # 文件在with块结束时自动关闭
    print("3. 文件自动关闭")
    
    # 重新打开文件进行读取
    print("4. 重新打开文件读取内容...")
    with open(filename, 'r', encoding='utf-8') as file:
        print("   ✓ 文件重新打开成功")
        
        # 定位并读取
        file.seek(0)  # 定位到开头
        content = file.read()
        print("   ✓ 读取操作完成")
        print("   文件内容:")
        for line_num, line in enumerate(content.split('\n'), 1):
            if line.strip():
                print(f"     第{line_num}行: {line}")
    
    print("5. 文件操作流程完毕")

# 执行完整示例
file_operation_example()

# ==================== 重要提醒 ====================
print("\n" + "=" * 50)
print("🔥 重要知识点总结")
print("=" * 50)

important_points = [
    "1. 文件句柄就像连接程序和文件的'管道'",
    "2. 不同的打开模式决定了管道的类型（只读/只写/读写）",
    "3. 定位操作用于控制读写的起始位置",
    "4. 文件操作完毕后必须关闭，释放系统资源",
    "5. 推荐使用with语句，可以自动关闭文件",
    "6. 文件操作三步曲：打开 → 读写 → 关闭"
]

for point in important_points:
    print(f"   {point}")

print("\n✅ 文件操作流程学习完成！")
