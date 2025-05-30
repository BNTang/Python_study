# -*- coding: utf-8 -*-

# num = 0
# while num < 10:
#     num += 1
#     print("num is now:", num)
# else:
#     print("The loop has ended.")

num = 0
while num < 10:
    num += 1
    print("num is now:", num)
    break
else:
    print("The loop has ended.")

# 一定要注意循环结束条件，防止死循环
# 在 Python 中，没有类似于其他语言的 do...while 语句
# 但是可以使用 while 循环来模拟 do...while 循环的行为