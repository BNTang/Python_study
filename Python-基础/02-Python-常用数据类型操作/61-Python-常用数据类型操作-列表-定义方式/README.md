# Python 常用数据类型操作 - 列表的定义方式

大家好，我是程序员NEO。今天我们来深入了解Python中最常用的数据结构之一：列表(List)。列表是Python中使用频率最高的数据类型之一，掌握好列表的操作对我们的Python编程至关重要。

## 什么是列表？

列表是Python中用于存储多个元素的有序集合，可以包含不同类型的数据，如字符串、数字、布尔值甚至其他列表。列表是可变的，意味着创建后可以修改其内容。

## 列表的定义方式

Python中定义列表有多种方法，下面我们一一介绍。

### 1. 直接定义

最直观的方式是使用方括号`[]`直接定义列表：

```python
name_list = ['程序员NEO', '程序员小张', '程序员小李']
print(name_list)  # 输出: ['程序员NEO', '程序员小张', '程序员小李']

print(type(name_list))  # 输出: <class 'list'>
```

列表的强大之处在于它可以存储不同类型的数据：

```python
names = ['程序员NEO', True, 123]
print(names)  # 输出: ['程序员NEO', True, 123]
```

我们也可以创建空列表：

```python
names = []
print(type(names))  # 输出: <class 'list'>
print(names)  # 输出: []
```

列表还可以嵌套其他列表，形成多维结构：

```python
items = ["a", "b", "c"]
names = [1, 2, 3, items]
print(names)  # 输出: [1, 2, 3, ['a', 'b', 'c']]
print(type(names))  # 输出: <class 'list'>
```

### 2. 使用range()函数

`range()`函数可以生成一系列数字，结合`list()`函数可以快速创建数字列表：

```python
# 创建1到99的列表
name_list = list(range(1, 100))
print(name_list)  # 输出: [1, 2, 3, ..., 99]

# 创建1到99，步长为3的列表
name_list = list(range(1, 100, 3))
print(name_list)  # 输出: [1, 4, 7, ..., 97]

# 创建更大范围的列表
name_list = list(range(1, 10000))
print(name_list)  # 输出一个包含1到9999的列表
```

注意：直接打印`range()`对象只会显示范围而不会列出所有元素，需要使用`list()`转换才能看到完整列表。

### 3. 列表推导式

列表推导式是Python中一种强大而简洁的创建列表的方式。它可以让我们用一行代码完成创建、转换和过滤操作。

#### 基本概念

列表推导式的核心思想是：一对一变更（转换每个元素），过滤（从多到少），从一个列表推导出另一个列表。

先看一个传统的方式创建列表：

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 原始的方式：找出奇数并计算平方
result = []
for i in nums:
    if i % 2 == 0:
        continue
    resultNum = i ** 2
    result.append(resultNum)

print(result)  # 输出: [1, 9, 25, 49, 81]
```

而使用列表推导式，我们可以大大简化代码：

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 计算所有数字的平方
resultList = [num ** 2 for num in nums]
print(resultList)  # 输出: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 只计算偶数的平方
resultList = [num ** 2 for num in nums if num % 2 == 0]
print(resultList)  # 输出: [4, 16, 36, 64, 100]
```

列表推导式还可以嵌套使用，形成更复杂的表达式：

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultList = [num ** 2 for num in nums for num2 in nums]
print(resultList)  # 输出100个元素的列表，每个nums中的元素都会与自身组合一次
```

## 总结

Python列表的三种主要定义方式各有特点：
- 直接定义：最直观，适用于元素较少或已知的情况
- 使用range()：适合创建数字序列
- 列表推导式：代码简洁高效，适合需要转换或过滤的场景

灵活运用这些方法，能让我们的Python代码更加简洁、高效。在实际编程中，根据具体需求选择最合适的列表定义方式，可以大大提高我们的编程效率。

下期我们将继续探讨Python列表的其他重要操作，敬请期待！