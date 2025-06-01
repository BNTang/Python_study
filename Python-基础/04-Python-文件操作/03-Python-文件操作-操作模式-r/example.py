# -*- coding: utf-8 -*-

# @Time    : 2025-5-31
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 03-Python-文件操作-操作模式-r

"""
Python文件操作三大步骤：
1. 打开文件 (open)
2. 读写操作 (read/write)
3. 关闭文件 (close)
"""

# ============== 1. 文件操作基础语法 ==============
print("=" * 50)
print("1. 文件操作基础语法")
print("=" * 50)

# open函数常用参数：
# open(file, mode='r', ...)
# file: 文件路径（相对路径或绝对路径）
# mode: 操作模式（r-读取, w-写入, a-追加等）

# 相对路径示例：相对于当前Python文件的同级目录
# 绝对路径示例：完整的文件路径

# ============== 2. 'r'模式特性详解 ==============
print("\n2. 'r'模式的三个重要特性：")
print("-" * 30)
print("特性1: 如果文件不存在，则会报错")
print("特性2: 以只读方式打开文件（不能写入）")
print("特性3: 文件指针指向文件开头")

# ============== 3. 创建测试文件 ==============
# 首先创建一个测试文件用于演示
test_content = "abcdefg\n这是第二行\n这是第三行"
with open("test.txt", "w", encoding="utf-8") as f:
    f.write(test_content)
print("\n✓ 已创建测试文件 test.txt")

# ============== 4. 'r'模式实际操作演示 ==============
print("\n" + "=" * 50)
print("4. 'r'模式实际操作演示")
print("=" * 50)

# 演示1：文件不存在时的错误
print("\n演示1：文件不存在时会报错")
try:
    f = open("不存在的文件.txt", "r", encoding="utf-8")
except FileNotFoundError as e:
    print(f"❌ 错误：{e}")

# 演示2：正确打开文件并读取
print("\n演示2：正确打开并读取文件")
try:
    # 第一步：打开文件
    f = open("test.txt", "r", encoding="utf-8")
    print("✓ 文件打开成功")
    
    # 第二步：读取操作
    content = f.read()  # 读取全部内容
    print(f"📖 读取内容：\n{content}")
    
    # 第三步：关闭文件
    f.close()
    print("✓ 文件已关闭")
    
except Exception as e:
    print(f"❌ 操作失败：{e}")

# 演示3：验证只读特性（不能写入）
print("\n演示3：验证'r'模式不能写入")
try:
    f = open("test.txt", "r", encoding="utf-8")
    # 尝试写入操作
    f.write("尝试写入新内容")  # 这里会报错
except Exception as e:
    print(f"❌ 写入失败：{e}")
    print("✓ 验证了'r'模式确实不支持写入操作")
finally:
    if 'f' in locals() and not f.closed:
        f.close()

# ============== 5. 文件指针位置演示 ==============
print("\n演示4：文件指针从开头开始")
f = open("test.txt", "r", encoding="utf-8")

# 使用tell()查看当前指针位置
print(f"📍 打开文件后指针位置：{f.tell()}")

# 读取前5个字符
partial_content = f.read(5)
print(f"📖 读取前5个字符：'{partial_content}'")
print(f"📍 读取后指针位置：{f.tell()}")

# 继续读取剩余内容
remaining_content = f.read()
print(f"📖 剩余内容：'{remaining_content}'")

f.close()

# ============== 6. 推荐使用with语句 ==============
print("\n" + "=" * 50)
print("6. 推荐使用with语句（自动关闭文件）")
print("=" * 50)

print("\n使用with语句的优势：")
print("- 自动关闭文件，无需手动调用close()")
print("- 即使出现异常也能正确关闭文件")
print("- 代码更简洁安全")

# with语句示例
print("\nwith语句示例：")
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(f"📖 文件内容：\n{content}")
# 文件在这里自动关闭

print("✓ 文件已自动关闭")

# ============== 7. 总结要点 ==============
print("\n" + "=" * 50)
print("7. 'r'模式总结")
print("=" * 50)
print("""
📚 关键知识点：
1. 'r'是open()函数的默认模式
2. 只能读取，不能写入
3. 文件必须存在，否则报FileNotFoundError
4. 文件指针从文件开头开始
5. 推荐使用with语句进行文件操作

💡 使用场景：
- 读取配置文件
- 读取日志文件  
- 读取文本数据进行分析
- 读取程序需要的静态数据
""")

# 清理测试文件
import os
if os.path.exists("test.txt"):
    os.remove("test.txt")
    print("\n🧹 已清理测试文件")
