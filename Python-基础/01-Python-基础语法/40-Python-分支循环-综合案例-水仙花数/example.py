# -*- coding: utf-8 -*-

# @Time    : 2025-5-18 13:49:39
# @Author  : NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 40-Python-分支循环-综合案例-水仙花数

# 用户输入一个3位数值, 判定是否是水仙花数
# 1. 要求对三位数值验证
# 2.判定3位水仙花数的标准
# 只需要验证是不是三位数值就可以
# 暂时不考虑非数字的情况
# 百位的3次方 + 十位的3次方 + 个位的3次方
# 1**3=1
# = 数值本身
# 153
# 5**3 = 125
# 3*3 = 27

# 获取用户输入
num_str = input("请输入一个三位数: ")
num = int(num_str)

# 验证是否是三位数
if 100 <= num <= 999:
    # 提取各个位的数字
    hundreds = num // 100  # 百位
    tens = (num % 100) // 10  # 十位
    ones = num % 10  # 个位
     
    # 计算各位数字的立方和
    sum_of_cubes = hundreds**3 + tens**3 + ones**3
    
    # 判断是否是水仙花数
    if sum_of_cubes == num:
        print(f"{num} 是水仙花数")
    else:
        print(f"{num} 不是水仙花数")
else:
    print("输入错误，请输入一个三位数")