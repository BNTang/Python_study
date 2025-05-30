# Python 常用数据类型操作 - 列表排序详解

## 一、排序操作简介

在 Python 编程中，排序是一项非常常见且重要的操作。Python 提供了两种主要的排序方式：
- 使用内置函数 `sorted()` - 创建一个新的已排序列表
- 使用列表对象的 `.sort()` 方法 - 直接修改原列表

这两种方式虽然用途相似，但有着本质的区别。让我们通过实例来深入了解。

## 二、sorted() 函数详解

`sorted()` 函数可以排序任何可迭代对象，并且总是返回一个新的已排序列表，原对象保持不变。

### 2.1 字符串排序

```python
# 字符串排序示例
s = "abcdefghijklmnopqrscccctuvwxyz"
result = sorted(s)
print(result)
# 输出: ['a', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```

注意：当对字符串进行排序时，`sorted()` 会返回一个由单个字符组成的列表，而不是一个新的字符串。

### 2.2 反向排序

使用 `reverse=True` 参数可以实现降序排序：

```python
# 字符串反向排序
s = "abcdefghijklmnopqrscccctuvwxyz"
result = sorted(s, reverse=True)
print(result)
# 输出: ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'c', 'c', 'c', 'c', 'b', 'a']

# 数字列表反向排序
s = [1, 3, 2, 4, 5, 22, 2, 2, 4, 19]
result = sorted(s, reverse=True)
print(result)
# 输出: [22, 19, 5, 4, 4, 3, 2, 2, 2, 1]
```

### 2.3 对数字列表进行排序

```python
s = [1, 3, 2, 4, 5, 22, 2, 2, 4, 19]
result = sorted(s)
print(result)
# 输出: [1, 2, 2, 2, 3, 4, 4, 5, 19, 22]
```

### 2.4 对元组列表进行排序

当对元组列表进行排序时，默认按照元组的第一个元素进行排序：

```python
s = [("neo", 20), ("程序员neo", 18), ("财务neo", 19)]
result = sorted(s)
print(result)
# 输出: [('neo', 20), ('程序员neo', 18), ('财务neo', 19)]
```

可以看到，排序是按照元组第一个元素（字符串）的字母顺序进行的。

### 2.5 使用自定义键进行排序

如果我们想按照元组的第二个元素（年龄）排序，可以使用 `key` 参数：

```python
def get_key(item):
    return item[1]

s = [("neo", 20), ("程序员neo", 18), ("财务neo", 19)]
result = sorted(s, key=get_key)
print(result)
# 输出: [('程序员neo', 18), ('财务neo', 19), ('neo', 20)]
```

这样就实现了按年龄从小到大的排序。同样，我们也可以结合 `reverse` 参数实现从大到小排序：

```python
s = [("neo", 20), ("程序员neo", 18), ("财务neo", 19)]
result = sorted(s, key=get_key, reverse=True)
print(result)
# 输出: [('neo', 20), ('财务neo', 19), ('程序员neo', 18)]
```

## 三、列表的 .sort() 方法

与 `sorted()` 不同，列表的 `.sort()` 方法是直接修改原列表，不会创建新的列表对象，并且返回值为 `None`。

```python
l = [1, 3, 2, 4, 5, 22, 2, 2, 4, 19]
result = l.sort()
print(result)  # 输出: None
print(l)       # 输出: [1, 2, 2, 2, 3, 4, 4, 5, 19, 22]
```

### 3.1 使用自定义键和 .sort() 方法

`.sort()` 方法也支持 `key` 参数：

```python
def get_key(item):
    return item[1]

s = [("neo", 20), ("程序员neo", 18), ("财务neo", 19)]
result = s.sort(key=get_key)
print(result)  # 输出: None
print(s)       # 输出: [('程序员neo', 18), ('财务neo', 19), ('neo', 20)]
```

### 3.2 反向排序与自定义键结合

同样，`.sort()` 方法也支持 `reverse` 参数：

```python
s = [("neo", 20), ("程序员neo", 18), ("财务neo", 19)]
result = s.sort(key=get_key, reverse=True)
print(result)  # 输出: None
print(s)       # 输出: [('neo', 20), ('财务neo', 19), ('程序员neo', 18)]
```

## 四、总结

1. **排序方式选择**:
   - 需要保留原列表不变，使用 `sorted()` 函数
   - 直接修改原列表，使用 `.sort()` 方法

2. **返回值差异**:
   - `sorted()` 返回新的排序后列表
   - `.sort()` 返回 `None`，直接修改原列表

3. **适用对象范围**:
   - `sorted()` 可用于任何可迭代对象（列表、元组、字符串等）
   - `.sort()` 仅适用于列表对象

4. **参数使用**:
   - 两者都支持 `key` 参数自定义排序逻辑
   - 两者都支持 `reverse` 参数控制升序或降序

掌握这两种排序方法，可以让我们在 Python 编程中更加得心应手地处理各种数据排序需求。

---

欢迎关注我的微信公众号，获取更多 Python 编程技巧！