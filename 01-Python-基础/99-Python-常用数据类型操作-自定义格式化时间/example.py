# -*- coding: utf-8 -*-

# @Time    : 2025-5-25
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 99-Python-常用数据类型操作-自定义格式化时间

import time

print("=== Python时间格式化操作示例 ===")

# 1. 获取当前时间的时间元组
current_time = time.localtime()
print(f"当前时间元组: {current_time}")

# 2. 使用strftime函数进行自定义格式化
# strftime(格式对象, 时间元组)
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print(f"格式化后的时间: {formatted_time}")

# 3. 常用格式符说明
print("\n=== 常用时间格式符 ===")
print("格式符说明:")
print("%y - 两位年份 (如: 25)")
print("%Y - 四位年份 (如: 2025)")
print("%m - 月份 (01-12)")
print("%d - 日期 (01-31)")
print("%H - 24小时制小时 (00-23)")
print("%I - 12小时制小时 (01-12)")
print("%M - 分钟 (00-59)")
print("%S - 秒钟 (00-59)")

# 4. 不同格式的示例
print("\n=== 不同格式示例 ===")
print(f"两位年份格式: {time.strftime('%y-%m-%d', current_time)}")
print(f"四位年份格式: {time.strftime('%Y/%m/%d', current_time)}")
print(f"12小时制时间: {time.strftime('%Y-%m-%d %I:%M:%S %p', current_time)}")
print(f"中文格式: {time.strftime('%Y年%m月%d日 %H时%M分%S秒', current_time)}")

# 5. 使用strptime函数：格式化日期字符串转回时间元组
print("\n=== strptime函数使用示例 ===")
date_string = "2025-05-25 14:30:45"
print(f"日期字符串: {date_string}")

# strptime(日期字符串, 格式字符串)
parsed_time = time.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"解析后的时间元组: {parsed_time}")

# 6. 时间格式化与解析的相互转换演示
print("\n=== 相互转换演示 ===")
# 步骤1: 时间元组 -> 格式化字符串
original_time = time.localtime()
formatted_str = time.strftime("%Y-%m-%d %H:%M:%S", original_time)
print(f"原始时间元组转格式化字符串: {formatted_str}")

# 步骤2: 格式化字符串 -> 时间元组
parsed_back = time.strptime(formatted_str, "%Y-%m-%d %H:%M:%S")
print(f"格式化字符串转回时间元组: {parsed_back}")

# 验证转换是否成功
print(f"转换前后是否一致: {original_time[:6] == parsed_back[:6]}")

print("\n=== 注意事项 ===")
print("1. strptime中的格式字符串必须与输入的日期字符串格式完全一致")
print("2. 格式符大小写敏感：%y是两位年份，%Y是四位年份")
print("3. 时间元组的前6个元素分别是：年、月、日、时、分、秒")
