# -*- coding: utf-8 -*-

# @Time    : 2025-5-25
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 100-Python-常用数据类型操作-获取当前CPU时间

import time

print("=== Python获取CPU时间测试程序执行耗时 ===")

# 使用场景：统计一段程序代码的执行耗时
print("主要用途：测试代码执行时间，优化程序性能")

# 1. 测试1000次循环的执行时间
print("\n=== 测试1：1000次循环 ===")
start = time.perf_counter()  # 获取开始时间

for i in range(1000):
    print(i, end=" ")

end = time.perf_counter()  # 获取结束时间
elapsed_time = end - start  # 计算时间差
print(f"\n1000次循环执行时间: {elapsed_time:.6f}秒")

# 2. 测试10000次循环的执行时间
print("\n=== 测试2：10000次循环 ===")
start = time.perf_counter()  # 获取开始时间

for i in range(10000):
    print(i, end=" ")

end = time.perf_counter()  # 获取结束时间
elapsed_time = end - start  # 计算时间差
print(f"\n10000次循环执行时间: {elapsed_time:.6f}秒")

# 3. 对比不同数量级的性能差异
print("\n=== 性能对比测试 ===")

def test_performance(count, description):
    """测试指定次数循环的性能"""
    start = time.perf_counter()
    
    # 模拟一些计算操作
    for i in range(count):
        result = i * i + i // 2
    
    end = time.perf_counter()
    elapsed = end - start
    print(f"{description}: {elapsed:.6f}秒")
    return elapsed

# 测试不同数量级
times_1k = test_performance(1000, "1千次计算")
times_10k = test_performance(10000, "1万次计算")
times_100k = test_performance(100000, "10万次计算")

print(f"\n性能提升倍数:")
print(f"1万次 vs 1千次: {times_10k/times_1k:.2f}倍")
print(f"10万次 vs 1千次: {times_100k/times_1k:.2f}倍")

# 4. 实际应用示例：测试不同算法的性能
print("\n=== 算法性能对比 ===")

def bubble_sort(arr):
    """冒泡排序"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    """快速排序"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 生成测试数据
import random
test_data = [random.randint(1, 1000) for _ in range(100)]

# 测试冒泡排序
start = time.perf_counter()
bubble_sorted = bubble_sort(test_data.copy())
bubble_time = time.perf_counter() - start

# 测试快速排序
start = time.perf_counter()
quick_sorted = quick_sort(test_data.copy())
quick_time = time.perf_counter() - start

print(f"冒泡排序耗时: {bubble_time:.6f}秒")
print(f"快速排序耗时: {quick_time:.6f}秒")
print(f"性能提升: {bubble_time/quick_time:.2f}倍")

# 5. 常用时间函数对比
print("\n=== 常用时间函数说明 ===")
print("time.perf_counter() - 高精度计时器，适合测量短时间间隔")
print("time.time() - 系统时间，可能受系统时钟调整影响")
print("time.process_time() - 进程CPU时间，不包括sleep时间")

# 演示不同时间函数的差异
print("\n=== 时间函数对比演示 ===")
start_perf = time.perf_counter()
start_time = time.time()
start_process = time.process_time()

# 执行一些计算
for i in range(50000):
    result = i ** 0.5

end_perf = time.perf_counter()
end_time = time.time()
end_process = time.process_time()

print(f"perf_counter(): {end_perf - start_perf:.6f}秒")
print(f"time(): {end_time - start_time:.6f}秒")
print(f"process_time(): {end_process - start_process:.6f}秒")

print("\n=== 使用建议 ===")
print("1. 推荐使用time.perf_counter()来测量代码执行时间")
print("2. 对于长时间运行的程序，可以使用time.process_time()")
print("3. 通过性能测试可以帮助优化代码，选择更高效的算法")
print("4. 在实际项目中，可以用这种方法找出性能瓶颈")
