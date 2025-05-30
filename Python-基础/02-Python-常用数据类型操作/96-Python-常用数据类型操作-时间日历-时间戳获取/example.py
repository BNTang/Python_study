# -*- coding: utf-8 -*-

# @Time    : 2025-5-24
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 96-Python-常用数据类型操作-时间日历-时间戳获取

"""
时间日历处理学习
主要学习 time、calendar、datetime 三个模块的使用

时间戳概念：
- 从1970年1月1日0:00:00 UTC（零时区）到指定时间的秒数
- 对于中国（东八区），是从1970年1月1日8:00:00开始计算
- 返回的是一个浮点数
"""

import time

# 1. 获取当前时间戳
print("=== 时间戳获取示例 ===")
result = time.time()
print(f"当前时间戳: {result}")

# 2. 验证时间戳的正确性 - 计算对应的年份
print("\n=== 时间戳验证 ===")
# 计算从1970年到现在的年数
# 一年 = 365天 × 24小时 × 60分钟 × 60秒
seconds_per_year = 365 * 24 * 60 * 60
years_since_1970 = result / seconds_per_year
current_year = 1970 + years_since_1970

print(f"从1970年到现在经过的秒数: {result}")
print(f"从1970年到现在经过的年数: {years_since_1970:.2f}")
print(f"计算得出的当前年份: {current_year:.2f}")

# 3. 更精确的当前年份获取（用于对比）
import datetime
actual_year = datetime.datetime.now().year
print(f"实际当前年份: {actual_year}")

# 4. 时间戳的其他应用示例
print("\n=== 时间戳应用场景 ===")
print("时间戳常用于:")
print("1. 记录用户操作时间（如发帖时间）")
print("2. 日志系统中记录事件发生时间")
print("3. 数据库中存储时间信息")
print("4. 计算时间间隔和比较时间")

# 5. 简单的时间间隔计算示例
print("\n=== 时间间隔计算示例 ===")
start_time = time.time()
# 模拟一些处理时间
time.sleep(1)  # 暂停1秒
end_time = time.time()

elapsed_time = end_time - start_time
print(f"开始时间戳: {start_time}")
print(f"结束时间戳: {end_time}")
print(f"耗时: {elapsed_time:.2f} 秒")
