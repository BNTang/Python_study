# -*- coding: utf-8 -*-

# @Time    : 2025-06-04
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 20-Python-文件操作-案例1-文件复制-大文件注意

"""
文件复制案例 - 大文件处理注意事项

核心知识点：
1. 文件复制的三个步骤：打开文件 -> 读写数据 -> 关闭文件
2. 大文件处理：分块读取，避免内存溢出
3. 文件指针自动移动机制
"""

def copy_file_unsafe(source_path, target_path):
    """
    不安全的文件复制方法 - 一次性读取所有内容
    问题：大文件会导致内存溢出
    """
    print("=== 不安全的复制方法（仅用于演示问题） ===")
    
    # 第一步：打开文件
    source_file = open(source_path, 'r', encoding='utf-8')  # 只读模式
    target_file = open(target_path, 'w', encoding='utf-8')  # 写入模式
    
    # 第二步：一次性读取所有内容（危险！）
    # content = source_file.read()  # 大文件会导致内存不足
    # target_file.write(content)
    
    print("警告：此方法对大文件不安全，已注释掉危险代码")
    
    # 第三步：关闭文件
    source_file.close()
    target_file.close()

def copy_file_safe(source_path, target_path, chunk_size=1024):
    """
    安全的文件复制方法 - 分块读取
    参数：
    - source_path: 源文件路径
    - target_path: 目标文件路径  
    - chunk_size: 每次读取的字节数（默认1024字节=1KB）
    """
    print(f"=== 安全的复制方法（每次读取{chunk_size}字节） ===")
    
    try:
        # 第一步：打开两个文件
        with open(source_path, 'r', encoding='utf-8') as source_file, \
             open(target_path, 'w', encoding='utf-8') as target_file:
            
            print("文件已打开，开始复制...")
            copied_chunks = 0
            
            # 第二步：循环读取和写入
            while True:
                # 从当前文件指针位置读取指定字节数
                content = source_file.read(chunk_size)
                
                # 关键判断：如果读取的内容长度为0，说明文件读完了
                if len(content) == 0:
                    print("文件读取完毕，跳出循环")
                    break
                
                # 将读取的内容写入目标文件
                target_file.write(content)
                copied_chunks += 1
                
                # 显示进度（可选）
                if copied_chunks % 100 == 0:
                    print(f"已复制 {copied_chunks} 个数据块...")
            
            print(f"复制完成！总共处理了 {copied_chunks} 个数据块")
            
    except FileNotFoundError:
        print(f"错误：找不到源文件 {source_path}")
    except PermissionError:
        print(f"错误：没有权限访问文件")
    except Exception as e:
        print(f"复制过程中发生错误：{e}")

def demo_file_pointer():
    """
    演示文件指针的自动移动机制
    """
    print("\n=== 文件指针移动演示 ===")
    
    # 创建一个测试文件
    test_content = "0123456789ABCDEFGHIJ"
    with open("test_pointer.txt", 'w') as f:
        f.write(test_content)
    
    # 演示分块读取时指针的移动
    with open("test_pointer.txt", 'r') as f:
        chunk_size = 5
        position = 0
        
        while True:
            content = f.read(chunk_size)
            if len(content) == 0:
                break
            
            print(f"位置 {position:2d}-{position+len(content)-1:2d}: '{content}'")
            position += len(content)
    
    # 清理测试文件
    import os
    os.remove("test_pointer.txt")

def main():
    """
    主函数 - 演示文件复制的各种方法
    """
    print("Python 文件复制案例 - 大文件处理")
    print("=" * 50)
    
    # 创建一个示例源文件
    source_file = "source_example.txt"
    target_file = "target_copy.txt"
    
    # 创建源文件内容
    with open(source_file, 'w', encoding='utf-8') as f:
        f.write("这是一个示例文件。\n" * 1000)  # 创建较大的文件用于测试
        f.write("文件复制测试内容\n")
        f.write("Python 文件操作学习\n")
    
    print(f"已创建源文件：{source_file}")
    
    # 演示不安全的方法（仅说明问题）
    copy_file_unsafe(source_file, target_file)
    
    # 演示安全的方法
    copy_file_safe(source_file, target_file, chunk_size=1024)
    
    # 验证复制结果
    try:
        with open(source_file, 'r', encoding='utf-8') as sf, \
             open(target_file, 'r', encoding='utf-8') as tf:
            source_content = sf.read()
            target_content = tf.read()
            
            if source_content == target_content:
                print("✅ 文件复制成功！内容完全一致")
            else:
                print("❌ 文件复制失败！内容不一致")
                
    except Exception as e:
        print(f"验证过程出错：{e}")
    
    # 演示文件指针机制
    demo_file_pointer()
    
    print("\n" + "=" * 50)
    print("学习要点总结：")
    print("1. 大文件复制要分块读取，避免内存溢出")
    print("2. 使用 while True + break 处理未知循环次数")
    print("3. 文件指针会自动移动，无需手动管理")
    print("4. 使用 with 语句自动管理文件资源")
    print("5. 添加异常处理提高程序健壮性")

if __name__ == "__main__":
    main()
