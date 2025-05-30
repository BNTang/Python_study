# -*- coding: utf-8 -*-

# @Time    : 2025-5-19 11:38:22
# @Author  : NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 41-Python-分支循环-综合案例-猜数字

# 1.程序内给定一个数字,比如500
# 给定一个数值,让用户猜
# 2.然后,让用户通过输入一个数值来猜
# 如果数值相等,则代表正确
# 程序结束
# 如果不相等,则给出提示, 是大了,还是小了
# 继续让用户猜

# 设定要猜的数字
target_number = 500

print("欢迎参加猜数字游戏！")
print("我已经想好了一个数字，请你来猜。")

# 初始化游戏循环
while True:
    # 获取用户的猜测
    guess_str = input("请输入你猜的数字: ")
    
    # 将输入转换为整数
    try:
        guess = int(guess_str)
    except ValueError:
        print("请输入有效的数字！")
        continue
    
    # 判断猜测结果
    if guess == target_number:
        print(f"恭喜你，猜对了！答案就是 {target_number}。")
        break  # 猜对了，退出循环
    elif guess > target_number:
        print("猜大了，请再试一次。")
    else:  # guess < target_number
        print("猜小了，请再试一次。")