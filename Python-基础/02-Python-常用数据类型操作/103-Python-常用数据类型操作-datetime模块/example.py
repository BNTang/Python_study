# -*- coding: utf-8 -*-

# @Time    : 2025-5-25
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 103-Python-常用数据类型操作-datetime模块

"""
datetime模块是Python处理日期和时间的标准库
注意：datetime是模块名称，但模块里面包含几个类：
- datetime类：用于操作具体的时间
- date类：用于操作日期
- time类：用于操作时间
- timedelta类：用于表示时间间隔
"""

import datetime

print("=== 1. 获取当前日期和时间 ===")
# 使用datetime.datetime.now()获取当前时间
t1 = datetime.datetime.now()
print(f"当前时间(now): {t1}")

# 使用datetime.datetime.today()获取当前时间
t2 = datetime.datetime.today()
print(f"当前时间(today): {t2}")

print(f"t1的类型: {type(t1)}")

print("\n=== 2. 单独获取年月日时分秒 ===")
t = datetime.datetime.now()
print(f"完整时间: {t}")
print(f"年份: {t.year}")
print(f"月份: {t.month}")
print(f"日期: {t.day}")
print(f"小时: {t.hour}")
print(f"分钟: {t.minute}")
print(f"秒数: {t.second}")

print("\n=== 3. 计算N天之后的日期 ===")
# 获取当前时间
today = datetime.datetime.now()
print(f"今天: {today}")

# 使用timedelta创建时间间隔（7天后）
time_delta = datetime.timedelta(days=7)
result = today + time_delta
print(f"7天后: {result}")

# 其他时间间隔示例
print(f"3小时后: {today + datetime.timedelta(hours=3)}")
print(f"30分钟后: {today + datetime.timedelta(minutes=30)}")
print(f"10秒后: {today + datetime.timedelta(seconds=10)}")

print("\n=== 4. 计算两个日期之间的时间差 ===")
# 创建两个日期对象
first = datetime.datetime(2017, 9, 2, 12, 0, 0)
second = datetime.datetime(2017, 9, 3, 12, 0, 0)

print(f"第一个日期: {first}")
print(f"第二个日期: {second}")

# 计算时间差
delta = second - first
print(f"时间差: {delta}")
print(f"时间差类型: {type(delta)}")

# 获取总秒数
total_seconds = delta.total_seconds()
print(f"时间差总秒数: {total_seconds}")

print("\n=== 5. 更多datetime操作示例 ===")
# 创建指定日期
specific_date = datetime.datetime(2025, 12, 25, 18, 30, 45)
print(f"指定日期: {specific_date}")

# 格式化输出
formatted_date = specific_date.strftime("%Y年%m月%d日 %H:%M:%S")
print(f"格式化输出: {formatted_date}")

# 只获取日期部分
date_only = specific_date.date()
print(f"只有日期: {date_only}")

# 只获取时间部分
time_only = specific_date.time()
print(f"只有时间: {time_only}")

# 计算距离特定日期还有多少天
target_date = datetime.datetime(2025, 12, 31, 23, 59, 59)
current_time = datetime.datetime.now()
days_until_target = (target_date - current_time).days
print(f"距离2025年12月31日还有: {days_until_target} 天")

print("\n=== datetime模块学习完成 ===")
