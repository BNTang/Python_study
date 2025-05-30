# -*- coding: utf-8 -*-

# @Time    : 2025-5-22 12:58:29
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 63-Python-常用数据类型操作-列表-常用操作-删除

# del 语句
# nums = [1, 2, 3, 4, 5]
# print(nums)

# del nums[0]
# print(nums)

# nums = [1, 2, 3, 4, 5]

# del nums

# print(nums)

# pop 方法
# nums = [1, 2, 3, 4, 5]
# print(nums)
# print(nums.pop())
# print(nums.pop(0))
# print(nums)
# print(nums.pop(11)) # IndexError: pop index out of range

# remove 方法
# nums = [1, 2, 3, 4, 5]
# print(nums)
# result = nums.remove(3)
# print(result)
# print(nums)

# 注意：循环内删除元素带来的坑
nums = [1, 2, 3, 4, 5, 5, 2, 3, 2]

for i in nums:
    # print(i)
    if i == 2:
        nums.remove(i) # 删除元素

print(nums)
# nums.remove(2)