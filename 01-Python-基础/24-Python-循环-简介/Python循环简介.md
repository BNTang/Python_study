循环是Python中用于重复执行代码块的基本结构。当需要多次执行相同或相似操作时，循环可以大幅减少代码量并提高效率。

## 为什么需要循环？

假设我们需要打印数字1到10：
```python
print(1)
print(2)
print(3)
# ... 以此类推
print(10)
```

使用循环，我们可以简化为：
```python
for i in range(1, 11):
    print(i)
```

## Python中的循环类型

Python主要有两种循环结构：

### 1. for循环

for循环用于遍历序列（如列表、元组、字符串）或其他可迭代对象。

**基本语法**:
```python
for 变量 in 可迭代对象:
    # 执行的代码块
```

**示例**:
```python
# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(fruit)

# 使用range()函数
for i in range(5):
    print(i)  # 打印0到4
```

### 2. while循环

while循环在条件为真时重复执行代码块。

**基本语法**:

```python
while 条件:
    # 执行的代码块
```

**示例**:
```python
# 打印1到5
count = 1
while count <= 5:
    print(count)
    count += 1
```

## 循环控制语句

### break语句
用于跳出当前循环。

```python
for i in range(10):
    if i == 5:
        break
    print(i)  # 只打印0到4
```

### continue语句
用于跳过当前迭代，继续下一次迭代。

```python
for i in range(10):
    if i == 5:
        continue
    print(i)  # 打印0到4和6到9，跳过5
```

### pass语句
空操作，通常用作占位符。

```python
for i in range(5):
    if i == 2:
        pass  # 什么都不做
    print(i)
```

## 嵌套循环

循环可以嵌套使用，即在一个循环内部包含另一个循环。

```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

## 循环使用技巧

### 使用enumerate()同时获取索引和值

```python
fruits = ["苹果", "香蕉", "橙子"]
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")
```

### 使用zip()同时遍历多个列表

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} 今年 {age} 岁")
```

## 总结

- **for循环**：用于遍历可迭代对象
- **while循环**：在条件为真时重复执行
- 循环控制语句：**break**、**continue**、**pass**
- 循环可以嵌套使用
- 有多种技巧可以使循环更高效
