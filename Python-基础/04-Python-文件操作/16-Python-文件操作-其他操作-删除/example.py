# -*- coding: utf-8 -*-

# @Time    : 2025-06-03
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 16-Python-文件操作-其他操作-删除

import os

print("=== Python 文件操作 - 删除操作 ===")
print()

# ========== 1. 删除文件 ==========
print("1. 删除文件操作")
print("-" * 30)

# 使用 os.remove() 删除文件
print("函数: os.remove(文件路径)")
print("作用: 删除指定的文件")
print("注意: 如果文件不存在会报错")
print()

# 示例代码
try:
    # 先创建一个测试文件
    with open("test_file.txt", "w", encoding="utf-8") as f:
        f.write("这是一个测试文件")
    print("✅ 创建测试文件: test_file.txt")
    
    # 删除文件
    os.remove("test_file.txt")
    print("✅ 删除文件成功: test_file.txt")
    
    # 再次删除同一文件 - 会报错
    # os.remove("test_file.txt")  # FileNotFoundError
    
except FileNotFoundError as e:
    print(f"❌ 错误: {e}")
except Exception as e:
    print(f"❌ 其他错误: {e}")

print()

# ========== 2. 删除目录 ==========
print("2. 删除目录操作")
print("-" * 30)

# 方法一: os.rmdir() - 只能删除空目录
print("方法一: os.rmdir()")
print("作用: 删除空目录")
print("限制: 只能删除空目录，非空目录会报错")
print()

try:
    # 创建空目录
    os.makedirs("empty_dir", exist_ok=True)
    print("✅ 创建空目录: empty_dir")
    
    # 删除空目录
    os.rmdir("empty_dir")
    print("✅ 删除空目录成功: empty_dir")
    
    # 尝试删除非空目录 - 会报错
    os.makedirs("non_empty_dir/sub_dir", exist_ok=True)
    with open("non_empty_dir/test.txt", "w") as f:
        f.write("test")
    print("✅ 创建非空目录: non_empty_dir")
    
    # os.rmdir("non_empty_dir")  # OSError: 目录不为空
    
except OSError as e:
    print(f"❌ 目录操作错误: {e}")
except Exception as e:
    print(f"❌ 其他错误: {e}")

print()

# 方法二: os.removedirs() - 递归删除目录
print("方法二: os.removedirs()")
print("作用: 递归删除目录层次结构")
print("特点: 从最深层开始删除，逐层向上删除空目录")
print()

try:
    # 创建多层目录结构
    os.makedirs("level1/level2/level3", exist_ok=True)
    print("✅ 创建多层目录: level1/level2/level3")
    
    # 递归删除目录
    os.removedirs("level1/level2/level3")
    print("✅ 递归删除成功: 删除了 level3 -> level2 -> level1")
    
except OSError as e:
    print(f"❌ 目录删除错误: {e}")
except Exception as e:
    print(f"❌ 其他错误: {e}")

print()

# ========== 3. 安全删除函数 ==========
print("3. 安全删除函数")
print("-" * 30)

def safe_remove_file(filepath):
    """安全删除文件"""
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"✅ 文件删除成功: {filepath}")
            return True
        else:
            print(f"⚠️ 文件不存在: {filepath}")
            return False
    except Exception as e:
        print(f"❌ 删除文件失败: {e}")
        return False

def safe_remove_dir(dirpath):
    """安全删除空目录"""
    try:
        if os.path.exists(dirpath):
            os.rmdir(dirpath)
            print(f"✅ 目录删除成功: {dirpath}")
            return True
        else:
            print(f"⚠️ 目录不存在: {dirpath}")
            return False
    except OSError as e:
        print(f"❌ 删除目录失败: {e}")
        return False

# 使用安全删除函数
print("使用安全删除函数:")
safe_remove_file("non_existent_file.txt")
safe_remove_dir("non_existent_dir")

print()

# ========== 4. 实际应用示例 ==========
print("4. 实际应用示例")
print("-" * 30)

# 清理临时文件
def cleanup_temp_files():
    """清理临时文件示例"""
    temp_files = ["temp1.txt", "temp2.txt", "temp3.txt"]
    
    # 创建临时文件
    for file in temp_files:
        with open(file, "w") as f:
            f.write("临时文件内容")
    print(f"✅ 创建临时文件: {temp_files}")
    
    # 批量删除
    deleted_count = 0
    for file in temp_files:
        if safe_remove_file(file):
            deleted_count += 1
    
    print(f"✅ 清理完成，删除了 {deleted_count} 个临时文件")

cleanup_temp_files()

print()

# ========== 知识点总结 ==========
print("🎯 知识点总结:")
print("=" * 50)
print("1. os.remove(文件路径) - 删除文件")
print("   ⚠️ 文件不存在会报 FileNotFoundError")
print()
print("2. os.rmdir(目录路径) - 删除空目录")
print("   ⚠️ 非空目录会报 OSError")
print()
print("3. os.removedirs(目录路径) - 递归删除目录")
print("   📝 从最深层开始，逐层删除空目录")
print()
print("4. 安全原则:")
print("   - 删除前检查文件/目录是否存在")
print("   - 使用 try-except 处理异常")
print("   - 防止误删重要文件")
print()
print("5. 常见错误:")
print("   - FileNotFoundError: 文件不存在")
print("   - OSError: 目录不为空或权限不足")

# 清理演示用的目录
try:
    if os.path.exists("non_empty_dir"):
        os.remove("non_empty_dir/test.txt")
        os.rmdir("non_empty_dir")
        print("\n🧹 清理演示目录完成")
except:
    pass
