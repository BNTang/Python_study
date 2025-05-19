# 42-Python-常用数据类型操作-简介

大家好，今天我们来聊一聊Python中常用的数据类型及其基本操作。作为一门灵活高效的编程语言，Python提供了多种数据类型来满足不同的编程需求。掌握这些基本数据类型的操作是Python编程的基础，也是进一步学习的重要前提。

## 1. 数字类型（Numbers）

Python中的数字类型主要包括整数（int）、浮点数（float）和复数（complex）。

### 1.1 整数（int）

整数可以是正数、负数或零，没有小数点。Python 3中的整数没有大小限制。

```python
# 整数的定义
a = 10
b = -5
c = 0

# 整数的运算
print(a + b)  # 5
print(a * b)  # -50
print(a // b)  # -2（整除）
print(a % b)  # 0（取余）
print(a ** 2)  # 100（幂运算）
```

### 1.2 浮点数（float）

浮点数是带有小数点的数字。

```python
# 浮点数的定义
x = 3.14
y = -0.001
z = 2.0

# 浮点数运算
print(x + y)  # 3.139
print(x * z)  # 6.28
print(round(x, 1))  # 3.1（四舍五入到1位小数）
```

### 1.3 复数（complex）

复数由实部和虚部组成，表示为`a + bj`。

```python
# 复数的定义
c1 = 2 + 3j
c2 = complex(4, -1)

# 复数运算
print(c1 + c2)  # (6+2j)
print(c1 * c2)  # (11+10j)
print(c1.real)  # 2.0（实部）
print(c1.imag)  # 3.0（虚部）
```

## 2. 字符串（String）

字符串是由字符组成的序列，在Python中使用单引号或双引号括起来。

### 2.1 字符串的创建与基本操作

```python
# 字符串的定义
s1 = 'Hello'
s2 = "World"

# 字符串拼接
greeting = s1 + ' ' + s2
print(greeting)  # Hello World

# 字符串重复
print(s1 * 3)  # HelloHelloHello

# 字符串索引（从0开始）
print(s1[0])  # H
print(s1[-1])  # o（负索引从末尾开始）

# 字符串切片
print(s1[1:4])  # ell
print(s1[:3])  # Hel
print(s1[2:])  # llo
```

### 2.2 常用字符串方法

Python的字符串提供了丰富的方法：

```python
# 大小写转换
print("python".upper())  # PYTHON
print("PYTHON".lower())  # python
print("python".capitalize())  # Python

# 查找与替换
text = "Python is amazing"
print(text.find("is"))  # 7
print(text.replace("amazing", "awesome"))  # Python is awesome

# 分割与连接
words = text.split(" ")
print(words)  # ['Python', 'is', 'amazing']
print("-".join(words))  # Python-is-amazing

# 判断方法
print("123".isdigit())  # True
print("Python".startswith("Py"))  # True
print("  ".isspace())  # True

# 去除空白
print("  Python  ".strip())  # "Python"
```

## 3. 列表（List）

列表是Python中最常用的数据类型之一，它是有序的、可变的集合，可以存储不同类型的元素。

### 3.1 列表的创建与基本操作

```python
# 列表的定义
fruits = ['apple', 'banana', 'cherry']
mixed = [1, 'hello', 3.14, True]

# 访问列表元素
print(fruits[0])  # apple
print(fruits[-1])  # cherry

# 修改列表元素
fruits[1] = 'orange'
print(fruits)  # ['apple', 'orange', 'cherry']

# 列表切片
print(fruits[0:2])  # ['apple', 'orange']
```

### 3.2 列表常用方法

```python
# 添加元素
fruits.append('grape')  # 在末尾添加元素
print(fruits)  # ['apple', 'orange', 'cherry', 'grape']

fruits.insert(1, 'banana')  # 在指定位置插入元素
print(fruits)  # ['apple', 'banana', 'orange', 'cherry', 'grape']

# 删除元素
fruits.remove('orange')  # 删除指定元素
print(fruits)  # ['apple', 'banana', 'cherry', 'grape']

popped = fruits.pop()  # 弹出末尾元素
print(popped)  # grape
print(fruits)  # ['apple', 'banana', 'cherry']

# 列表操作
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()  # 排序
print(numbers)  # [1, 1, 3, 4, 5, 9]

numbers.reverse()  # 反转
print(numbers)  # [9, 5, 4, 3, 1, 1]

print(len(numbers))  # 6（长度）
print(numbers.count(1))  # 2（统计元素出现次数）
```

