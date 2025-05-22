# -*- coding: utf-8 -*-

# @Time    : 2025-5-22 12:58:29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 74-Python-常用数据类型操作-字典-定义的注意事项

# key不能重复,如果是重复的后面的会覆盖前面的
# d = {"name": "neo", "name": "neo2"}
# print(d)

# key必须任意不可变类型
# d = {[1, 2]: "neo"}
# print(d) # 报错, TypeError: unhashable type: 'list'

# num = 10
# print(id(num))  # 1407263040
# num = 20
# print(id(num))  # 1407263072

num = [1, 2, 3]
print(id(num))  # 1407263040
num.append(4)
print(id(num))  # 1407263040