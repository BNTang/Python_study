# -*- coding: utf-8 -*-

# @Time    : 2025-06-03
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 19-Python-文件操作-案例1-文件复制

import os

# 文件复制案例 - 步骤分析：
# 1. 以只读模式打开源文件
# 2. 以写入模式打开目标文件（副本）
# 3. 从源文件读取内容
# 4. 将读取的内容写入目标文件
# 5. 关闭两个文件

# 切换到files目录（如果存在的话）
try:
    os.chdir('files')
except FileNotFoundError:
    print("files目录不存在，在当前目录创建文件")

def copy_file(source_filename, target_filename):
    """
    文件复制函数
    :param source_filename: 源文件名
    :param target_filename: 目标文件名
    """
    try:
        # 步骤1: 以只读模式打开源文件，指定UTF-8编码
        source_file = open(source_filename, 'r', encoding='utf-8')
        
        # 步骤2: 以写入模式打开目标文件，指定UTF-8编码
        dst_file = open(target_filename, 'w', encoding='utf-8')
        
        # 步骤3: 从源文件读取所有内容
        content = source_file.read()
        
        # 步骤4: 将内容写入目标文件
        dst_file.write(content)
        
        # 步骤5: 关闭文件
        source_file.close()
        dst_file.close()
        
        print(f"文件复制成功: {source_filename} -> {target_filename}")
        
    except FileNotFoundError:
        print(f"错误: 找不到源文件 {source_filename}")
    except PermissionError:
        print("错误: 没有文件操作权限")
    except Exception as e:
        print(f"复制过程中发生错误: {e}")

# 创建一个测试文件
def create_test_file():
    """创建一个测试用的源文件"""
    test_content = """这是一个测试文件
用于演示文件复制功能
包含中文内容测试编码处理
File copy test content
测试完成"""
    
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write(test_content)
    print("测试文件 test.txt 创建成功")

# 使用with语句的更安全的文件复制方法
def copy_file_with_context(source_filename, target_filename):
    """
    使用with语句的文件复制（推荐方法）
    自动处理文件关闭，即使出现异常也能正确关闭文件
    """
    try:
        with open(source_filename, 'r', encoding='utf-8') as source_file:
            with open(target_filename, 'w', encoding='utf-8') as dst_file:
                # 一次性读取所有内容（适合小文件）
                content = source_file.read()
                dst_file.write(content)
        
        print(f"文件复制成功 (with语句): {source_filename} -> {target_filename}")
        
    except FileNotFoundError:
        print(f"错误: 找不到源文件 {source_filename}")
    except Exception as e:
        print(f"复制过程中发生错误: {e}")

# 处理大文件的分块复制方法
def copy_large_file(source_filename, target_filename, chunk_size=1024):
    """
    分块复制大文件
    :param source_filename: 源文件名
    :param target_filename: 目标文件名  
    :param chunk_size: 每次读取的字节数
    """
    try:
        with open(source_filename, 'r', encoding='utf-8') as source_file:
            with open(target_filename, 'w', encoding='utf-8') as dst_file:
                while True:
                    # 分块读取
                    chunk = source_file.read(chunk_size)
                    if not chunk:  # 读取完毕
                        break
                    dst_file.write(chunk)
        
        print(f"大文件复制成功: {source_filename} -> {target_filename}")
        
    except Exception as e:
        print(f"大文件复制错误: {e}")

if __name__ == "__main__":
    # 演示文件复制功能
    
    print("=== Python文件复制案例演示 ===\n")
    
    # 1. 创建测试文件
    create_test_file()
    
    # 2. 基本文件复制
    print("\n1. 基本文件复制:")
    copy_file('test.txt', 'copy1.txt')
    
    # 3. 使用with语句复制（推荐）
    print("\n2. 使用with语句复制:")
    copy_file_with_context('test.txt', 'copy2.txt')
    
    # 4. 大文件分块复制演示
    print("\n3. 分块复制演示:")
    copy_large_file('test.txt', 'copy3.txt', chunk_size=10)
    
    print("\n=== 关键知识点总结 ===")
    print("1. 文件复制三步骤: 打开源文件 -> 读取内容 -> 写入目标文件")
    print("2. 编码处理: 统一使用UTF-8编码避免乱码")
    print("3. 异常处理: 使用try-except处理文件不存在等错误")
    print("4. 资源管理: 推荐使用with语句自动关闭文件")
    print("5. 大文件处理: 使用分块读取避免内存溢出")
