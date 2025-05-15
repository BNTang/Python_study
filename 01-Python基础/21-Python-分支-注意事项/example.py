# -*- coding: utf-8 -*-
# 强制缩进# tab缩进
# 注意
# if 10 > 2:
#     print("10 is greater than 2")
#     print("10 is greater than 2")
#     print("10 is greater than 2")
#     print("10 is greater than 2")

# print("10 is greater than 2")

# if else 匹配问题
# 嵌套


# 按照缩进格式进行匹配建议,不要写嵌套层级太深的代码
# Python中没有类似于其他语言中的swith...case语法

# 注意：仅适用于Python 3.10及以上版本
day = "Monday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("工作日")
    case "Saturday" | "Sunday":
        print("周末")
    case _:
        print("未知")