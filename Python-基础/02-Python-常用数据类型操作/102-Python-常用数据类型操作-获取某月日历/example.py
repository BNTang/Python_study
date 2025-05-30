# -*- coding: utf-8 -*-

# @Time    : 2025-5-25
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 102-Python-常用数据类型操作-获取某月日历

# calendar模块
# 这个模块主要提供了与日历相关的一些功能
# 比如可以给定一个月份，帮你打印这个月的文本日历

# 导入calendar模块
import calendar

# 示例1：显示2017年6月份的日历
print("=== 2017年6月份日历 ===")
print(calendar.month(2017, 6))

# 示例2：显示当前年份的某个月
import datetime
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month

print(f"\n=== {current_year}年{current_month}月份日历 ===")
print(calendar.month(current_year, current_month))

# 示例3：显示整年的日历
print(f"\n=== {current_year}年整年日历 ===")
print(calendar.calendar(current_year))

# 示例4：获取某月的第一天是星期几和该月总天数
first_weekday, days_in_month = calendar.monthrange(2017, 6)
print(f"\n2017年6月份信息：")
print(f"第一天是星期{first_weekday + 1}（0=星期一，6=星期日）")
print(f"该月共有{days_in_month}天")

# 示例5：判断某年是否为闰年
year = 2024
if calendar.isleap(year):
    print(f"\n{year}年是闰年")
else:
    print(f"\n{year}年不是闰年")
