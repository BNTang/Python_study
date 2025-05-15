# Python-循环-while循环-简单语法

## 什么是 while 循环？

在 Python 中，while 循环用于重复执行一段代码，只要给定的条件保持为真。当不知道循环需要执行多少次时，while 循环特别有用。

## 基本语法

```python
while 条件:
    # 循环体
    # 当条件为真时执行的代码
```

## 简单示例

```python
# 打印 1 到 5 的数字
count = 1
while count <= 5:
    print(count)
    count += 1
```

输出:
```
1
2
3
4
5
```

## break 和 continue 语句

### break 语句
`break` 语句用于提前退出循环。

```python
# 使用 break 退出循环
count = 1
while count <= 10:
    print(count)
    if count == 5:
        break  # 当 count 等于 5 时退出循环
    count += 1
```

输出:
```
1
2
3
4
5
```

### continue 语句
`continue` 语句用于跳过当前迭代，继续下一次迭代。

```python
# 使用 continue 跳过偶数
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:  # 如果是偶数
        continue  # 跳过当前迭代
    print(count)
```

输出:
```
1
3
5
7
9
```

## 无限循环

无限循环是条件始终为真的循环。必须通过 `break` 语句或其他方式（如 Ctrl+C）退出。

```python
# 无限循环 - 谨慎使用！
while True:
    user_input = input("输入 'quit' 退出: ")
    if user_input.lower() == 'quit':
        break
    print("你输入了:", user_input)
```

## while...else 结构

Python 中的 while 循环也可以有一个 else 子句，当条件变为假时执行。

```python
# while...else 示例
count = 1
while count <= 5:
    print(count)
    count += 1
else:
    print("循环正常结束，count =", count)
```

输出:
```
1
2
3
4
5
循环正常结束，count = 6
```

## 嵌套 while 循环

```python
# 嵌套 while 循环
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i, "*", j, "=", i * j)
        j += 1
    i += 1
    print("-----")
```

## 练习题

1. 编写一个程序，计算 1 到 100 之间所有整数的和。
2. 编写一个程序，从用户那里获取输入，直到用户输入 "quit"。
3. 编写一个程序，计算用户输入的所有正数的平均值，遇到负数时停止。
