# 格式化输出
# name = "Alice"
# age = 30

# 我的名字是 xxx，年龄是 xxx
# print("我的名字是 %s, 年龄是 %d" % (name, age))

# %[(name)][flags][width][.precision]typecode
# []: 可以省略

# (name)
# 表示，根据，指定的名称(key)，查找对应的值，格式化到字符串当中
# mathScore = 59
# englishScore = 89
# print("我的数学分数是%d, 英语分数是%d" % (mathScore, englishScore))
# 假设我现在有一个需求就是将数学分数和英语分数，互换一下
# 第一种方式就是在 %后面，直接将数学分数和英语分数互换
# print("我的数学分数是%d, 英语分数是%d" % (englishScore, mathScore))
# 第二种方式就是通过 name 来指定
# print("我的数学分数是%(mathScore)d, 英语分数是%(englishScore)d" % {"mathScore": mathScore, "englishScore": englishScore})

# width：表示占用的宽度
# 我如下的代码，100，这个数字是不是占用 3 个宽度
# print("%d" % 100)
# 这个时候我改一下代码的写法，我在 %d 前面加上一个 4
# print("%4d" % 100)
# 所以 width 的意思就是占用的宽度

# flags：表示对齐的方式
# 左对齐
# print("%-4d" % 100)

# 与负数对齐
# print("%d" % -100)
# print("% d" % 100)
# 多个空格也是显示一个空格
# print("%  d" % 100)

min = 5
sec = 8
# 05:08
# print("%d:%d" % (min, sec))
# print("%2d:%2d" % (min, sec))
# print("%12d:%02d" % (min, sec))
