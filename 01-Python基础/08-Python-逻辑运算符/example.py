# -*- coding: utf-8 -*-

# b = True
# not 非，取反，真 -> 假；假 -> 真
# 一元运算符
# print(b)
# print(not b)

# and 与，并且，and 的两边必须都是真，最终才会是真
# 身份证 -> 并且 -> 成年 => 上网
# 二元运算符
# 是否有身份证
# id_card = True
# 是否成年
# age = False
# 是否可以上网
# result = id_card and age
# print(result)

# or 或，或者，or 的两边只要有一个条件是真的，那么最终都是真的
# 一真全真
# 门开了 窗户开了 => 进入到房间
# 是否门开了
# door = True
# 是否窗户开了
# window = False
# result = door or window
# print(result)

# 注意
# 非布尔类型的值，如果作为真假来判定，一般都是非零即真，非空即真
# 整个逻辑表达式的结果不一定只是True和False
# print(1 or False)
# print(bool(0))
# print(bool(""))

# print(0 and True)
# print(1 and 3)
# print(1 or 3)
# print(0 or 3)
# print(0 or False)
# print(0 or False or 6)
