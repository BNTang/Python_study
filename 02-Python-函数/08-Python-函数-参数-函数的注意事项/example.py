# -*- coding: utf-8 -*-

# @Time    : 2025-5-27
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 08-Python-函数-参数-函数的注意事项

"""
Python函数参数的注意事项：
1. Python中只有引用传递（地址传递），没有值传递
2. 对于不可变类型（int, str, tuple等），无法修改原对象
3. 对于可变类型（list, dict, set等），可以修改原对象
"""

print("=" * 50)
print("Python函数参数传递机制演示")
print("=" * 50)

# ====== 1. 基础概念演示：不可变类型（int） ======
print("\n1. 不可变类型（int）演示：")

def test_immutable(number):
    print(f"函数内部 - 修改前number的ID: {id(number)}")
    print(f"函数内部 - 修改前number的值: {number}")
    
    # 尝试修改number的值
    number = 666
    print(f"函数内部 - 修改后number的ID: {id(number)}")
    print(f"函数内部 - 修改后number的值: {number}")

# 测试不可变类型
b = 10
print(f"调用前b的ID: {id(b)}")
print(f"调用前b的值: {b}")

test_immutable(b)

print(f"调用后b的ID: {id(b)}")
print(f"调用后b的值: {b}")
print("结论：不可变类型在函数内修改不会影响原变量")

# ====== 2. 可变类型（list）演示 ======
print("\n" + "=" * 50)
print("2. 可变类型（list）演示：")

def test_mutable(number):
    print(f"函数内部 - 修改前number的ID: {id(number)}")
    print(f"函数内部 - 修改前number的值: {number}")
    
    # 修改list内容
    number.append(666)
    print(f"函数内部 - 修改后number的ID: {id(number)}")
    print(f"函数内部 - 修改后number的值: {number}")

# 测试可变类型
b = [1, 2, 3]
print(f"调用前b的ID: {id(b)}")
print(f"调用前b的值: {b}")

test_mutable(b)

print(f"调用后b的ID: {id(b)}")
print(f"调用后b的值: {b}")
print("结论：可变类型在函数内修改会影响原变量")

# ====== 3. 深入理解：重新赋值 vs 修改内容 ======
print("\n" + "=" * 50)
print("3. 重新赋值 vs 修改内容的区别：")

def test_reassign_list(lst):
    print(f"函数内部 - 重新赋值前lst的ID: {id(lst)}")
    # 重新赋值（创建新对象）
    lst = [7, 8, 9]
    print(f"函数内部 - 重新赋值后lst的ID: {id(lst)}")
    print(f"函数内部 - 重新赋值后lst的值: {lst}")

def test_modify_list(lst):
    print(f"函数内部 - 修改前lst的ID: {id(lst)}")
    # 修改原对象内容
    lst.clear()
    lst.extend([7, 8, 9])
    print(f"函数内部 - 修改后lst的ID: {id(lst)}")
    print(f"函数内部 - 修改后lst的值: {lst}")

# 测试重新赋值
print("\n3.1 重新赋值测试：")
original_list1 = [1, 2, 3]
print(f"原始列表ID: {id(original_list1)}, 值: {original_list1}")
test_reassign_list(original_list1)
print(f"调用后列表ID: {id(original_list1)}, 值: {original_list1}")

# 测试修改内容
print("\n3.2 修改内容测试：")
original_list2 = [1, 2, 3]
print(f"原始列表ID: {id(original_list2)}, 值: {original_list2}")
test_modify_list(original_list2)
print(f"调用后列表ID: {id(original_list2)}, 值: {original_list2}")

# ====== 4. 常见数据类型分类 ======
print("\n" + "=" * 50)
print("4. Python数据类型分类：")
print("不可变类型：int, float, str, tuple, frozenset, bool, None")
print("可变类型：list, dict, set, bytearray")

# ====== 5. 实际应用示例 ======
print("\n" + "=" * 50)
print("5. 实际应用示例：")

def safe_list_operation(lst):
    """安全的列表操作：不修改原列表"""
    new_lst = lst.copy()  # 创建副本
    new_lst.append("新元素")
    return new_lst

def unsafe_list_operation(lst):
    """不安全的列表操作：修改原列表"""
    lst.append("新元素")
    return lst

original = ["元素1", "元素2"]
print(f"原始列表: {original}")

# 安全操作
safe_result = safe_list_operation(original)
print(f"安全操作后 - 原列表: {original}")
print(f"安全操作后 - 返回列表: {safe_result}")

# 不安全操作
unsafe_result = unsafe_list_operation(original)
print(f"不安全操作后 - 原列表: {original}")
print(f"不安全操作后 - 返回列表: {unsafe_result}")

print("\n" + "=" * 50)
print("总结：")
print("1. Python中所有参数传递都是引用传递（地址传递）")
print("2. 不可变类型：函数内重新赋值不影响原变量")
print("3. 可变类型：函数内修改内容会影响原变量")
print("4. 要避免意外修改，可以传递副本或使用不可变类型")
print("=" * 50)
