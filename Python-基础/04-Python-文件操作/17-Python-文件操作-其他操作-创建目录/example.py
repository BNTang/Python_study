# -*- coding: utf-8 -*-

# @Time    : 2025-06-03
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 17-Python-文件操作-其他操作-创建目录

import os

# ========== 核心知识点 =========
# os.mkdir() - 创建单级目录
# 语法: os.mkdir(path, mode=0o777)
# 注意: 只能创建一级目录，不支持多级目录创建

print("=" * 50)
print("Python 文件操作 - 创建目录 (os.mkdir)")
print("=" * 50)

# 1. 基本用法 - 创建单个目录
print("\n1. 创建单个目录:")
try:
    os.mkdir("a")
    print("✓ 成功创建目录 'a'")
except FileExistsError:
    print("⚠ 目录 'a' 已存在")
except Exception as e:
    print(f"✗ 创建失败: {e}")

# 2. 尝试创建多级目录 (会失败)
print("\n2. 尝试创建多级目录 (演示错误):")
try:
    os.mkdir("b/c/d")  # 这会失败
    print("✓ 成功创建多级目录")
except FileNotFoundError:
    print("✗ 失败: 无法创建多级目录，父目录不存在")
except Exception as e:
    print(f"✗ 创建失败: {e}")

# 3. 重复创建已存在的目录 (会失败)
print("\n3. 重复创建已存在目录 (演示错误):")
try:
    os.mkdir("a")  # 目录已存在
    print("✓ 成功创建目录")
except FileExistsError:
    print("✗ 失败: 目录已存在，无法重复创建")

# 4. 使用 mode 参数设置权限
print("\n4. 创建目录并设置权限:")
try:
    # mode 参数：数字模式权限 (八进制)
    # 格式：0o + 三位数字
    # 每位数字表示：拥有者、同组用户、其他用户的权限
    # 权限值：4(读) + 2(写) + 1(执行) = 7(全部权限)
    os.mkdir("b", mode=0o777)  # 所有用户都有读写执行权限
    print("✓ 成功创建目录 'b'，权限：0o777")
except FileExistsError:
    print("⚠ 目录 'b' 已存在")
except Exception as e:
    print(f"✗ 创建失败: {e}")

# ========== 权限模式详解 =========
print("\n" + "=" * 50)
print("权限模式 (mode) 详解")
print("=" * 50)

permission_examples = [
    ("0o755", "拥有者: 读写执行(7), 其他: 读执行(5)"),
    ("0o644", "拥有者: 读写(6), 其他: 只读(4)"),
    ("0o777", "所有用户: 读写执行(7)"),
    ("0o700", "仅拥有者: 读写执行(7), 其他: 无权限(0)")
]

print("\n数字权限说明:")
print("• 4 = 读权限 (read)")
print("• 2 = 写权限 (write)")  
print("• 1 = 执行权限 (execute)")
print("• 7 = 4+2+1 = 读写执行")
print("• 6 = 4+2 = 读写")
print("• 5 = 4+1 = 读执行")
print("• 4 = 只读")

print("\n常用权限模式:")
for mode, description in permission_examples:
    print(f"• {mode}: {description}")

# ========== 实用函数封装 =========
print("\n" + "=" * 50)
print("实用函数示例")
print("=" * 50)

def safe_mkdir(path, mode=0o777):
    """
    安全创建目录函数
    """
    try:
        os.mkdir(path, mode)
        print(f"✓ 成功创建目录: {path}")
        return True
    except FileExistsError:
        print(f"⚠ 目录已存在: {path}")
        return False
    except FileNotFoundError:
        print(f"✗ 父目录不存在: {path}")
        return False
    except PermissionError:
        print(f"✗ 权限不足: {path}")
        return False
    except Exception as e:
        print(f"✗ 创建失败: {path}, 错误: {e}")
        return False

# 测试安全创建函数
print("\n5. 使用安全创建函数:")
test_dirs = ["test1", "test2", "nonexistent/test3"]
for dir_name in test_dirs:
    safe_mkdir(dir_name)

# ========== 清理测试目录 =========
print("\n" + "=" * 50)
print("清理测试目录")
print("=" * 50)

def cleanup_test_dirs():
    """清理创建的测试目录"""
    test_dirs = ["a", "b", "test1", "test2"]
    for dir_name in test_dirs:
        try:
            if os.path.exists(dir_name):
                os.rmdir(dir_name)
                print(f"✓ 已删除目录: {dir_name}")
        except Exception as e:
            print(f"✗ 删除失败: {dir_name}, 错误: {e}")

# 取消注释下面这行来清理测试目录
# cleanup_test_dirs()

print("\n" + "=" * 50)
print("总结")
print("=" * 50)
print("• os.mkdir() 只能创建单级目录")
print("• 创建多级目录需要使用 os.makedirs()")
print("• mode 参数用于设置目录权限 (Unix/Linux)")
print("• 在 Windows 系统中 mode 参数通常被忽略")
print("• 建议使用异常处理来应对各种错误情况")
