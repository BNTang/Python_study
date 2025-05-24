# -*- coding: utf-8 -*-

# @Time    : 2025-5-24
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 98-Python-常用数据类型操作-格式化时间

import time

print("=" * 50)
print("时间格式化示例")
print("=" * 50)

# 1. 获取当前时间戳
current_timestamp = time.time()
print(f"当前时间戳: {current_timestamp}")

# 2. 获取当前时间元组
current_time_tuple = time.localtime()
print(f"当前时间元组: {current_time_tuple}")

print("\n" + "=" * 50)
print("格式化时间示例")
print("=" * 50)

# 3. 将时间戳转换为可读的格式化时间
# 使用 ctime() 函数将时间戳转换为可读字符串
result1 = time.ctime(current_timestamp)
print(f"时间戳格式化结果: {result1}")

# 4. 将时间元组转换为可读的格式化时间
# 使用 asctime() 函数将时间元组转换为可读字符串
result2 = time.asctime(current_time_tuple)
print(f"时间元组格式化结果: {result2}")

print("\n" + "=" * 50)
print("其他格式化示例")
print("=" * 50)

# 5. 使用 strftime() 进行自定义格式化
custom_format1 = time.strftime("%Y-%m-%d %H:%M:%S", current_time_tuple)
print(f"自定义格式1 (年-月-日 时:分:秒): {custom_format1}")

custom_format2 = time.strftime("%Y年%m月%d日 %H时%M分%S秒", current_time_tuple)
print(f"自定义格式2 (中文格式): {custom_format2}")

custom_format3 = time.strftime("%A, %B %d, %Y", current_time_tuple)
print(f"自定义格式3 (英文格式): {custom_format3}")

# 6. 格式化指定时间戳
specified_timestamp = 1609459200  # 2021-01-01 00:00:00 UTC
specified_time = time.ctime(specified_timestamp)
print(f"指定时间戳 {specified_timestamp} 的格式化结果: {specified_time}")

print("\n" + "=" * 50)
print("总结")
print("=" * 50)
print("1. ctime() - 将时间戳转换为可读字符串")
print("2. asctime() - 将时间元组转换为可读字符串") 
print("3. strftime() - 自定义格式化时间显示")
print("格式化时间比时间戳和时间元组更容易阅读和理解")
