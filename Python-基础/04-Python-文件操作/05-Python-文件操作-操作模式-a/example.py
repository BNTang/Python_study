# -*- coding: utf-8 -*-

# @Time    : 2025-06-01
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 05-Python-文件操作-操作模式-a

"""
Python文件操作 - 'a'模式（追加模式）

'a'模式的三个特点：
1. 只写模式 - 不能读取文件内容
2. 文件不存在时自动创建
3. 文件指针默认指向文件末尾（追加写入）
"""

# ========== 'a'模式特点演示 ==========

print("=== Python文件操作 - 'a'模式演示 ===\n")

# 1. 演示文件不存在时自动创建
print("1. 测试文件自动创建功能")
try:
    # 打开一个不存在的文件，'a'模式会自动创建
    with open('a_test.txt', 'a', encoding='utf-8') as f:
        f.write('123456')
    print("✓ 文件 'a_test.txt' 自动创建成功")
except Exception as e:
    print(f"✗ 创建文件失败: {e}")

# 2. 演示'a'模式只写不能读
print("\n2. 测试'a'模式的只写特性")
try:
    with open('a_test.txt', 'a', encoding='utf-8') as f:
        # 尝试读取文件内容 - 这会报错
        content = f.read()
except Exception as e:
    print(f"✓ 验证成功：'a'模式不支持读取操作 - {e}")

# 3. 演示追加写入功能（指针指向文件末尾）
print("\n3. 测试追加写入功能")

# 首先查看当前文件内容
try:
    with open('a_test.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"文件当前内容: '{content}'")
except:
    print("无法读取文件内容")

# 使用'a'模式追加内容
try:
    with open('a_test.txt', 'a', encoding='utf-8') as f:
        f.write('ABCD')
    print("✓ 成功追加内容 'ABCD'")
except Exception as e:
    print(f"✗ 追加内容失败: {e}")

# 再次查看文件内容
try:
    with open('a_test.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"追加后文件内容: '{content}'")
except:
    print("无法读取文件内容")

# ========== 'a'模式与'w'模式对比 ==========

print("\n=== 'a'模式与'w'模式对比 ===")

# 创建测试文件
with open('compare_test.txt', 'w', encoding='utf-8') as f:
    f.write('原始内容')

print("原始文件内容: '原始内容'")

# 使用'w'模式写入
with open('compare_test.txt', 'w', encoding='utf-8') as f:
    f.write('w模式内容')

with open('compare_test.txt', 'r', encoding='utf-8') as f:
    content = f.read()
print(f"'w'模式写入后: '{content}' (覆盖原内容)")

# 重新写入原始内容
with open('compare_test.txt', 'w', encoding='utf-8') as f:
    f.write('原始内容')

# 使用'a'模式写入
with open('compare_test.txt', 'a', encoding='utf-8') as f:
    f.write('a模式内容')

with open('compare_test.txt', 'r', encoding='utf-8') as f:
    content = f.read()
print(f"'a'模式写入后: '{content}' (追加到原内容)")

# ========== 实际应用场景 ==========

print("\n=== 'a'模式实际应用场景 ===")

# 日志文件追加
def write_log(message):
    """向日志文件追加消息"""
    with open('app.log', 'a', encoding='utf-8') as f:
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'[{timestamp}] {message}\n')

# 示例：记录多条日志
write_log('应用程序启动')
write_log('用户登录成功')
write_log('数据处理完成')

print("✓ 日志记录完成，查看 'app.log' 文件")

# ========== 注意事项 ==========

print("\n=== 'a'模式使用注意事项 ===")
print("1. 'a'模式只能写入，不能读取")
print("2. 文件指针始终在文件末尾，无法移动到其他位置")
print("3. 非常适合日志记录、数据追加等场景")
print("4. 如果需要既读又写，可以考虑'a+'模式")

# 清理测试文件（可选）
import os
try:
    os.remove('a_test.txt')
    os.remove('compare_test.txt')
    print("\n清理测试文件完成")
except:
    pass

print("\n=== 'a'模式演示结束 ===")
