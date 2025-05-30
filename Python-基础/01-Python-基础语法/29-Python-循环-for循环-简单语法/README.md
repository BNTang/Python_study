# Python 循环 - for循环基础语法

## 为什么需要循环？

在编程中，我们经常需要重复执行某些操作。比如向10个好友发送相同的消息，或者计算100个数字的总和。如果没有循环，我们就需要写10次或100次几乎完全相同的代码，这显然是低效且容易出错的。

循环结构能够帮助我们优雅地处理这类重复性任务，而Python中最常用的循环之一就是`for`循环。

## for循环的基本概念

`for`循环主要用于**遍历集合**（如字符串、列表、元组等），它会自动迭代集合中的每个元素并执行指定的操作。

### 基本语法

```python
for 变量 in 可迭代对象:
    # 循环体（要重复执行的代码）
```

### 工作原理

1. Python从可迭代对象（通常是一个集合）中取出一个元素
2. 将这个元素赋值给循环变量
3. 执行循环体中的代码
4. 返回第1步，直到集合中的所有元素都被处理完毕

## for循环实战演练

### 1. 遍历字符串

字符串在Python中是一个字符的序列，可以用for循环逐个处理每个字符：

```python
notice = "社会我NEO哥，人称NEO哥"
for char in notice:
    print("当前字符:", char)
```

执行结果：

```
当前字符: 社
当前字符: 会
当前字符: 我
...以此类推...
```

### 2. 遍历列表

列表是Python中最常用的数据结构之一，for循环可以轻松访问列表中的每个元素：

```python
pets = ["小白", "小黑", "小花"]
for pet in pets:
    print("当前宠物:", pet)
```

执行结果：

```
当前宠物: 小白
当前宠物: 小黑
当前宠物: 小花
```

### 3. 使用range()函数生成数字序列

如果需要执行指定次数的循环，可以使用`range()`函数：

```python
# 打印5次"Hello"
for i in range(5):  # range(5)生成0,1,2,3,4
    print(f"第{i+1}次打印：Hello")
```

执行结果：

```
第1次打印：Hello
第2次打印：Hello
第3次打印：Hello
第4次打印：Hello
第5次打印：Hello
```

range()函数还可以指定起始值和步长：

```python
# range(start, stop, step)
for i in range(1, 10, 2):  # 从1开始，到10结束（不包含），步长为2
    print(i)  # 输出：1, 3, 5, 7, 9
```

### 4. 遍历元组和集合

元组和集合的遍历方式与列表相同：

```python
# 元组
colors = ("红", "橙", "黄", "绿", "蓝")
for color in colors:
    print(f"彩虹有{color}色")

# 集合
unique_numbers = {1, 3, 5, 7, 9}
for num in unique_numbers:
    print(f"{num}是奇数")
```

### 5. 遍历字典

字典是键值对的集合，可以有多种遍历方式：

```python
student = {
    "name": "小明",
    "age": 18,
    "score": 95
}

# 遍历键
for key in student:
    print(key, student[key])

# 遍历键值对
for key, value in student.items():
    print(f"{key}: {value}")
```

## for循环的高级用法

### 1. enumerate() - 同时获取索引和值

```python
fruits = ["苹果", "香蕉", "橙子"]
for index, fruit in enumerate(fruits):
    print(f"序号{index+1}: {fruit}")
```

输出：

```
序号1: 苹果
序号2: 香蕉
序号3: 橙子
```

### 2. 列表推导式 - 简洁高效的循环表达式

最初的写法可能是：

```python
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)  # [1, 4, 9, 16, 25]
```

使用列表推导式可以简化为：

```python
squares = [i ** 2 for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

## 小结

for循环是Python中处理集合元素的强大工具，通过简洁的语法可以轻松遍历各种数据结构。掌握for循环对编写高效、简洁的Python代码至关重要。主要记住以下几点：

1. for循环主要用于遍历集合中的元素
2. 循环变量会依次获取集合中的每个元素
3. 结合range()函数可以实现计数循环
4. 不同数据结构（字符串、列表、元组、字典等）都可以使用for循环遍历
5. 列表推导式是for循环的简洁表达形式

学习编程就像学习一门语言，熟能生巧。希望大家多多练习for循环的使用，灵活应用到实际编程中！

---
欢迎关注我的公众号，获取更多Python学习资料！