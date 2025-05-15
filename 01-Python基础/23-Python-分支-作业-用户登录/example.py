# -*- coding: utf-8 -*-

# 定义正确的用户名和密码
correct_username = "admin"
correct_password = "123456"

# 获取用户输入的用户名和密码
username = input("请输入用户名：")
password = input("请输入密码：")

# 验证用户名和密码
if username == correct_username and password == correct_password:
    # 用户名和密码都正确
    print("登录成功")
else:
    if username != correct_username:
        # 如果账号错误
        print("账号错误")
    else:
        # 如果密码错误
        print("密码错误")
