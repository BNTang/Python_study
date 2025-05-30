# -*- coding: utf-8 -*-

# @Time    : 2025-5-24
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 97-Python-常用数据类型操作-时间元组

import time

print("=" * 50)
print("Python时间元组操作示例")
print("=" * 50)

# 1. 获取当前时间元组（不带参数）
print("\n1. 获取当前时间元组：")
result = time.localtime()
print(f"当前时间元组: {result}")

# 时间元组结构说明
print("\n时间元组结构说明：")
print("tm_year  (年份)    :", result.tm_year)
print("tm_mon   (月份)    :", result.tm_mon)
print("tm_mday  (日期)    :", result.tm_mday)
print("tm_hour  (小时)    :", result.tm_hour)
print("tm_min   (分钟)    :", result.tm_min)
print("tm_sec   (秒)      :", result.tm_sec)
print("tm_wday  (星期几)  :", result.tm_wday, "(0=周一, 6=周日)")
print("tm_yday  (年中第几天):", result.tm_yday)
print("tm_isdst (夏令时)  :", result.tm_isdst, "(0=否, 1=是, -1=不确定)")

# 2. 使用指定时间戳获取时间元组
print("\n2. 使用指定时间戳获取时间元组：")
# 示例时间戳：1404104425 (对应2014年6月30日)
timestamp = 1404104425
result_with_timestamp = time.localtime(timestamp)
print(f"时间戳 {timestamp} 对应的时间元组:")
print(result_with_timestamp)

# 格式化显示
print(f"格式化显示: {result_with_timestamp.tm_year}年{result_with_timestamp.tm_mon}月{result_with_timestamp.tm_mday}日 "
      f"{result_with_timestamp.tm_hour}:{result_with_timestamp.tm_min:02d}:{result_with_timestamp.tm_sec:02d}")

# 3. 时间元组的索引访问
print("\n3. 时间元组的索引访问（0-8个元素）：")
for i in range(9):
    print(f"索引 {i}: {result[i]}")

# 4. 补充：将时间元组转回时间戳
print("\n4. 将时间元组转回时间戳：")
timestamp_back = time.mktime(result)
print(f"当前时间元组转换的时间戳: {timestamp_back}")

print("\n" + "=" * 50)
print("时间元组操作学习要点：")
print("1. 理解时间元组的9个元素含义")
print("2. 掌握time.localtime()函数的使用")
print("3. 了解时间元组的结构和访问方式")
print("=" * 50)
