# Python 循环结构：while 循环详解

在 Python 编程中，循环结构是我们处理重复任务的强大工具。今天，我们来学习 while 循环，并通过一个简单的案例——计算 1 到 10 的总和，来掌握它的用法。

## while 循环的基本语法

while 循环的基本语法如下：

```python
while 条件表达式:
    循环体
```

当条件表达式为真（True）时，循环体会一直执行；当条件表达式为假（False）时，循环结束。

## 案例：计算 1-10 的总和

让我们用 while 循环来解决一个简单的问题：计算从 1 到 10 的所有整数之和。

### 思路分析

1. 我们需要两个变量：一个记录当前数字（num），一个记录累加的结果（result）
2. 从 1 开始，依次将每个数字加到结果中
3. 当数字达到 10 时，循环结束

### 代码实现

```python
# 计算 1-10 的数值总和
num = 0
result = 0

while num < 10:
    num += 1
    result += num

print("1-10的总和是:", result)
```

### 代码详解

1. `num = 0`：初始化计数器变量，从 0 开始
2. `result = 0`：初始化结果变量，用于累加数字
3. `while num < 10:`：设置循环条件，当 num 小于 10 时，继续执行循环
4. `num += 1`：每次循环，计数器加 1（相当于 num = num + 1）
5. `result += num`：将当前数字加到结果中（相当于 result = result + num）
6. 循环结束后，打印计算结果

运行这段代码，我们会得到输出：`1-10的总和是: 55`

## 循环的执行过程

让我们来跟踪这个循环的执行过程：

| 循环次数 | num的值（递增后） | result的值（累加后） | 条件 num < 10 |
|---------|----------------|-------------------|---------------|
| 初始状态 | 0              | 0                 | True          |
| 第1次    | 1              | 1                 | True          |
| 第2次    | 2              | 3                 | True          |
| 第3次    | 3              | 6                 | True          |
| 第4次    | 4              | 10                | True          |
| 第5次    | 5              | 15                | True          |
| 第6次    | 6              | 21                | True          |
| 第7次    | 7              | 28                | True          |
| 第8次    | 8              | 36                | True          |
| 第9次    | 9              | 45                | True          |
| 第10次   | 10             | 55                | False（循环结束）|

## 优化与其他方法

除了使用 while 循环，我们还有其他方式可以计算 1 到 10 的和：

### 1. 使用 for 循环

```python
result = 0
for i in range(1, 11):  # 注意 range(1, 11) 生成 1 到 10 的序列
    result += i
print("1-10的总和是:", result)
```

### 2. 使用内置函数 sum()

```python
result = sum(range(1, 11))
print("1-10的总和是:", result)
```

### 3. 使用数学公式

对于 1 到 n 的连续整数求和，我们可以使用公式：n*(n+1)/2

```python
n = 10
result = n * (n + 1) // 2  # 整数除法
print("1-10的总和是:", result)
```

## 小结

while 循环是 Python 中非常重要的控制结构，适用于不确定循环次数、需要根据条件判断是否继续循环的场景。在本例中，我们通过计算 1 到 10 的和，展示了 while 循环的基本用法。

同时，我们也学习了多种解决同一问题的方法。这正是编程的魅力所在——同一个问题可以有多种解决方案，而选择最适合当前场景的方法，是编程能力提升的重要体现。

## 练习

1. 尝试修改代码，计算 1 到 100 的总和
2. 尝试计算 1 到 n 的总和，其中 n 由用户输入
3. 修改循环，只计算 1 到 10 中偶数的总和

希望这篇文章对你学习 Python 的 while 循环有所帮助。下一篇，我们将继续深入学习 Python 的其他循环结构和控制语句。敬请关注！