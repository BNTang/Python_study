# -*- coding: utf-8 -*-

# @Time    : 2025-06-03
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 15-Python-文件操作-其他操作-重命名

"""
文件操作 - 重命名操作详解
重点学习：os.rename() 和 os.renames() 的区别和使用
"""

import os

# ========== 重命名操作核心知识点 ==========

"""
⭐⭐ 重命名操作重点 ⭐⭐

1️⃣ os.rename(src, dst) - 基础重命名
   • src: 源文件/目录名
   • dst: 目标文件/目录名
   • 只能重命名单个文件或目录
   • 目标路径的父目录必须存在

2️⃣ os.renames(src, dst) - 递归重命名  
   • 可以创建不存在的中间目录
   • 按树状结构逐层修改
   • 更强大但需谨慎使用
"""

# ========== 1. 文件重命名演示 ==========

def file_rename_demo():
    """文件重命名基础操作"""
    print("=== 1. 文件重命名演示 ===")
    
    # 创建测试文件
    original_file = "test_file.txt"
    new_file = "renamed_file.txt"
    
    # 先创建原始文件
    with open(original_file, 'w', encoding='utf-8') as f:
        f.write("这是测试文件内容\n文件重命名测试")
    print(f"✅ 创建原始文件: {original_file}")
    
    try:
        # 重命名文件
        os.rename(original_file, new_file)
        print(f"✅ 文件重命名成功: {original_file} → {new_file}")
        
        # 验证文件内容是否保持不变
        with open(new_file, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"📄 重命名后文件内容: {content}")
            
    except FileNotFoundError:
        print(f"❌ 源文件不存在: {original_file}")
    except FileExistsError:
        print(f"❌ 目标文件已存在: {new_file}")
    except Exception as e:
        print(f"❌ 重命名失败: {e}")

# ========== 2. 目录重命名演示 ==========

def directory_rename_demo():
    """目录重命名操作"""
    print("\n=== 2. 目录重命名演示 ===")
    
    original_dir = "first"
    new_dir = "one"
    
    # 创建测试目录
    if not os.path.exists(original_dir):
        os.makedirs(original_dir)
        print(f"✅ 创建原始目录: {original_dir}")
    
    # 在目录中创建测试文件
    test_file_path = os.path.join(original_dir, "test.txt")
    with open(test_file_path, 'w', encoding='utf-8') as f:
        f.write("目录中的测试文件")
    print(f"✅ 在目录中创建文件: {test_file_path}")
    
    try:
        # 重命名目录
        os.rename(original_dir, new_dir)
        print(f"✅ 目录重命名成功: {original_dir} → {new_dir}")
        
        # 验证目录中的文件是否仍然存在
        new_file_path = os.path.join(new_dir, "test.txt")
        if os.path.exists(new_file_path):
            print(f"✅ 目录中的文件仍然存在: {new_file_path}")
            
    except Exception as e:
        print(f"❌ 目录重命名失败: {e}")

# ========== 3. os.rename() 局限性演示 ==========

def rename_limitation_demo():
    """演示 os.rename() 的局限性"""
    print("\n=== 3. os.rename() 局限性演示 ===")
    
    # 创建测试目录和文件
    os.makedirs("one", exist_ok=True)
    test_file = os.path.join("one", "one.txt")
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("测试文件内容")
    print(f"✅ 创建测试结构: one/one.txt")
    
    try:
        # 尝试重命名到不存在的目录路径
        # 这会失败，因为 'two' 目录不存在
        os.rename("one/one.txt", "two/two.txt")
        print("✅ 重命名成功")
        
    except FileNotFoundError as e:
        print(f"❌ os.rename() 失败: {e}")
        print("🔍 原因: 目标路径的父目录 'two' 不存在")
        print("💡 解决方案: 使用 os.renames() 或先创建父目录")

# ========== 4. os.renames() 强大功能演示 ==========

def renames_advanced_demo():
    """演示 os.renames() 的强大功能"""
    print("\n=== 4. os.renames() 强大功能演示 ===")
    
    # 确保测试环境
    if os.path.exists("two"):
        import shutil
        shutil.rmtree("two")
    
    try:
        # 使用 os.renames() 进行多级重命名
        # 它会自动创建不存在的中间目录
        os.renames("one/one.txt", "two/two.txt")
        print("✅ os.renames() 重命名成功!")
        print("🎯 功能说明:")
        print("   • 自动将 'one' 目录重命名为 'two'")
        print("   • 自动将 'one.txt' 重命名为 'two.txt'")
        print("   • 按树状结构逐层处理")
        
        # 验证结果
        if os.path.exists("two/two.txt"):
            print("✅ 验证: 新文件路径存在")
            with open("two/two.txt", 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"📄 文件内容: {content}")
        
        if not os.path.exists("one"):
            print("✅ 验证: 原目录已被重命名")
            
    except Exception as e:
        print(f"❌ os.renames() 失败: {e}")

