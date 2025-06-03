# -*- coding: utf-8 -*-

# @Time    : 2025-06-03
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 14-Python-文件操作-关闭

"""
文件操作的三个步骤：
1. 打开文件 (open)
2. 读写文件 (read/write)
3. 关闭文件 (close) ⭐重点⭐
"""

# ========== 关闭文件的两大重要原因 ==========

"""
❗❗ 为什么必须关闭文件？❗❗

1️⃣ 释放系统资源
   - 每个打开的文件都会占用系统资源（类似分配一只手去拿麻袋）
   - 如果不关闭，资源会一直被占用
   - 关闭后可以释放这些资源给其他程序使用

2️⃣ 立即清空缓冲区数据到磁盘
   - 写入操作不会立即写入文件，而是先放到缓冲区
   - 缓冲区满了或达到特定条件才会真正写入磁盘
   - 关闭文件会强制清空缓冲区，避免数据丢失
"""

# ========== 缓冲区机制演示 ==========

def demonstrate_buffer_mechanism():
    """演示缓冲区机制"""
    print("=== 缓冲区机制演示 ===")
    
    # 创建测试文件
    filename = "test_buffer.txt"
    
    # 1. 不使用flush()的情况
    print("1. 写入数据但不立即flush...")
    f = open(filename, 'w', encoding='utf-8')
    f.write("ABC")  # 这个数据会先放在缓冲区，不会立即写入文件
    
    # 此时查看文件，可能看不到内容（因为还在缓冲区）
    print("   数据写入缓冲区，但可能还未写入文件")
    
    # 2. 使用flush()强制刷新缓冲区
    print("2. 使用flush()强制刷新缓冲区...")
    f.write("123")
    f.flush()  # ⭐立即清空缓冲区到文件⭐
    print("   现在数据已经强制写入文件")
    
    f.close()  # 关闭文件也会自动清空缓冲区
    print("3. 文件已关闭，所有数据确保写入")

# ========== 标准文件操作流程 ==========

def standard_file_operations():
    """标准的文件操作流程"""
    print("\n=== 标准文件操作流程 ===")
    
    filename = "example.txt"
    
    # ✅ 正确的文件操作方式
    try:
        # 步骤1: 打开文件
        f = open(filename, 'w', encoding='utf-8')
        print("✅ 文件已打开")
        
        # 步骤2: 读写操作
        f.write("Hello World!\n")
        f.write("Python文件操作\n")
        f.write("记得关闭文件！")
        print("✅ 数据写入完成")
        
        # 步骤3: 关闭文件 ⭐⭐⭐
        f.close()
        print("✅ 文件已关闭")
        
    except Exception as e:
        print(f"❌ 操作失败: {e}")

# ========== with语句自动关闭文件 ==========

def with_statement_demo():
    """使用with语句自动管理文件关闭"""
    print("\n=== with语句自动关闭文件 ===")
    
    # 推荐方式：使用with语句
    filename = "auto_close.txt"
    
    # with语句会自动关闭文件，即使出现异常也会关闭
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("使用with语句\n")
        f.write("自动管理文件关闭\n")
        f.write("更加安全和简洁")
        print("✅ 数据写入完成")
    # 文件在这里自动关闭，无需手动调用close()
    print("✅ 文件自动关闭")

# ========== flush()方法详解 ==========

def flush_method_demo():
    """flush()方法使用演示"""
    print("\n=== flush()方法演示 ===")
    
    filename = "flush_demo.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        # 写入数据到缓冲区
        f.write("第一行数据\n")
        print("写入第一行（在缓冲区）")
        
        # 立即刷新到磁盘
        f.flush()  # ⭐强制将缓冲区数据写入磁盘⭐
        print("✅ 第一行已刷新到磁盘")
        
        f.write("第二行数据\n")
        f.write("第三行数据\n")
        print("写入第二、三行（在缓冲区）")
        
        # 文件关闭时会自动刷新剩余缓冲区数据
    print("✅ 文件关闭，剩余数据自动刷新到磁盘")

# ========== 错误示例：忘记关闭文件 ==========

def bad_example():
    """❌ 错误示例：忘记关闭文件"""
    print("\n=== ❌ 错误示例 ===")
    
    # 不推荐的方式
    f = open("bad_example.txt", 'w', encoding='utf-8')
    f.write("这个文件可能不会被正确关闭")
    # 忘记调用 f.close() 
    # 可能导致：
    # 1. 数据丢失（缓冲区数据未写入）
    # 2. 资源泄露（文件句柄未释放）
    print("❌ 忘记关闭文件，可能导致数据丢失和资源泄露")

# ========== 重点总结 ==========

def summary():
    """重点知识总结"""
    print("\n" + "="*50)
    print("📚 重点知识总结")
    print("="*50)
    print("1️⃣  文件操作三步骤：打开 → 读写 → 关闭")
    print("2️⃣  必须关闭文件的原因：")
    print("   • 释放系统资源")
    print("   • 清空缓冲区数据到磁盘")
    print("3️⃣  缓冲区机制：")
    print("   • 写入数据先放缓冲区，不立即写磁盘")
    print("   • 提升IO性能，减少磁盘读写次数")
    print("4️⃣  flush()方法：立即清空缓冲区到磁盘")
    print("5️⃣  推荐使用with语句自动管理文件关闭")
    print("="*50)

# ========== 主程序 ==========

if __name__ == "__main__":
    print("🎯 Python文件操作 - 关闭文件的重要性")
    print("="*60)
    
    # 演示各种情况
    demonstrate_buffer_mechanism()
    standard_file_operations()
    with_statement_demo()
    flush_method_demo()
    bad_example()
    summary()
    
    print("\n✨ 学习完成！记住：文件操作后必须关闭文件！")
