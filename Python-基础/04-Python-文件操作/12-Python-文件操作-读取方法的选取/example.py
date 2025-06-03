# -*- coding: utf-8 -*-

# @Time    : 2025-06-03
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 12-Python-文件操作-读取方法的选取

"""
Python文件读取方法选择指南
===========================

四种主要的文件读取方法及其特点：
1. read() - 一次性读取全部内容
2. readlines() - 一次性读取所有行到列表
3. readline() - 逐行读取
4. for循环遍历 - 迭代器方式逐行读取
"""

# 创建示例文件用于演示
def create_sample_file():
    """创建示例文件"""
    with open('sample.txt', 'w', encoding='utf-8') as f:
        for i in range(5):
            f.write(f"这是第{i+1}行内容\n")

# 方法1: read() - 一次性读取全部内容
def method_read():
    """
    read()方法特点：
    - 一次性读取整个文件内容到内存
    - 内存消耗大，适合小文件
    - 处理速度快（数据已在内存中）
    """
    print("=== 方法1: read() ===")
    with open('sample.txt', 'r', encoding='utf-8') as f:
        content = f.read()  # 一次性读取全部内容
        print("读取结果:")
        print(repr(content))
        print(f"内容类型: {type(content)}")

# 方法2: readlines() - 一次性读取所有行
def method_readlines():
    """
    readlines()方法特点：
    - 一次性读取所有行到列表
    - 内存消耗大，适合小文件
    - 便于按行处理数据
    """
    print("\n=== 方法2: readlines() ===")
    with open('sample.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()  # 一次性读取所有行
        print("读取结果:")
        for i, line in enumerate(lines):
            print(f"第{i+1}行: {repr(line)}")
        print(f"内容类型: {type(lines)}")

# 方法3: readline() - 逐行读取
def method_readline():
    """
    readline()方法特点：
    - 每次只读取一行
    - 内存友好，适合大文件
    - 需要循环控制读取过程
    """
    print("\n=== 方法3: readline() ===")
    with open('sample.txt', 'r', encoding='utf-8') as f:
        line_num = 1
        while True:
            line = f.readline()  # 每次读取一行
            if not line:  # 文件结束
                break
            print(f"第{line_num}行: {repr(line)}")
            line_num += 1

# 方法4: for循环遍历文件对象
def method_for_loop():
    """
    for循环遍历特点：
    - 文件对象本身是迭代器
    - 自动逐行读取，内存友好
    - 代码简洁，适合大文件
    - 推荐用于大文件处理
    """
    print("\n=== 方法4: for循环遍历 ===")
    with open('sample.txt', 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):  # f本身就是迭代器
            print(f"第{line_num}行: {repr(line)}")

# 性能和内存对比演示
def performance_comparison():
    """
    性能和内存使用对比
    """
    print("\n" + "="*50)
    print("性能和内存使用特点总结:")
    print("="*50)
    
    print("高内存消耗方法 (适合小文件):")
    print("├─ read()      : 一次性加载全部内容，处理速度快")
    print("└─ readlines() : 一次性加载所有行，便于索引访问")
    
    print("\n低内存消耗方法 (适合大文件):")
    print("├─ readline()  : 手动控制逐行读取")
    print("└─ for循环     : 自动逐行读取，代码最简洁")

# 使用场景建议
def usage_recommendations():
    """
    使用场景建议
    """
    print("\n" + "="*50)
    print("使用场景建议:")
    print("="*50)
    
    scenarios = [
        ("小文件 + 追求处理速度", "read() 或 readlines()"),
        ("大文件 + 内存有限", "for循环遍历 (推荐)"),
        ("大文件 + 需要精确控制", "readline()"),
        ("日志文件分析", "for循环遍历"),
        ("配置文件读取", "readlines()"),
        ("超大数据文件", "for循环遍历")
    ]
    
    for scenario, method in scenarios:
        print(f"• {scenario:<20} → {method}")

# 实际应用示例
def practical_examples():
    """
    实际应用示例
    """
    print("\n" + "="*50)
    print("实际应用示例:")
    print("="*50)
    
    # 示例1: 小配置文件 - 使用readlines()
    print("\n示例1: 读取配置文件 (小文件)")
    config_content = ["username=admin\n", "password=123456\n", "port=8080\n"]
    with open('config.txt', 'w', encoding='utf-8') as f:
        f.writelines(config_content)
    
    with open('config.txt', 'r', encoding='utf-8') as f:
        config_lines = f.readlines()  # 适合小配置文件
        for line in config_lines:
            if '=' in line:
                key, value = line.strip().split('=')
                print(f"配置项: {key} = {value}")
    
    # 示例2: 大日志文件 - 使用for循环
    print("\n示例2: 处理日志文件 (大文件)")
    # 模拟大日志文件
    with open('large_log.txt', 'w', encoding='utf-8') as f:
        for i in range(1000):
            f.write(f"2024-01-01 10:{i:02d}:00 INFO: 处理请求 {i}\n")
    
    error_count = 0
    with open('large_log.txt', 'r', encoding='utf-8') as f:
        for line in f:  # 内存友好的方式处理大文件
            if 'ERROR' in line:
                error_count += 1
    print(f"错误日志统计: {error_count} 条")

# 主函数
def main():
    """主函数 - 演示所有读取方法"""
    print("Python文件读取方法选择演示")
    print("="*50)
    
    # 创建示例文件
    create_sample_file()
    
    # 演示四种读取方法
    method_read()
    method_readlines()
    method_readline()
    method_for_loop()
    
    # 性能对比和建议
    performance_comparison()
    usage_recommendations()
    practical_examples()
    
    print("\n" + "="*50)
    print("总结:")
    print("• 小文件或需要高速处理: 使用 read() 或 readlines()")
    print("• 大文件或内存限制: 使用 for循环遍历 (推荐)")
    print("• 需要精确控制: 使用 readline()")
    print("="*50)

if __name__ == "__main__":
    main()
