# Python装饰器注意事项3：如何正确处理有返回值的函数

## 前言

在前面的章节中，我们学习了装饰器的基本用法，但在实际开发中，经常会遇到一个问题：**当被装饰的函数有返回值时，装饰器应该如何处理？**

今天我们就来深入探讨这个重要的问题，并给出通用的解决方案。

## 问题的发现

让我们先来看一个问题场景。假设我们有一个简单的装饰器和两个函数：

```python
def my_decorator(function):
    def wrapper(*args, **kwargs):
        print("=" * 30)
        print("装饰器：函数执行前的处理")
        function(*args, **kwargs)  # 注意这里！
        print("装饰器：函数执行后的处理")
        print("=" * 30)
    return wrapper

@my_decorator
def add_numbers(number1, number2, number3):
    print(f"计算：{number1} + {number2} + {number3}")
    return number1 + number2 + number3  # 有返回值

@my_decorator  
def print_hello():
    print("Hello, World!")  # 无返回值
```

现在让我们测试一下这两个函数：

```python
result1 = add_numbers(10, 20, 30)
result2 = print_hello()

print(f"result1: {result1}")
print(f"result2: {result2}")
```

**运行结果：**
```
==============================
装饰器：函数执行前的处理
计算：10 + 20 + 30
装饰器：函数执行后的处理
==============================
==============================
装饰器：函数执行前的处理
Hello, World!
装饰器：函数执行后的处理
==============================
result1: None
result2: None
```

## 问题分析

你发现问题了吗？**原本应该返回60的`add_numbers`函数，现在返回了`None`！**

这是为什么呢？让我们分析一下：

1. 当我们调用`add_numbers(10, 20, 30)`时，实际上调用的是装饰器内部的`wrapper`函数
2. 在`wrapper`函数中，我们执行了`function(*args, **kwargs)`，但**没有返回这个执行结果**
3. 由于`wrapper`函数没有`return`语句，所以默认返回`None`

**核心问题：装饰器内部函数必须与被装饰函数的格式保持一致，包括返回值！**

## 解决方案：正确处理返回值

要解决这个问题，我们需要修改装饰器，让它能够正确处理被装饰函数的返回值：

```python
def my_decorator(function):
    def wrapper(*args, **kwargs):
        print("=" * 30)
        print("装饰器：函数执行前的处理")
        
        # 关键点1：保存被装饰函数的执行结果
        result = function(*args, **kwargs)
        
        print("装饰器：函数执行后的处理")
        print("=" * 30)
        
        # 关键点2：返回被装饰函数的执行结果
        return result
    
    return wrapper
```

**关键改动说明：**

1. **保存结果**：使用`result = function(*args, **kwargs)`保存被装饰函数的执行结果
2. **返回结果**：使用`return result`将结果返回给调用者

## 验证解决方案

现在让我们测试修改后的装饰器：

```python
@my_decorator
def add_numbers(number1, number2, number3):
    print(f"计算：{number1} + {number2} + {number3}")
    return number1 + number2 + number3

@my_decorator
def print_hello():
    print("Hello, World!")

# 测试
result1 = add_numbers(10, 20, 30)
result2 = print_hello()

print(f"result1: {result1}")  # 现在应该是60
print(f"result2: {result2}")  # 仍然是None
```

**运行结果：**
```
==============================
装饰器：函数执行前的处理
计算：10 + 20 + 30
装饰器：函数执行后的处理
==============================
==============================
装饰器：函数执行前的处理
Hello, World!
装饰器：函数执行后的处理
==============================
result1: 60
result2: None
```

**完美！** 现在：
- 有返回值的函数（`add_numbers`）正确返回了计算结果60
- 无返回值的函数（`print_hello`）仍然返回None

## 通用装饰器的设计原则

通过这个例子，我们总结出通用装饰器的几个重要原则：

### 1. 参数兼容性
使用可变参数`*args, **kwargs`确保装饰器能处理任意参数的函数：

```python
def wrapper(*args, **kwargs):
    # 可以处理任意参数的函数
    result = function(*args, **kwargs)
    return result
```

### 2. 返回值兼容性  
始终返回被装饰函数的执行结果：

```python
# ✅ 正确做法
result = function(*args, **kwargs)
return result

# ❌ 错误做法
function(*args, **kwargs)  # 没有返回结果
```

### 3. 通用性验证
一个好的装饰器应该能同时处理：
- 有返回值的函数 → 保持原有返回值
- 无返回值的函数 → 返回None（Python函数的默认行为）

## 实践建议

在实际开发中，建议始终按照以下模板编写装饰器：

```python
def my_decorator(function):
    """通用装饰器模板"""
    def wrapper(*args, **kwargs):
        # 前置处理
        print("执行前的处理...")
        
        # 执行被装饰函数并保存结果
        result = function(*args, **kwargs)
        
        # 后置处理  
        print("执行后的处理...")
        
        # 返回原函数的执行结果
        return result
    
    return wrapper
```

## 总结

今天我们学习了装饰器处理返回值的重要知识点：

1. **问题根源**：装饰器内部函数没有正确处理被装饰函数的返回值
2. **解决方案**：保存并返回被装饰函数的执行结果
3. **设计原则**：装饰器内部函数必须与被装饰函数格式保持一致
4. **通用模板**：使用`*args, **kwargs`处理参数，始终返回执行结果

掌握了这个技巧，你就能写出真正实用的通用装饰器了！

下一篇文章，我们将继续探讨装饰器的高级用法。敬请期待！

---

**关注我，学习更多Python实战技巧！**
