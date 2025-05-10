在编程学习过程中，判断条件是否成立是常见需求，这时“逻辑运算符”非常重要。Python 主要有三种逻辑运算符：not、and、or。下面带大家理清它们的用法，看完就会写出更准确的判断逻辑。

## 一、not —— 取反运算

`not` 是一元运算符，用于对布尔值取反。若原本为真（True），使用 `not` 后变为假（False）；若原本为假，则变为真。

```python
b = True
print(b)       # 输出：True
print(not b)   # 输出：False
```

就像在生活中说“不是”，比如“不是男生”，就是对“是男生”的否定。

## 二、and —— 并且（同时为真才为真）

`and` 是二元运算符，连接两个条件，只有当**两个条件都为真**时，结果才为真，否则为假。

**例子：**

上网需满足两个条件：有身份证**并且**已成年。只要有一项不满足，就不能上网。

```python
# 是否有身份证
id_card = True
# 是否成年
age = False
# 是否可以上网
result = id_card and age
print(result)  # 输出：False
```

由于 age 为 False（未成年），结果为 False，无法上网。

## 三、or —— 或者（有一个真就为真）

`or` 也是二元运算符，与 `and` 不同，只要**有一方为真**，结果就为真。

**例子：**

进入房间的条件：门开了**或者**窗户开了。只要有一个打开，就能进房间。

```python
# 是否门开了
door = True
# 是否窗户开了
window = False
result = door or window
print(result)  # 输出：True
```

因为 door 为 True，所以结果为 True。无论 window 是否打开，只要一方成立即可。

## 四、注意事项：布尔与非布尔类型的真假

在 Python 中，不仅仅 True 或 False 可以作为判断依据，其它类型也有自己的“真假”属性：

- 0、None、空字符串（“”）、空列表（）、空元组（()）：视为 False
- 其他非零数字、非空对象（如 “abc”、[1,2,3]）：视为 True

逻辑运算的返回值并不总是 True 或 False，而是返回某个运算数本身。例如：

```python
print(1 or False)           # 输出 1
print(0 and True)           # 输出 0
print(1 and 3)              # 输出 3
print(1 or 3)               # 输出 1
print(0 or 3)               # 输出 3
print(0 or False or 6)      # 输出 6
```

这是因为 Python 的 `and` 和 `or` 具有“短路”机制：

- `and` 遇到第一个为假的值就直接返回，不再判断其余部分。
- `or` 遇到第一个为真的值就直接返回，后面的不再执行。

这种特性在实际编程中特别实用，比如可以为变量设置默认值：

```python
name = input("请输入你的名字：") or "游客"
```

如果用户没有输入内容（即为空字符串，视为假），name 就会被赋值为“游客”。

## 五、总结

学会了 Python 逻辑运算符 `not`、`and`、`or`，你就能轻松表达各类条件判断：

- `not`：取反
- `and`：两边都为真才为真
- `or`：有一边为真就为真
- Python 逻辑运算不仅返回 True 或 False，还可能直接返回参与运算的值
