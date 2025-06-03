# -*- coding: utf-8 -*-

# @Time    : 2025-06-03
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 18-Python-文件操作-其他操作-查看改变列举目录

import os

print("=== Python文件操作：目录相关操作 ===\n")

# 1. 获取当前工作目录
print("1. 获取当前工作目录：")
current_dir = os.getcwd()
print(f"当前目录：{current_dir}\n")

# 2. 在当前目录创建文件
print("2. 在当前目录创建文件：")
with open("cc.py", "w", encoding="utf-8") as f:
    f.write("# 这是在当前目录创建的文件")
print("创建文件：cc.py\n")

# 3. 创建目录并在其中创建文件
print("3. 创建目录并在其中创建文件：")
if not os.path.exists("a"):
    os.makedirs("a")
    print("创建目录：a")

# 方法1：直接指定路径创建文件
with open("a/dd.py", "w", encoding="utf-8") as f:
    f.write("# 这是在a目录下创建的文件")
print("在a目录下创建文件：dd.py\n")

# 4. 改变当前目录
print("4. 改变当前目录：")
original_dir = os.getcwd()
os.chdir("a")
print(f"切换后的当前目录：{os.getcwd()}")

# 在新目录下创建文件
with open("ee.py", "w", encoding="utf-8") as f:
    f.write("# 这是切换目录后创建的文件")
print("在a目录下创建文件：ee.py")

# 恢复到原目录
os.chdir(original_dir)
print(f"恢复到原目录：{os.getcwd()}\n")

# 5. 列举目录内容
print("5. 列举目录内容：")

# 列举当前目录（使用 "." 表示当前目录）
print("当前目录内容（使用 '.'）：")
current_contents = os.listdir(".")
print(current_contents)
print()

# 列举a目录内容
print("a目录内容：")
a_contents = os.listdir("a")
print(a_contents)
print()

# 列举上级目录（使用 ".." 表示上级目录）
print("上级目录内容（使用 '..'）：")
try:
    parent_contents = os.listdir("..")
    print(parent_contents[:5])  # 只显示前5个，避免输出过多
    print("...")
except Exception as e:
    print(f"无法访问上级目录：{e}")

print("\n=== 重要知识点总结 ===")
print("• os.getcwd() - 获取当前工作目录")
print("• os.chdir(path) - 改变当前工作目录")
print("• os.listdir(path) - 列举指定目录的内容")
print("• '.' - 表示当前目录")
print("• '..' - 表示上级目录")
print("• 相对路径是相对于当前工作目录的")
print("• listdir()返回的是列表，只列举一级目录内容")
