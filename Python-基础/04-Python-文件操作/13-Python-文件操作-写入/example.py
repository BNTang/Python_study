# -*- coding: utf-8 -*-

# @Time    : 2025-06-03
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 13-Python-文件操作-写入

"""
Python文件操作 - 写入操作详解

重点知识：
1. write()方法的基本使用
2. write()方法的返回值（写入内容的字节长度）
3. 使用writable()方法进行容错处理
4. 不同文件模式对写入操作的影响
"""

print("=== Python文件写入操作演示 ===\n")

# 1. 基本的写入操作
print("1. 基本写入操作:")
f = open("a.txt", "a")  # 以追加模式打开文件
result = f.write("abc")  # write()方法返回写入内容的字节长度
print(f"写入返回值: {result}")  # 打印返回值，应该是3
f.close()

print("查看文件内容后再次写入...")
f = open("a.txt", "a")
result = f.write("abc")  # 再次写入相同内容
print(f"第二次写入返回值: {result}")  # 仍然返回3，不是文件总长度
f.close()

print("\n重点：write()返回值是本次写入的字节长度，不是文件总长度\n")

# 2. 带容错处理的写入操作
print("2. 带容错处理的写入操作:")
f = open("a.txt", "a")  # 以追加模式打开
if f.writable():  # 检查文件是否可写
    result = f.write("def")
    print(f"可写模式 - 写入成功，返回值: {result}")
else:
    print("文件不可写")
f.close()

# 3. 演示只读模式下的行为
print("\n3. 只读模式下的写入尝试:")
f = open("a.txt", "r")  # 以只读模式打开
if f.writable():  # 检查是否可写
    result = f.write("ghi")
    print(f"写入返回值: {result}")
else:
    print("只读模式 - 文件不可写，跳过写入操作")
f.close()

# 4. 不同写入模式的演示
print("\n4. 不同写入模式对比:")

# 写入模式 'w' - 覆盖原有内容
print("使用 'w' 模式（覆盖写入）:")
with open("test_w.txt", "w") as f:
    result = f.write("第一行内容\n")
    print(f"写入字节数: {result}")

with open("test_w.txt", "w") as f:  # 再次以w模式打开
    result = f.write("新内容")  # 会覆盖之前的内容
    print(f"覆盖写入字节数: {result}")

# 追加模式 'a' - 在文件末尾追加
print("\n使用 'a' 模式（追加写入）:")
with open("test_a.txt", "a") as f:
    result = f.write("第一行内容\n")
    print(f"写入字节数: {result}")

with open("test_a.txt", "a") as f:  # 再次以a模式打开
    result = f.write("追加内容\n")  # 在末尾追加
    print(f"追加写入字节数: {result}")

# 5. 使用with语句的最佳实践
print("\n5. 推荐的写入方式（使用with语句）:")
filename = "best_practice.txt"

# 检查并写入
try:
    with open(filename, "w", encoding="utf-8") as f:
        if f.writable():
            content = "这是使用with语句的最佳实践示例\n包含中文内容测试"
            result = f.write(content)
            print(f"使用with语句写入成功，字节数: {result}")
        else:
            print("文件不可写")
except IOError as e:
    print(f"文件操作错误: {e}")

print("\n=== 知识点总结 ===")
print("1. write()方法返回写入内容的字节长度")
print("2. 使用writable()检查文件是否可写")
print("3. 'w'模式会覆盖原有内容，'a'模式会追加内容")
print("4. 推荐使用with语句自动管理文件关闭")
print("5. 添加适当的异常处理提高代码健壮性")