## 4. 元组（Tuple）

元组是有序的、不可变的集合，一旦创建就不能修改其内容。

```python
# 元组的定义
coordinates = (10, 20)
person = ('John', 25, 'USA')

# 访问元组元素
print(coordinates[0])  # 10
print(person[-1])  # USA

# 元组不可修改
# coordinates[0] = 15  # 这会报错！

# 元组方法
print(person.count(25))  # 1
print(person.index('John'))  # 0
```

## 5. 字典（Dictionary）

字典是无序的、可变的键值对集合，每个键都必须是唯一的。

### 5.1 字典的创建与基本操作

```python
# 字典的定义
student = {
    'name': 'Alice',
    'age': 22,
    'major': 'Computer Science'
}

# 访问字典元素
print(student['name'])  # Alice

# 修改或添加元素
student['age'] = 23
student['gender'] = 'Female'
print(student)  # {'name': 'Alice', 'age': 23, 'major': 'Computer Science', 'gender': 'Female'}
```

### 5.2 字典常用方法

```python
# 获取所有键和值
print(student.keys())  # dict_keys(['name', 'age', 'major', 'gender'])
print(student.values())  # dict_values(['Alice', 23, 'Computer Science', 'Female'])
print(student.items())  # dict_items([('name', 'Alice'), ('age', 23), ('major', 'Computer Science'), ('gender', 'Female')])

# 安全获取值
print(student.get('name'))  # Alice
print(student.get('phone', 'Not Found'))  # Not Found（指定默认值）

# 删除元素
removed = student.pop('gender')
print(removed)  # Female
print(student)  # {'name': 'Alice', 'age': 23, 'major': 'Computer Science'}
```

## 6. 集合（Set）

集合是无序的、不包含重复元素的集合。

```python
# 集合的定义
colors = {'red', 'green', 'blue'}
numbers = {1, 2, 3, 2, 1}  # 重复元素会被自动去除
print(numbers)  # {1, 2, 3}

# 集合操作
colors.add('yellow')  # 添加元素
colors.remove('green')  # 删除元素
print(colors)  # {'red', 'blue', 'yellow'}

# 集合运算
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # {1, 2, 3, 4, 5}（并集）
print(set1.intersection(set2))  # {3}（交集）
print(set1.difference(set2))  # {1, 2}（差集）
```

## 7. 数据类型转换

Python提供了多种内置函数来进行数据类型的转换。

```python
# 字符串转数字
num_str = "42"
num_int = int(num_str)  # 42
num_float = float(num_str)  # 42.0

# 数字转字符串
num = 3.14
str_num = str(num)  # "3.14"

# 列表、元组、集合之间的转换
my_list = [1, 2, 3, 2]
print(tuple(my_list))  # (1, 2, 3, 2)
print(set(my_list))  # {1, 2, 3}

# 字典相关转换
pairs = [('a', 1), ('b', 2)]
print(dict(pairs))  # {'a': 1, 'b': 2}
```

## 8. 综合实例

让我们来看一个综合运用各种数据类型的例子：

```python
# 分析学生成绩数据
students = [
    {'name': 'Alice', 'scores': [85, 90, 78]},
    {'name': 'Bob', 'scores': [92, 88, 95]},
    {'name': 'Charlie', 'scores': [76, 85, 79]}
]

# 计算每个学生的平均分
for student in students:
    name = student['name']
    scores = student['scores']
    average = sum(scores) / len(scores)
    print(f"{name}的平均分是: {average:.2f}")
    
# 找出最高平均分
highest_avg = 0
top_student = ''

for student in students:
    avg = sum(student['scores']) / len(student['scores'])
    if avg > highest_avg:
        highest_avg = avg
        top_student = student['name']
        
print(f"最高平均分学生: {top_student}, 平均分: {highest_avg:.2f}")
```

## 总结

Python提供了多种强大而灵活的数据类型，包括数字、字符串、列表、元组、字典和集合。每种类型都有其独特的特性和适用场景。熟练掌握这些数据类型的操作和方法，是成为Python高手的必经之路。

希望这篇文章能帮助你更好地理解和使用Python的常用数据类型。在实际编程中，选择合适的数据类型可以让你的代码更加简洁、高效和易于维护。

下一篇，我们将深入探讨Python的控制流结构。敬请期待！