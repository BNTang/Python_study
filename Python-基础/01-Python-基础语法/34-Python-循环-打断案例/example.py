# -*- coding: utf-8 -*-

# @Time    : 2025-5-17 12:30:06
# @Author  : NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 34-Python-循环-打断案例

# 1. 34-Python-循环-打断案例
# 做一个简单的加法计算器, 让用户输入两个数值,输出对应的和
# 案例
# 要求
# 用户如果不退出这个程序,则输出完毕之后,继续让用户使用
# 如果中间用户输入的数据有误,则给出错误提示, 并从头开始, 让用户数据数值

def main():
    """简单的加法计算器程序"""
    while True:
        print("\n===== 简单加法计算器 =====")
        
        # 获取并验证第一个数值
        while True:
            try:
                num1 = float(input("请输入第一个数值: "))
                break
            except ValueError:
                print("错误: 请输入有效的数字!")
        
        # 获取并验证第二个数值
        while True:
            try:
                num2 = float(input("请输入第二个数值: "))
                break
            except ValueError:
                print("错误: 请输入有效的数字!")
        
        # 计算并显示结果
        result = num1 + num2
        print(f"\n计算结果: {num1} + {num2} = {result}")
        
        # 询问用户是否继续
        choice = input("\n是否继续使用计算器? (y/n): ")
        if choice.lower() != 'y':
            print("感谢使用，再见!")
            break

if __name__ == "__main__":
    main()