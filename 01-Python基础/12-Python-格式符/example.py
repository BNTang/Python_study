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

# 分
# min = 5
# 秒
# sec = 8
# 05:08
# print("%d:%d" % (min, sec))
# 我写一个2，在控制台允许的效果居然是空格进行填充的
# print("%2d:%2d" % (min, sec))
# 如果我想让它在控制台显示的效果是 05:08，我就用0补充即可
# print("%02d:%02d" % (min, sec))
# 12d，表示填充12个空格
# print("%12d:%02d" % (min, sec))

# typeCode：表示数据的类型
score = 59.9
# 显示不全
# print("%d" % score)
# 精度太高
# print("%f" % score)
# print("%.2f" % score)
# print("%d" % 0b10)
# print("%d" % 0o10)
# print("%d" % 0x10)

# print("%o" % 10)
# print("%E" % 155555555555)

# print("%d" % 101.1)
# print("%g" % 10111111111111111)

# print("%s" % "abc")
# print("%c" % 97)

# 99%
# print("99%")
# score = 65
# print("%d%%" % score)
