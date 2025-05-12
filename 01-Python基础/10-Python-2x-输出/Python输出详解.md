在学习 Python 编程时，“输出”几乎是我们最常用的操作。今天我们来系统梳理 print 的用法，包括 Python2 和 Python3 的使用区别与技巧，一篇文章全掌握！

------

## 一、Python2 和 Python3 的 print 用法区别

- **Python2**：print 是语句。用法：`print xxx`
- **Python3**：print 是函数。用法：`print(xxx)`

建议直接学习 Python3 的写法，兼容新旧版本，且更规范。

------

## 二、print 的基础用法

### 1. 输出单个值

Python2：

```python
print 123
```

Python3：

```python
print(123)
```

### 2. 输出变量

```python
num = 10
print(num)
```

### 3. 输出多个变量

```python
num = 10
name = '小明'
print(num, name)
# 输出：10 小明
```

------

## 三、print 的进阶用法

### 1. 格式化输出

#### 1) 百分号占位符（兼容 Python2/3）

```python
num = 10
name = '小明'
print('我的名字是%s，我的年龄是%d' % (name, num))
```

#### 2) format 方法（推荐 Python3）

```python
print('我的名字是{}，我的年龄是{}'.format(name, num))
```

#### 3) f-string（Python3.6+）

```python
print(f'我的名字是{name}，我的年龄是{num}')
```

------

### 2. 控制输出末尾和分隔符

#### 1) print 默认换行，如何不换行？

Python2：

```python
print '1',
print '2',
print '3',
```

Python3：

```python
print('1', end=' ')
print('2', end=' ')
print('3')
```

#### 2) 自定义分隔符

Python3 可用 sep 参数：

```python
print('1', '2', '3', sep='-')  # 输出：1-2-3
```

或者用 join 拼接列表：

```python
print('-'.join(['1', '2', '3']))  # 输出：1-2-3
```

------

### 3. 输出到文件

有时需要将内容写入文件：

Python2：

```python
f = open('test.txt', 'w')
print >>f, "示例内容"
f.close()
```

Python3：

```python
with open('test.txt', 'w', encoding='utf-8') as f:
    print("示例内容", file=f)
```

------

### 4. 立即刷新输出

print 默认内容先存入缓冲区，如遇换行、刷新时才输出。若想立即显示，可用 flush 参数：

```python
import time
for i in range(3):
    print(i, end=' ', flush=True)
    time.sleep(1)
```

------

## 四、print 输出原理补充

Python 输出时，内容会先写入缓冲区。在遇到换行、缓冲区满或程序结束时，才真正输出到终端。需要及时显示时，可设置 flush=True 强制刷新。

------

## 五、总结

本文系统梳理了 print 的各种用法：

- Python2 与 Python3 语法区别
- 基础用法、格式化输出、分隔符、控制结尾
- 如何输出到文件、输出立即刷新原理