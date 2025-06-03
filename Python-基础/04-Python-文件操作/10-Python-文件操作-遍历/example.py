# -*- coding: utf-8 -*-

# @Time    : 2025-06-03
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 10-Python-文件操作-遍历

"""
Python文件操作-遍历

重点知识：
1. 三种文件读取方法：read(), readline(), readlines()
2. 两种遍历方式：直接遍历文件对象、遍历行列表
3. 文件对象是迭代器，支持懒加载
"""

import collections.abc

# 首先创建一个示例文件用于演示
def create_demo_file():
    """创建演示用的文件"""
    with open('demo.txt', 'w', encoding='utf-8') as f:
        f.write('1\n2\n3\n4\n5')
    print("演示文件已创建")

# 演示三种文件读取方法
def demo_read_methods():
    """演示三种读取文件的方法"""
    print("\n=== 三种文件读取方法演示 ===")
    
    # 方法1：read() - 读取指定字节数或全部内容
    with open('demo.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"read()方法读取全部内容：{repr(content)}")
    
    # 方法2：readline() - 按行读取
    with open('demo.txt', 'r', encoding='utf-8') as f:
        print("\nreadline()方法按行读取：")
        line = f.readline()
        while line:
            print(f"读取到：{repr(line)}")
            line = f.readline()
    
    # 方法3：readlines() - 读取所有行到列表
    with open('demo.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(f"\nreadlines()方法读取所有行：{lines}")

# 演示方式1：直接遍历文件对象
def demo_iterate_file_object():
    """演示直接遍历文件对象"""
    print("\n=== 方式1：直接遍历文件对象 ===")
    
    with open('demo.txt', 'r', encoding='utf-8') as f:
        print("直接遍历文件对象f：")
        for i in f:
            print(repr(i))  # 使用repr显示换行符
        
        # 验证文件对象是迭代器
        f.seek(0)  # 重置文件指针
        is_iterator = isinstance(f, collections.abc.Iterator)
        print(f"\n文件对象是否为迭代器：{is_iterator}")
        print("💡 重点：文件对象是迭代器，支持懒加载，按需读取每一行")

# 演示方式2：遍历行列表
def demo_iterate_lines_list():
    """演示遍历readlines()返回的行列表"""
    print("\n=== 方式2：遍历行列表 ===")
    
    with open('demo.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
        print("遍历readlines()返回的列表：")
        for i in content:
            print(repr(i))
        
        # 使用strip()去除换行符
        f.seek(0)
        content_stripped = f.readlines()
        print("\n使用strip()去除换行符：")
        for i in content_stripped:
            print(repr(i.strip()))

# 对比两种遍历方式的差异
def compare_iteration_methods():
    """对比两种遍历方式"""
    print("\n=== 两种遍历方式对比 ===")
    
    # 创建更复杂的测试文件
    with open('demo.txt', 'w', encoding='utf-8') as f:
        f.write('1\n22\n333\n4444\n55555')
    
    print("方式1 - 直接遍历文件对象（逐行处理）：")
    with open('demo.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(f"处理行：{repr(line.strip())}")
    
    print("\n方式2 - 遍历行列表（一次性加载）：")
    with open('demo.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(f"处理行：{repr(line.strip())}")

# 主函数演示
def main():
    """主函数：演示所有功能"""
    print("🎯 Python文件操作-遍历学习")
    
    # 创建演示文件
    create_demo_file()
    
    # 演示三种读取方法
    demo_read_methods()
    
    # 演示两种遍历方式
    demo_iterate_file_object()
    demo_iterate_lines_list()
    
    # 对比两种方式
    compare_iteration_methods()
    
    print("\n📚 学习总结：")
    print("1. 文件对象本身就是迭代器，可以直接用for循环遍历")
    print("2. readlines()返回列表，也可以用for循环遍历")
    print("3. 直接遍历文件对象更节省内存（懒加载）")
    print("4. 遍历行列表适合需要多次访问所有行的场景")

if __name__ == "__main__":
    main()
