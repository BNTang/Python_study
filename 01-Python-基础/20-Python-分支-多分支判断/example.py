# -*- coding: utf-8 -*-

score = 85

# 可读性太差
# if 90 <= score <= 100:
#     print('优秀')
# else:
#     if 80 <= score < 90:
#         print('良好')
#     else:
#         if 60 <= score < 80:
#             print('及格')
#         else:
#             if 0 <= score < 60:
#                 print('不及格')
#             else:
#                 print('分数不合法')

# 可读性好
if 90 <= score <= 100:
    print('优秀')
elif 80 <= score < 90:
    print('良好')
elif 60 <= score < 80:
    print('及格')
elif 0 <= score < 60:
    print('不及格')
else:
    print('分数不合法')