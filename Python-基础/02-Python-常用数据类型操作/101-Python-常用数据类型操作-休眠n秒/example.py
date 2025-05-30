# -*- coding: utf-8 -*-

# @Time    : 2025-5-25
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 101-Python-常用数据类型操作-休眠n秒

import time
import random

def main():
    print("=== Python常用数据类型操作 - 休眠演示 ===")
    print()
    
    # 初始化数据
    print("📋 初始化数据...")
    data_list = [1, 2, 3, 4, 5]
    data_dict = {"name": "张三", "age": 25, "city": "北京"}
    data_set = {10, 20, 30, 40, 50}
    
    print(f"列表数据: {data_list}")
    print(f"字典数据: {data_dict}")
    print(f"集合数据: {data_set}")
    print("✅ 数据初始化完成")
    
    # 休眠2秒
    print("\n💤 休眠2秒...")
    time.sleep(2)
    
    # 列表操作
    print("\n📝 执行列表操作...")
    data_list.append(6)
    print(f"添加元素后: {data_list}")
    time.sleep(1)  # 休眠1秒
    
    data_list.extend([7, 8, 9])
    print(f"扩展列表后: {data_list}")
    time.sleep(1)
    
    # 字典操作
    print("\n📚 执行字典操作...")
    data_dict["score"] = 95
    print(f"添加键值对后: {data_dict}")
    time.sleep(1)
    
    data_dict.update({"grade": "A", "subject": "Python"})
    print(f"更新字典后: {data_dict}")
    time.sleep(1)
    
    # 集合操作
    print("\n🔢 执行集合操作...")
    data_set.add(60)
    print(f"添加元素后: {data_set}")
    time.sleep(1)
    
    new_set = {70, 80, 90}
    union_set = data_set.union(new_set)
    print(f"集合并集: {union_set}")
    time.sleep(1)
    
    # 模拟实时数据处理
    print("\n🔄 模拟实时数据处理...")
    for i in range(5):
        random_num = random.randint(1, 100)
        print(f"第{i+1}次处理: 生成随机数 {random_num}")
        print("─" * 30)
        time.sleep(1.5)  # 每次处理后休眠1.5秒
    
    print("\n✨ 所有操作完成！")
    print("最终数据状态:")
    print(f"列表: {data_list}")
    print(f"字典: {data_dict}")
    print(f"集合: {union_set}")

if __name__ == "__main__":
    main()
