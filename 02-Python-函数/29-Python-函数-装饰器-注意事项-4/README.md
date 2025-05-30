# Python装饰器进阶：带参数的装饰器详解

## 前言

在前面的文章中，我们已经学习了Python装饰器的基本用法。今天我们要深入探讨一个更高级的话题：**带参数的装饰器**。

你是否遇到过这样的场景：需要多个功能相似但细节不同的装饰器？比如有时需要在函数执行前打印横线，有时需要打印等号，有时需要打印星号...

如果按照传统方式，我们需要写多个几乎相同的装饰器，这显然违背了DRY（Don't Repeat Yourself）原则。今天就让我们一起学习如何用带参数的装饰器优雅地解决这个问题。

## 从问题开始：代码重复的困扰

首先，让我们看一个简单的例子。假设我有一个函数：

```python
def f1():
    print("666")
```

现在我想为这个函数添加装饰效果，在执行前打印一些装饰字符。按照传统方式，我们可能会这样写：

```python
def zsq(func):
    """装饰器 - 打印横线"""
    def inner():
        print("-" * 30)  # 打印30个横线
        func()  # 执行原函数
    return inner

def zsq1(func):
    """装饰器 - 打印等号"""
    def inner():
        print("=" * 30)  # 打印30个等号
        func()  # 执行原函数
    return inner

def zsqs(func):
    """装饰器 - 打印星号"""
    def inner():
        print("*" * 30)  # 打印30个星号
        func()  # 执行原函数
    return inner
```

使用这些装饰器：

```python
@zsq
def demo1():
    print("666")

@zsq1  
def demo2():
    print("666")

@zsqs
def demo3():
    print("666")
```

**问题显而易见：**
- 三个装饰器的结构几乎完全相同
- 只有打印的字符不同（`-`、`=`、`*`）
- 如果需要更多字符，就得写更多装饰器
- 代码重复，维护困难

## 理想的解决方案

我们理想中的解决方案应该是这样的：

```python
@get_decorator("-")  # 传入横线参数
def f2():
    print("666")

@get_decorator("=")  # 传入等号参数
def f3():
    print("666")

@get_decorator("*")  # 传入星号参数
def f4():
    print("666")
```

看起来很完美，但这样写能行吗？让我们来分析一下。

## 为什么简单的参数传递不行？

你可能会想，直接给装饰器函数加个参数不就行了：

```python
def zsq(func, char):  # ❌ 这样写是错误的
    def inner():
        print(char * 30)
        func()
    return inner
```

但这样写是**行不通**的！为什么？

**关键理解：装饰器语法糖的工作原理**

当我们写：
```python
@zsq
def f1():
    pass
```

它等价于：
```python
f1 = zsq(f1)
```

注意，Python会**自动**将被装饰的函数作为**唯一参数**传递给装饰器。装饰器函数只能接收一个参数（被装饰的函数），不能接收其他参数。

所以 `@zsq("-")` 这样的写法会报错，因为Python不知道如何处理这个额外的参数。

## 正确的解决方案：装饰器工厂

要实现带参数的装饰器，我们需要引入一个新概念：**装饰器工厂**。

**核心思想：**
- 写一个函数，这个函数接收参数，返回装饰器
- `@` 符号后面的内容必须是一个装饰器函数

```python
def get_decorator(char):
    """
    装饰器工厂函数
    参数：char - 要打印的字符
    返回：装饰器函数
    """
    def decorator(func):  # 这才是真正的装饰器
        def inner():     # 这是被装饰后的函数
            print(char * 30)  # 使用传入的字符
            func()           # 执行原函数
        return inner
    return decorator  # 返回装饰器
```

**三层结构解析：**
1. **外层函数** (`get_decorator`)：接收参数，返回装饰器
2. **中层函数** (`decorator`)：真正的装饰器，接收被装饰的函数
3. **内层函数** (`inner`)：装饰后的函数，包含增强逻辑

## 工作原理深度解析

当我们写：
```python
@get_decorator("-")
def f2():
    print("666")
```

实际的执行过程是：

1. **第一步**：`get_decorator("-")` 被调用，返回一个装饰器
2. **第二步**：返回的装饰器装饰 `f2` 函数

等价于：
```python
decorator = get_decorator("-")  # 获取装饰器
f2 = decorator(f2)             # 用装饰器装饰函数
```

**关键理解：** `@get_decorator("-")` 中的 `get_decorator("-")` 会**先执行**，其返回值才是真正用来装饰函数的装饰器。

