# -*- coding: utf-8 -*-

# 是否大于 是 否 Bool
# >
# result = 10 > 2
# print(result)

# <
# result = 10 < 2
# print(result)

# !=
# result = 10 != 2
# print(result)

# <>
# Python2.x 版本支持，等同于!=
# Python3.x 版本不支持，报错，以后统一使用!=表示不等于
# result = 10 <> 2
# print(result)

# >=
# result = 10 >= 2
# print(result)

# <=
# result = 10 <= 2
# print(result)

# ==
# result = 10 == 2
# print(result)

# is 比对唯一标识
# num = 10
# print(id(num))

# a = 10
# b = 10
# print(id(a),  id(b))
# print(a is b)

# a = [1]
# b = [1]
# print(a == b)
# print(id(a))
# print(id(b))
# print(a is b)

# 链状比较运算符
num = 10
# num > 5，并且 num < 20
# 其它语言：num > 5 && num < 20 / num > 5 & num < 20 / num > 5 and num < 20
result = 5 < num < 20
print(result)
