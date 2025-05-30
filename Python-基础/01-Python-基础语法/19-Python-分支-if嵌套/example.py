# -*- coding: utf-8 -*-

# if 的嵌套
score = 61

# if 90 <=  score <= 100:
#     print('优秀')
# if 80 <= score < 90:
#     print('良好')
# if 60 <= score < 80:
#     print('及格')
# if 0 <= score < 60:
#     print('不及格')

# 以上代码判断的次数太多了，本章节主要介绍一下 if 嵌套来优化这个问题，不然就像你过安保一样明显你第一层已经通过了后续就不用再进行再次安检一样的道理

# 下面是 if 嵌套的代码
if 90 <= score <= 100:
    print('优秀')
else:
    if 80 <= score < 90:
        print('良好')
    else:
        if 60 <= score < 80:
            print('及格')
        else:
            if 0 <= score < 60:
                print('不及格')
            else:
                print('分数不合法')