## 完整示例和测试

```python
def get_decorator(char):
    def decorator(func):
        def inner():
            print(char * 30)
            func()
        return inner
    return decorator

@get_decorator("-")
def f2():
    print("666")

@get_decorator("=")
def f3():
    print("666")

@get_decorator("*")
def f4():
    print("666")

@get_decorator("#")
def f5():
    print("666")

# 测试
f2()  # 输出：30个横线 + 666
f3()  # 输出：30个等号 + 666
f4()  # 输出：30个星号 + 666
f5()  # 输出：30个井号 + 666
```

## 进阶：更复杂的参数装饰器

带参数的装饰器不仅可以接收单个参数，还可以接收多个参数：

```python
def advanced_decorator(char, count, prefix=""):
    """
    更复杂的参数装饰器
    参数：
    - char: 装饰字符
    - count: 字符重复次数  
    - prefix: 前缀文本
    """
    def decorator(func):
        def inner():
            if prefix:
                print(f"{prefix}:")
            print(char * count)
            func()
            print(char * count)
        return inner
    return decorator

@advanced_decorator("*", 20, "开始执行")
def important_function():
    print("这是一个重要的函数")

@advanced_decorator("=", 15, "DEBUG")  
def debug_function():
    print("调试信息")
```

## 实际应用场景

带参数的装饰器在实际开发中有很多应用场景：

### 1. 日志记录
```python
def log_decorator(level="INFO"):
    def decorator(func):
        def inner(*args, **kwargs):
            print(f"[{level}] 调用函数: {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{level}] 函数执行完毕")
            return result
        return inner
    return decorator

@log_decorator("DEBUG")
def calculate(a, b):
    return a + b
```

### 2. 性能监控
```python
def performance_monitor(threshold=1.0):
    import time
    def decorator(func):
        def inner(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            cost = time.time() - start
            if cost > threshold:
                print(f"警告：函数 {func.__name__} 执行时间过长: {cost:.2f}秒")
            return result
        return inner
    return decorator

@performance_monitor(0.5)
def slow_function():
    time.sleep(1)  # 模拟耗时操作
```

### 3. 权限控制
```python
def require_permission(permission):
    def decorator(func):
        def inner(*args, **kwargs):
            if not check_permission(permission):
                raise PermissionError(f"需要 {permission} 权限")
            return func(*args, **kwargs)
        return inner
    return decorator

@require_permission("admin")
def delete_user(user_id):
    # 删除用户的逻辑
    pass
```

## 常见误区和注意事项

### 1. 参数位置的误解
```python
# ❌ 错误：试图在装饰器函数中直接加参数
def wrong_decorator(func, char):
    pass

# ✅ 正确：使用装饰器工厂
def correct_decorator(char):
    def decorator(func):
        pass
    return decorator
```

### 2. 忘记返回装饰器
```python
def get_decorator(char):
    def decorator(func):
        def inner():
            print(char * 30)
            func()
        return inner
    # ❌ 忘记返回装饰器
    # return decorator  # 必须有这一行
```

### 3. 混淆调用时机
```python
# @get_decorator  # ❌ 错误：这是函数本身，不是调用
@get_decorator()  # ✅ 正确：这是函数调用，返回装饰器
```

## 总结

带参数的装饰器是Python中的一个重要概念，它的核心思想是：

1. **装饰器工厂模式**：外层函数接收参数，返回真正的装饰器
2. **三层结构**：参数接收层 → 装饰器层 → 装饰后函数层
3. **执行顺序**：先调用工厂函数获取装饰器，再用装饰器装饰目标函数

**关键要点：**
- `@` 后面必须是装饰器函数，不能是其他类型
- `@get_decorator(param)` 会先执行 `get_decorator(param)` 获取装饰器
- 带参数的装饰器可以大大减少代码重复，提高代码复用性

**实践建议：**
- 当你发现自己在写多个相似的装饰器时，考虑使用带参数的装饰器
- 合理设计参数，让装饰器既灵活又易用
- 注意处理边界情况和参数验证

掌握了带参数的装饰器，你就能写出更加灵活和强大的Python代码。在实际项目中，这种模式经常用于日志记录、权限控制、性能监控等场景，是Python高级编程中不可或缺的技能。

---

**下期预告：** 我们将学习装饰器的更高级用法：类装饰器和装饰器的组合使用。敬请期待！

如果这篇文章对你有帮助，欢迎点赞、转发、关注！有任何问题也欢迎在评论区讨论。
