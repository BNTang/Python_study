# -*- coding: utf-8 -*-

# @Time    : 2025-06-04
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 22-Python-文件操作-案例3-列表清单

import os

# ====== 知识点1: os.listdir()基础使用 ======
# os.listdir() 只能列出当前目录下的直接子文件和子文件夹，不会深入递归

def basic_list_demo():
    """演示 os.listdir() 的基础用法"""
    print("=== os.listdir() 基础演示 ===")
    file_list = os.listdir(".")  # 列出当前目录
    print("当前目录下的文件和文件夹:", file_list)
    print()

# ====== 知识点2: 递归函数实现深层遍历 ======
# 递归思路：
# 1. 列举当前目录下所有文件和子文件夹
# 2. 遍历列表，判断每个项目是文件还是目录
# 3. 如果是目录，递归调用自身继续遍历
# 4. 如果是文件，直接处理（打印或写入）

def list_files_to_txt(dir_path, output_file):
    """
    递归遍历目录并将文件清单写入txt文件
    
    Args:
        dir_path: 要遍历的目录路径
        output_file: 输出文件对象
    """
    # 第一步：列举出当前给定文件夹下的所有子文件和子文件夹
    try:
        file_list = os.listdir(dir_path)
    except PermissionError:
        print(f"无权限访问目录: {dir_path}")
        return
    
    # 第二步：遍历列表并判定是否是目录
    for file_name in file_list:
        # 构建完整路径（重要：避免相对路径问题）
        full_path = os.path.join(dir_path, file_name)
        
        # 判断是目录还是文件
        if os.path.isdir(full_path):
            # 是目录：先写入目录名，然后递归遍历
            output_file.write(f"{file_name}/\n")  # 目录名后加斜杠标识
            list_files_to_txt(full_path, output_file)  # 递归调用
            output_file.write("\n")  # 每组结束后添加空行
        else:
            # 是文件：直接写入文件名（添加缩进美化格式）
            output_file.write(f"\t{file_name}\n")

# ====== 知识点3: 文件操作与路径处理 ======
def generate_file_list(target_dir="files", output_filename="list.txt"):
    """
    生成文件清单的主函数
    
    Args:
        target_dir: 要遍历的目标目录
        output_filename: 输出文件名
    """
    print(f"=== 开始生成 {target_dir} 目录的文件清单 ===")
    
    # 检查目标目录是否存在
    if not os.path.exists(target_dir):
        print(f"错误：目录 '{target_dir}' 不存在")
        return
    
    # 以追加模式打开文件（如果需要多次写入）
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(f"=== {target_dir} 目录文件清单 ===\n\n")
        list_files_to_txt(target_dir, f)
    
    print(f"文件清单已生成到: {output_filename}")

# ====== 知识点4: 增强版 - 带统计功能的文件清单 ======
def list_files_with_stats(dir_path, output_file, indent_level=0):
    """
    增强版：递归遍历并统计文件信息
    
    Args:
        dir_path: 目录路径
        output_file: 输出文件对象
        indent_level: 缩进级别（用于美化输出）
    """
    indent = "\t" * indent_level
    file_count = 0
    dir_count = 0
    
    try:
        file_list = os.listdir(dir_path)
        file_list.sort()  # 排序，让输出更整齐
    except PermissionError:
        output_file.write(f"{indent}[无权限访问]\n")
        return 0, 0
    
    for file_name in file_list:
        full_path = os.path.join(dir_path, file_name)
        
        if os.path.isdir(full_path):
            dir_count += 1
            output_file.write(f"{indent}📁 {file_name}/\n")
            # 递归统计子目录
            sub_files, sub_dirs = list_files_with_stats(full_path, output_file, indent_level + 1)
            file_count += sub_files
            dir_count += sub_dirs
        else:
            file_count += 1
            # 获取文件大小
            try:
                file_size = os.path.getsize(full_path)
                size_str = format_file_size(file_size)
                output_file.write(f"{indent}📄 {file_name} ({size_str})\n")
            except:
                output_file.write(f"{indent}📄 {file_name}\n")
    
    return file_count, dir_count

def format_file_size(size_bytes):
    """格式化文件大小显示"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"

def generate_enhanced_file_list(target_dir="files", output_filename="enhanced_list.txt"):
    """生成增强版文件清单"""
    print(f"=== 生成增强版文件清单 ===")
    
    if not os.path.exists(target_dir):
        print(f"错误：目录 '{target_dir}' 不存在")
        return
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(f"=== {target_dir} 目录详细清单 ===\n")
        f.write(f"生成时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        total_files, total_dirs = list_files_with_stats(target_dir, f)
        
        f.write(f"\n=== 统计信息 ===\n")
        f.write(f"总文件数: {total_files}\n")
        f.write(f"总目录数: {total_dirs}\n")
    
    print(f"增强版文件清单已生成到: {output_filename}")

# ====== 主程序执行 ======
if __name__ == "__main__":
    # 演示基础用法
    basic_list_demo()
    
    # 生成基础文件清单
    generate_file_list()
    
    # 生成增强版文件清单
    generate_enhanced_file_list()
    
    print("\n=== 核心知识点总结 ===")
    print("1. os.listdir() - 列出目录内容（不递归）")
    print("2. os.path.isdir() - 判断是否为目录")
    print("3. os.path.isfile() - 判断是否为文件") 
    print("4. os.path.join() - 安全的路径拼接")
    print("5. 递归函数 - 实现深层目录遍历")
    print("6. 文件写入 - 将结果保存到文件")
    print("7. 异常处理 - 处理权限和路径问题")
