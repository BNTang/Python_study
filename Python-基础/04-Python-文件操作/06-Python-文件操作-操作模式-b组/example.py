# -*- coding: utf-8 -*-

# @Time    : 2025-06-01
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 06-Python-文件操作-操作模式-b组

"""
【重点知识】Python文件操作 - 二进制模式(b组)

文件操作模式分类：
1. 文本模式：r, w, a
2. 二进制模式：rb, wb, ab  ← 本节重点

核心要点：
- 'b' 表示以二进制格式操作文件
- 用于处理图片、视频、音频等二进制文件
- 读取结果是bytes类型，不是str类型
"""

print("=== Python文件操作-二进制模式演示 ===\n")

# ==================== 知识点1：二进制模式的三种类型 ====================
print("1. 二进制模式类型：")
print("   - rb：以二进制模式读取文件")
print("   - wb：以二进制模式写入文件（覆盖）")
print("   - ab：以二进制模式追加文件\n")

# ==================== 知识点2：实际案例 - 图片文件操作 ====================
print("2. 实际案例：复制图片的前半部分")

# 步骤说明
print("\n操作步骤：")
print("   1.1 打开原图片文件（rb模式）")
print("   1.2 读取文件内容")
print("   1.3 关闭原文件")
print("   2.1 打开目标文件（wb模式）")
print("   2.2 写入前半部分内容")
print("   2.3 关闭目标文件\n")

try:
    # ============ 第一步：读取原图片文件 ============
    print("正在读取原图片文件...")
    
    # 1.1 打开文件 - 使用rb模式（二进制读取）
    with open("xxx.jpg", "rb") as from_file:
        # 1.2 读取文件内容（二进制数据）
        from_content = from_file.read()
        print(f"   原文件大小: {len(from_content)} 字节")
        print(f"   数据类型: {type(from_content)}")
        print(f"   前20字节: {from_content[:20]}")
    # 1.3 文件自动关闭（使用with语句）
    
    # ============ 第二步：写入到新图片文件 ============
    print("\n正在写入新图片文件...")
    
    # 计算前半部分的大小
    half_size = len(from_content) // 2
    write_content = from_content[:half_size]
    
    # 2.1 打开目标文件 - 使用wb模式（二进制写入）
    with open("xxx2.jpg", "wb") as to_file:
        # 2.2 写入前半部分内容
        to_file.write(write_content)
        print(f"   写入文件大小: {len(write_content)} 字节")
    # 2.3 文件自动关闭
    
    print("✅ 图片前半部分复制完成！")
    
except FileNotFoundError:
    print("❌ 错误：找不到xxx.jpg文件")
    print("📝 解决方案：请确保当前目录下有xxx.jpg文件")
except Exception as e:
    print(f"❌ 发生错误：{e}")

# ==================== 知识点3：常见错误对比 ====================
print("\n3. 常见错误对比：")
print("❌ 错误写法：")
print("   with open('image.jpg', 'r') as f:  # 文本模式读取二进制文件")
print("   ↳ 报错：UnicodeDecodeError")
print()
print("✅ 正确写法：")
print("   with open('image.jpg', 'rb') as f:  # 二进制模式读取二进制文件")
print("   ↳ 返回bytes对象")

# ==================== 知识点4：使用场景总结 ====================
print("\n4. 使用场景总结：")
scenarios = {
    "文本文件": ["txt", "py", "html", "css", "js"],
    "二进制文件": ["jpg", "png", "mp4", "mp3", "exe", "zip"]
}

for file_type, extensions in scenarios.items():
    mode = "r/w/a" if file_type == "文本文件" else "rb/wb/ab + b模式"
    print(f"   {file_type}: {', '.join(extensions)} → 使用 {mode}")

print("\n" + "="*50)
print("🎯 学习要点：")
print("1. 二进制文件必须使用带'b'的模式")
print("2. 读取结果是bytes类型，不是str类型")
print("3. 图片、视频、音频都是二进制文件")
print("4. 使用with语句可以自动关闭文件")
print("="*50)