# ========== 5. 实用的重命名函数封装 ==========

def safe_rename(src, dst, create_dirs=False):
    """安全的重命名函数
    
    Args:
        src: 源路径
        dst: 目标路径  
        create_dirs: 是否创建中间目录
    """
    try:
        if create_dirs:
            # 创建目标目录的父目录
            dst_dir = os.path.dirname(dst)
            if dst_dir and not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
                print(f"✅ 创建目录: {dst_dir}")
            
            os.rename(src, dst)
        else:
            os.rename(src, dst)
            
        print(f"✅ 重命名成功: {src} → {dst}")
        return True
        
    except FileNotFoundError:
        print(f"❌ 源文件/目录不存在: {src}")
        return False
    except FileExistsError:
        print(f"❌ 目标文件/目录已存在: {dst}")
        return False
    except Exception as e:
        print(f"❌ 重命名失败: {e}")
        return False

def batch_rename_demo():
    """批量重命名演示"""
    print("\n=== 5. 批量重命名演示 ===")
    
    # 创建多个测试文件
    test_files = ["file1.txt", "file2.txt", "file3.txt"]
    for file in test_files:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(f"内容: {file}")
        print(f"✅ 创建文件: {file}")
    
    # 批量重命名（添加前缀）
    print("\n📝 批量添加前缀 'new_':")
    for file in test_files:
        new_name = f"new_{file}"
        safe_rename(file, new_name)

# ========== 6. 注意事项和最佳实践 ==========

def best_practices():
    """重命名操作的最佳实践"""
    print("\n=== 6. 重命名最佳实践 ===")
    print("📋 重要注意事项:")
    print("1️⃣ 重命名前检查源文件/目录是否存在")
    print("2️⃣ 检查目标文件/目录是否已存在，避免覆盖")
    print("3️⃣ 使用异常处理确保程序稳定性")
    print("4️⃣ 跨平台考虑：注意路径分隔符")
    print("5️⃣ 权限问题：确保有足够的文件系统权限")
    
    print("\n🔧 函数选择指南:")
    print("• os.rename():   简单重命名，目标目录必须存在")
    print("• os.renames():  复杂重命名，可创建中间目录")
    print("• 推荐使用 os.rename() + 手动创建目录的方式")

# ========== 清理测试文件 ==========

def cleanup_test_files():
    """清理演示过程中创建的测试文件"""
    print("\n=== 清理测试文件 ===")
    
    # 要清理的文件和目录列表
    cleanup_items = [
        "renamed_file.txt", "new_file1.txt", "new_file2.txt", "new_file3.txt",
        "one", "two"
    ]
    
    import shutil
    for item in cleanup_items:
        try:
            if os.path.isfile(item):
                os.remove(item)
                print(f"🗑️ 删除文件: {item}")
            elif os.path.isdir(item):
                shutil.rmtree(item)
                print(f"🗑️ 删除目录: {item}")
        except Exception as e:
            print(f"⚠️ 清理失败 {item}: {e}")

# ========== 重点总结 ==========

def summary():
    """重点知识总结"""
    print("\n" + "="*60)
    print("📚 重点知识总结")
    print("="*60)
    print("🎯 核心概念:")
    print("   • 重命名操作使用 os 模块")
    print("   • 重命名 = 移动 + 改名")
    print("   • 文件内容不会改变，只改变路径/名称")
    print()
    print("🔧 两个重要函数:")
    print("   os.rename(src, dst):")
    print("   ├─ 基础重命名功能")
    print("   ├─ 目标目录必须存在") 
    print("   └─ 适合简单重命名操作")
    print()
    print("   os.renames(src, dst):")
    print("   ├─ 高级重命名功能")
    print("   ├─ 自动创建中间目录")
    print("   └─ 按树状结构逐层处理")
    print()
    print("⚠️ 注意事项:")
    print("   • 权限检查")
    print("   • 异常处理")  
    print("   • 避免覆盖重要文件")
    print("   • 跨平台路径兼容性")
    print("="*60)

# ========== 主程序 ==========

if __name__ == "__main__":
    print("🎯 Python文件操作 - 重命名操作详解")
    print("="*60)
    
    # 执行所有演示
    file_rename_demo()
    directory_rename_demo()
    rename_limitation_demo()
    renames_advanced_demo()
    batch_rename_demo()
    best_practices()
    
    # 清理测试文件
    cleanup_test_files()
    
    # 总结
    summary()
    
    print("\n✨ 学习完成！掌握了文件和目录的重命名操作！")
