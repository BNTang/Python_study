# Python 常用数据类型操作 - 数值与运算符

## 1. Python 中的数值类型

在 Python 中，主要有三种数值类型：
- 整数（int）：如 10, -5, 0
- 浮点数（float）：如 3.14, -0.001, 1.0
- 复数（complex）：如 3+4j（本文不详细讨论）

不同于其他语言，Python 的整数没有大小限制，能表示任意大的数字，这使得数学计算更加便捷。

## 2. 算术运算符

Python 提供了丰富的算术运算符，让我们能够进行各种数学计算：

| 运算符 | 描述 | 示例 |
|-------|------|------|
| + | 加法 | 5 + 2 = 7 |
| - | 减法 | 5 - 2 = 3 |
| * | 乘法 | 5 * 2 = 10 |
| / | 除法（结果为浮点数） | 5 / 2 = 2.5 |
| // | 整除（向下取整） | 5 // 2 = 2 |
| % | 取余/模运算 | 5 % 2 = 1 |
| ** | 幂运算 | 5 ** 2 = 25 |

### 2.1 整除和取余的应用场景

整除（//）和取余（%）是两个非常有用的运算符，它们常常被用于以下场景：

**整除（//）的应用场景**：
- 需要向下取整的除法计算
- 计算时间的时、分、秒
- 数组索引的快速计算

**取余（%）的应用场景**：
- 判断奇偶性（n % 2 == 0 表示 n 是偶数）
- 循环索引（在固定范围内循环）
- 格式化时间（如 12 小时制）

示例：将秒转换为时分秒

```python
seconds = 3661
hours = seconds // 3600      # 整除计算小时
seconds %= 3600              # 取余计算剩余秒数
minutes = seconds // 60      # 整除计算分钟
seconds %= 60                # 取余计算剩余秒数
print(f"{hours}时{minutes}分{seconds}秒")  # 输出：1时1分1秒
```

## 3. 比较运算符

比较运算符用于比较值，返回布尔值（True 或 False）：

| 运算符 | 描述 | 示例 |
|-------|------|------|
| == | 等于 | a == b |
| != | 不等于 | a != b |
| > | 大于 | a > b |
| < | 小于 | a < b |
| >= | 大于等于 | a >= b |
| <= | 小于等于 | a <= b |
| is | 对象身份比较 | a is b |
| is not | 否定对象身份比较 | a is not b |

### 3.1 `==` 和 `is` 的区别

- `==` 比较的是对象的值是否相等
- `is` 比较的是对象的内存地址是否相同（是否是同一个对象）

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True，值相等
print(a is b)  # False，不是同一个对象
print(a is c)  # True，是同一个对象
```

### 3.2 链状比较运算符

Python 允许我们使用链状比较，使代码更加简洁：

```python
# 传统写法
x = 5
if x > 0 and x < 10:
    print("x 在 0 和 10 之间")

# 链状比较写法
if 0 < x < 10:
    print("x 在 0 和 10 之间")
```

链状比较的例子：`10 < a <= 66` 等价于 `10 < a and a <= 66`

## 4. 逻辑运算符

Python 中的三个逻辑运算符：

| 运算符 | 描述 | 示例 |
|-------|------|------|
| and | 逻辑与，两边都为 True 则返回 True | a and b |
| or | 逻辑或，至少有一边为 True 则返回 True | a or b |
| not | 逻辑非，取反 | not a |

### 4.1 逻辑运算符的短路特性

Python 的 `and` 和 `or` 运算符具有短路特性：

- `and`：如果第一个操作数为 False，则不再评估第二个操作数
- `or`：如果第一个操作数为 True，则不再评估第二个操作数

```python
# 短路特性示例
def func():
    print("函数被调用")
    return False

# and 的短路特性
result1 = False and func()  # 函数不会被调用
print(result1)  # False

# or 的短路特性
result2 = True or func()   # 函数不会被调用
print(result2)  # True
```

### 4.2 非布尔类型的逻辑运算

在 Python 中，非布尔类型的值在参与逻辑运算时遵循"非零即真"的原则：

- 数值：0 为 False，非零为 True
- 字符串：空字符串为 False，非空字符串为 True
- 列表/元组/字典：空为 False，非空为 True
- None：始终为 False

更有趣的是，`and` 和 `or` 运算符返回的不一定是布尔值，而是操作数本身：

- `x and y`：如果 x 为假，返回 x，否则返回 y
- `x or y`：如果 x 为真，返回 x，否则返回 y

```python
# 非布尔类型的逻辑运算
print(42 and 0)    # 0
print(42 and 23)   # 23
print(0 or 42)     # 42
print("" or "Hello")  # "Hello"
```

## 5. 数值类型的自动转换

当不同数值类型进行运算时，Python 会自动进行类型转换：

```python
n1 = 10       # int
n2 = 1.2      # float

print(type(n1), type(n2))  # <class 'int'> <class 'float'>

result = n1 + n2
print(result)       # 11.2
print(type(result)) # <class 'float'>
```

规则是：当 int 和 float 类型进行算术运算时，结果会被提升为 float 类型。

## 6. 实用技巧

1. **交换两个变量的值**：
   ```python
   a, b = 10, 20
   a, b = b, a  # 一行代码完成交换
   ```

2. **使用除法时的类型选择**：
   ```python
   # 需要精确结果用 /
   result1 = 5 / 2  # 2.5
   
   # 只需要整数部分用 //
   result2 = 5 // 2  # 2
   ```

3. **使用逻辑运算符简化条件赋值**：
   ```python
   # 传统方式
   if condition:
       x = value1
   else:
       x = value2
       
   # 使用逻辑运算简化
   x = condition and value1 or value2  # 当 value1 可能为假值时不要用
   x = value1 if condition else value2  # 更推荐这种写法
   ```

通过以上内容，我们了解了 Python 中数值类型的基本操作和各种运算符的使用方法。熟练掌握这些基础知识，将使我们的 Python 编程之路更加顺畅！