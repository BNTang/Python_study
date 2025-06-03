# -*- coding: utf-8 -*-

# @Time    : 2025-06-03
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 11-Python-文件操作-判定可读

"""
知识点：Python文件操作 - 判定文件是否可读

为什么需要判定文件是否可读？
- 提升代码的容错程度和健壮性
- 避免因文件权限问题导致程序崩溃
- 在读取文件前进行预检查

核心方法：file.readable()
- 返回True：文件可读
- 返回False：文件不可读
"""

# 1. 首先创建一个测试文件
print("=== 1. 创建测试文件 ===")
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("12345\n这是测试内容")
print("测试文件创建完成")

# 2. 演示不同文件打开模式的可读性
print("\n=== 2. 不同文件打开模式的可读性测试 ===")

# 以读取模式打开文件 - 可读
print("以读取模式(r)打开文件:")
with open("test.txt", "r", encoding="utf-8") as f:
    print(f"文件是否可读: {f.readable()}")
    if f.readable():
        content = f.read()
        print(f"文件内容: {content}")

# 以追加模式打开文件 - 不可读
print("\n以追加模式(a)打开文件:")
with open("test.txt", "a", encoding="utf-8") as f:
    print(f"文件是否可读: {f.readable()}")
    if f.readable():
        content = f.read()
        print(f"文件内容: {content}")
    else:
        print("文件不可读，跳过读取操作")

# 以写入模式打开文件 - 不可读
print("\n以写入模式(w)打开文件:")
with open("test.txt", "w", encoding="utf-8") as f:
    print(f"文件是否可读: {f.readable()}")
    if f.readable():
        content = f.read()
        print(f"文件内容: {content}")
    else:
        print("文件不可读，跳过读取操作")

# 3. 容错处理的重要性演示
print("\n=== 3. 容错处理演示 ===")

# 不使用容错处理的代码（会报错）
print("不使用容错处理的风险:")
try:
    with open("test.txt", "a", encoding="utf-8") as f:
        # 直接读取会报错
        content = f.read()
        print(content)
except Exception as e:
    print(f"错误信息: {e}")
    print("这种错误会影响后续代码执行")

# 使用容错处理的正确做法
print("\n使用容错处理的正确做法:")
with open("test.txt", "a", encoding="utf-8") as f:
    if f.readable():
        content = f.read()
        print(f"文件内容: {content}")
    else:
        print("文件不可读，程序正常继续执行")

print("后续代码正常执行...")

# 4. 实际应用场景
print("\n=== 4. 实际应用场景 ===")

def safe_read_file(filename, mode="r"):
    """
    安全读取文件的函数
    
    Args:
        filename: 文件名
        mode: 打开模式
    
    Returns:
        文件内容或None
    """
    try:
        with open(filename, mode, encoding="utf-8") as f:
            if f.readable():
                return f.read()
            else:
                print(f"警告: 文件 {filename} 在 {mode} 模式下不可读")
                return None
    except FileNotFoundError:
        print(f"错误: 文件 {filename} 不存在")
        return None
    except Exception as e:
        print(f"错误: 读取文件时发生异常 - {e}")
        return None

# 测试安全读取函数
print("测试安全读取函数:")
result1 = safe_read_file("test.txt", "r")
print(f"读取模式结果: {result1}")

result2 = safe_read_file("test.txt", "a")
print(f"追加模式结果: {result2}")

result3 = safe_read_file("不存在的文件.txt", "r")
print(f"不存在文件结果: {result3}")

# 5. 重点总结
print("\n=== 重点总结 ===")
print("1. 使用 file.readable() 方法判定文件是否可读")
print("2. 不同文件打开模式有不同的读写权限:")
print("   - 'r': 只读模式，可读不可写")
print("   - 'w': 写入模式，可写不可读")
print("   - 'a': 追加模式，可写不可读")
print("   - 'r+': 读写模式，既可读又可写")
print("3. 容错处理可以提升代码健壮性，避免程序崩溃")
print("4. 在文件操作前进行权限检查是良好的编程习惯")

# 清理测试文件
import os
if os.path.exists("test.txt"):
    os.remove("test.txt")
    print("\n测试文件已清理")
