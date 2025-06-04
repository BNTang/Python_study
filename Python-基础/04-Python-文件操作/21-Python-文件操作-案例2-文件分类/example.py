# -*- coding: utf-8 -*-

# @Time    : 2025-06-04
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 21-Python-文件操作-案例2-文件分类

"""
文件分类案例实现
功能：按照文件后缀名自动将文件分类到不同文件夹中

实现步骤：
1. 遍历所有文件
2. 分解文件后缀名
3. 查看是否存在同名目录
4. 如果不存在则创建目录
5. 移动文件到对应目录

示例：
- a.txt, e.txt -> txt文件夹
- b.jpg, c.jpg -> jpg文件夹  
- d.py, f.py -> py文件夹
"""

import os
import shutil

def main():
    # 第0步：定义要处理的文件路径
    path = "files"
    
    # 容错处理1：检查路径是否存在
    if not os.path.exists(path):
        print(f"错误：路径 {path} 不存在！")
        exit()
    
    # 切换到目标目录
    os.chdir(path)
    
    # 第1步：获取所有文件名称列表
    file_list = os.listdir("./")
    print("文件列表:", file_list)
    
    # 第2步：遍历所有文件
    for file_name in file_list:
        print(f"\n正在处理文件: {file_name}")
        
        # 跳过目录，只处理文件
        if os.path.isdir(file_name):
            print(f"  跳过目录: {file_name}")
            continue
        
        # 第3步：分解文件后缀名
        # 3.1 获取最后一个点的索引位置（从右往左查找）
        index = file_name.rfind(".")
        
        # 容错处理2：检查是否找到扩展名
        if index == -1:
            print(f"  跳过无扩展名文件: {file_name}")
            continue
        
        # 3.2 根据索引位置截取后缀名（去掉点号）
        extension = file_name[index + 1:]
        print(f"  文件扩展名: {extension}")
        
        # 第4步：检查是否存在同名目录，如果不存在则创建
        if not os.path.exists(extension):
            print(f"  创建目录: {extension}")
            os.mkdir(extension)
        else:
            print(f"  目录已存在: {extension}")
        
        # 第5步：移动文件到对应目录
        try:
            # 移动文件：从当前位置移动到扩展名文件夹中
            shutil.move(file_name, extension)
            print(f"  文件移动成功: {file_name} -> {extension}/")
        except Exception as e:
            print(f"  文件移动失败: {e}")

def create_test_files():
    """
    创建测试文件的辅助函数
    用于演示文件分类功能
    """
    test_files = [
        "a.txt", "e.txt",           # txt文件
        "b.jpg", "c.jpg",           # jpg文件  
        "d.py", "f.py",             # py文件
        "test.pdf",                 # pdf文件
        "demo.docx",                # docx文件
        "no_extension_file"         # 无扩展名文件
    ]
    
    # 确保files目录存在
    if not os.path.exists("files"):
        os.mkdir("files")
    
    # 创建测试文件
    for file_name in test_files:
        file_path = os.path.join("files", file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"这是测试文件 {file_name} 的内容")
    
    print("测试文件创建完成！")

if __name__ == "__main__":
    # 可以先运行这个函数创建测试文件
    # create_test_files()
    
    # 运行主程序
    main()
    
    print("\n文件分类完成！")

"""
重点知识总结：

1. 文件操作核心方法：
   - os.listdir()：获取目录下所有文件和文件夹
   - os.path.exists()：检查路径是否存在
   - os.mkdir()：创建目录
   - os.chdir()：切换当前工作目录
   - shutil.move()：移动文件

2. 字符串处理技巧：
   - str.rfind()：从右往左查找字符，返回索引
   - 字符串切片：[start:end] 提取子字符串

3. 容错处理要点：
   - 检查路径存在性
   - 处理无扩展名文件
   - 异常捕获与处理

4. 编程逻辑：
   - 先判断后操作
   - 使用continue跳过不符合条件的项目
   - 模块化函数设计

5. 实际应用场景：
   - 下载文件夹整理
   - 项目文件分类
   - 批量文件处理
"""
