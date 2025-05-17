# -*- coding: utf-8 -*-

# 29-Python-循环-for循环-简单语法

# 重复性的执行一些操作
# 使用场景
# 更多的是遍历一个集合

# for x in xxx:
# 语法
# 循怀语句
# 通常是一个集合XXX
# 般使用
# 解释
# 会取出集合中的每一个元素,赋值给变量x
# 在循环体中，可以直接使用x的值
# 当集合中的元素被遍历完毕,循环 就会结束

# 遍历一个集合
# 字符串、列表

# notice = "社会我NEO哥，人称NEO哥"
# for char in notice:
    # print("当前字符:", char)

pets = ["小白", "小黑", "小花"]
for pet in pets:
    print("当前宠物:", pet)