# Python字符串操作：填充与压缩

在Python编程中，字符串的处理是我们经常需要面对的任务。今天我们来学习字符串的填充与压缩操作，这些操作可以帮助我们格式化文本，使输出更加美观规整。

## 字符串的填充操作

当我们需要将字符串按照特定格式对齐时，Python提供了几个非常有用的方法。

### 1. 左对齐（ljust）

`ljust()`方法将字符串左对齐，并使用指定字符填充右侧至指定长度。

```python
name = "abc"
print("填充后的字符串为：", name.ljust(10, "0"))  # 输出：abc0000000
print(name)  # 输出：abc（原字符串不变）

name = "abc"
print("填充后的字符串为：", name.ljust(3, "0"))  # 输出：abc（长度已达到，不填充）
print(name)  # 输出：abc
```

需要注意的是，如果指定的长度小于或等于原字符串长度，则返回原字符串。

### 2. 右对齐（rjust）

与左对齐相反，`rjust()`方法将字符串右对齐，并使用指定字符填充左侧。

```python
name = "abc"
print("填充后的字符串为：", name.rjust(10, "0"))  # 输出：0000000abc
print(name)  # 输出：abc

name = "abc"
print("填充后的字符串为：", name.rjust(3, "0"))  # 输出：abc
print(name)  # 输出：abc
```

这种方法在格式化数字或创建表格式输出时特别有用。

### 3. 居中对齐（center）

`center()`方法使字符串居中显示，两侧填充指定字符。

```python
name = "abc"
print("填充后的字符串为：", name.center(10, "0"))  # 输出：000abc0000
print(name)  # 输出：abc

print("填充后的字符串为：", name.center(3, "0"))  # 输出：abc
print(name)  # 输出：abc
```

当填充的总长度为奇数时，Python会在右侧多填充一个字符。

### 4. 零填充（zfill）

`zfill()`是一个专门用来在字符串前面填充0的方法，常用于数字格式化。

```python
name = "abc"
print("填充后的字符串为：", name.zfill(10))  # 输出：0000000abc
print(name)  # 输出：abc

print("填充后的字符串为：", name.zfill(3))  # 输出：abc
print(name)  # 输出：abc
```

`zfill()`特别适合处理需要固定位数的数值字符串，例如订单号、编号等。

## 字符串的压缩操作（去除空格）

在处理用户输入或文本数据时，我们经常需要去除多余的空格。Python提供了三种方法来处理这种情况。

### 1. 去除左侧空格（lstrip）

`lstrip()`方法用于去除字符串左侧的空格。

```python
name = "   abc"
print("去除空格后的字符串为：", name.lstrip())  # 输出：abc
print(name)  # 输出：   abc（原字符串不变）
```

### 2. 去除右侧空格（rstrip）

`rstrip()`方法用于去除字符串右侧的空格。

```python
name = "abc   "
print("去除空格后的字符串为：", name.rstrip())  # 输出：abc
print(name)  # 输出：abc   （原字符串不变）
```

### 3. 去除两侧空格（strip）

`strip()`方法用于同时去除字符串两侧的空格。

```python
name = "   abc   "
print("去除空格后的字符串为：", name.strip())  # 输出：abc
print(name)  # 输出：   abc   （原字符串不变）
```

这三个方法不仅可以去除空格，还可以指定要去除的字符。如果不指定参数，默认去除空白字符（空格、制表符、换行符等）。

## 总结

通过本文的学习，我们掌握了Python中字符串的填充和压缩操作：

- 填充操作：`ljust()`, `rjust()`, `center()`, `zfill()`
- 压缩操作：`lstrip()`, `rstrip()`, `strip()`

这些方法不会改变原字符串，而是返回一个新的字符串。在实际编程中，这些方法可以帮助我们更好地处理字符串格式化和清洗工作。希望这篇文章对你学习Python字符串操作有所帮助！

---

如果你觉得这篇文章对你有帮助，欢迎关注我的公众号【程序员NEO】，获取更多Python学习资源！

#Python #字符串操作 #编程学习