# -*- coding: utf-8 -*-

# 0
#根据分数区间，打印出对应的级别特大于等于90 并且 小于等于100优秀#:大于等于80班并且 小于90良好*大于等于60 并且 小于80#及格#大于等于0并且 小于60不及格
# )并

score = 59

# if score >= 90 and score <= 100:
#     print('优秀')
# elif score >= 80 and score < 90:
#     print('良好')
# elif score >= 60 and score < 80:
#     print('及格')
# elif score >= 0 and score < 60:
#     print('不及格')

if 90 <=  score <= 100:
    print('优秀')
elif 80 <= score < 90:
    print('良好')
elif 60 <= score < 80:
    print('及格')
elif 0 <= score < 60:
    print('不及格')
