# Python 常用数据类型操作 - 字符串函数操作 (查找计算)

在 Python 编程中，字符串是我们最常用的数据类型之一。如何高效地处理字符串、查找子串、计算长度等操作，是日常编程中的基本技能。今天我们就来详细学习 Python 中字符串的查找和计算操作。

## 1. 字符串长度计算 - len() 函数

`len()` 函数可以计算字符串的长度（即包含的字符个数）。

```python
name = "Python"
num = len(name)
print("字符串长度为：", num)  # 输出：字符串长度为：6
```

### 中文字符串长度

Python 3 中，一个中文字符的长度为 1：

```python
name = "我是 Python"
num = len(name)
print("字符串长度为：", num)  # 输出：字符串长度为：8
```

### 特殊字符的计算

换行符 `\n` 也被视为一个字符：

```python
name = "我是 Python\n"
num = len(name)
print("字符串长度为：", num)  # 输出：字符串长度为：9

name = "我是\nPython"
num = len(name)
print("字符串长度为：", num)  # 输出：字符串长度为：8
```

## 2. 字符串查找操作

### 2.1 find() 方法 - 从左向右查找

`find()` 方法用于检测字符串中是否包含指定的子字符串。如果找到了，返回子字符串的第一个字符在原字符串中的索引位置；如果没有找到，则返回 -1。

#### 基本用法

```python
name = "wo shi sz"
num = name.find("shi")
print("子串索引位置为：", num)  # 输出：子串索引位置为：3
```

#### 查找单个字符

```python
name = "wo shi sz"
num = name.find("s")
print("子串索引位置为：", num)  # 输出：子串索引位置为：3
```

**注意：** `find()` 方法是从左向右查找的，返回第一个匹配项的位置。

#### 查找不存在的子串

```python
name = "wo shi sz"
num = name.find("x")
print("子串索引位置为：", num)  # 输出：子串索引位置为：-1
```

#### 指定查找范围

您可以指定查找的开始位置：

```python
name = "wo shi sz"
num = name.find("s", 4)  # 从索引4开始查找
print("子串索引位置为：", num)  # 输出：子串索引位置为：7
```

您还可以同时指定查找的开始和结束位置：

```python
name = "wo shi sz"
num = name.find("s", 0, 4)  # 在索引0到3的范围内查找
print("子串索引位置为：", num)  # 输出：子串索引位置为：3
```

### 2.2 rfind() 方法 - 从右向左查找

`rfind()` 方法与 `find()` 类似，但它是从字符串的右边开始查找。

```python
name = "wo shi sz"
num = name.rfind("s")
print("子串索引位置为：", num)  # 输出：子串索引位置为：7
```

查找子串也是从右向左的顺序：

```python
name = "wo shi sz"
num = name.rfind("shi")
print("子串索引位置为：", num)  # 输出：子串索引位置为：3
```

同样，如果没有找到子串，返回 -1：

```python
name = "wo shi sz"
num = name.rfind("x")
print("子串索引位置为：", num)  # 输出：子串索引位置为：-1
```

### 2.3 index() 方法 - 功能类似 find()

`index()` 方法与 `find()` 方法几乎完全相同，区别在于：如果 `index()` 方法找不到子串，会引发 `ValueError` 异常，而不是返回 -1。

```python
name = "wo shi sz"
num = name.index("shi")
print("子串索引位置为：", num)  # 输出：子串索引位置为：3

name = "wo shi sz"
num = name.index("s")
print("子串索引位置为：", num)  # 输出：子串索引位置为：3
```

查找不存在的子串会引发异常：

```python
try:
    name = "wo shi sz"
    num = name.index("x")
    print("子串索引位置为：", num)
except ValueError:
    print("子串不存在，引发了 ValueError 异常")
```

### 2.4 rindex() 方法 - 功能类似 rfind()

`rindex()` 方法与 `rfind()` 方法类似，区别也是在没找到子串时会引发异常而不是返回 -1。

```python
name = "wo shi sz"
num = name.rindex("s")
print("子串索引位置为：", num)  # 输出：子串索引位置为：7

name = "wo shi sz"
num = name.rindex("shi")
print("子串索引位置为：", num)  # 输出：子串索引位置为：3
```

查找不存在的子串同样会引发异常：

```python
try:
    name = "wo shi sz"
    num = name.rindex("x")
    print("子串索引位置为：", num)
except ValueError:
    print("子串不存在，引发了 ValueError 异常")
```

## 3. 字符串计数 - count() 方法

`count()` 方法用于统计字符串中某个子串出现的次数。

### 基本用法

```python
name = "wo shi sz"
num = name.count("s")
print("子串出现的次数为：", num)  # 输出：子串出现的次数为：2
```

### 统计子串出现次数

```python
name = "wo shi sz"
num = name.count("shi")
print("子串出现的次数为：", num)  # 输出：子串出现的次数为：1
```

### 统计不存在的子串

如果子串不存在，返回 0：

```python
name = "wo shi sz"
num = name.count("x")
print("子串出现的次数为：", num)  # 输出：子串出现的次数为：0
```

### 指定查找范围

和 `find()` 方法一样，`count()` 也可以指定查找范围：

```python
name = "wo shi sz"
num = name.count("s", 0, 4)  # 在索引0到3的范围内查找
print("子串出现的次数为：", num)  # 输出：子串出现的次数为：1
```

## 总结

在 Python 中，对字符串进行查找和计算操作有多种方法：

1. **长度计算**：`len()` 函数可以计算字符串的长度
2. **子串查找**：
   - `find()` 和 `rfind()`：分别从左向右和从右向左查找，找不到返回 -1
   - `index()` 和 `rindex()`：与上面两个方法功能类似，但找不到会抛出异常
3. **次数统计**：`count()` 方法可以统计子串出现的次数

这些方法在日常编程中非常实用，掌握它们可以帮助你更高效地处理字符串数据。在实际应用中，选择合适的方法可以让你的代码更加简洁、健壮。

希望这篇文章对你有所帮助，欢迎关注我的公众号获取更多 Python 学习内容！

---

> 本文作者：程序员NEO  
> 版权声明：本文为原创文章，未经允许不得转载。  
> GitHub：https://github.com/BNTang  
> Email：it666@linux.do
