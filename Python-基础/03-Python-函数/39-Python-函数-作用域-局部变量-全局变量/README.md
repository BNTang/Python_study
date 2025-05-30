# Python函数作用域详解：局部变量与全局变量

在Python编程中，理解变量作用域是非常重要的基础知识。今天我们来深入学习Python中的两种主要变量类型：**局部变量**和**全局变量**，以及它们的使用规则和注意事项。

## 什么是局部变量？

局部变量是指定义在函数体内部的变量，它的作用范围仅限于该函数内部。

### 基础示例

让我们先来看一个简单的例子：

```python
def test():
    a = 1  # 局部变量
    print(f"函数内部访问局部变量: {a}")

test()  # 输出: 函数内部访问局部变量: 1
```

### 局部变量的特性

1. **只能在函数内部访问**
2. **可以在函数内部修改**
3. **函数外部无法访问**

```python
def test():
    a = 1
    print(f"函数内部访问: {a}")
    
    # 可以修改局部变量
    a = 2
    print(f"修改后的值: {a}")

test()

# 尝试在函数外访问局部变量会报错
try:
    print(a)  # NameError: name 'a' is not defined
except NameError as e:
    print(f"错误：{e}")
```

## Python的LEGB查找规则

Python使用LEGB规则来查找变量，这是一个从内到外的查找顺序：

- **L (Local)**: 局部作用域
- **E (Enclosing)**: 外层函数作用域
- **G (Global)**: 全局作用域
- **B (Built-in)**: 内建作用域

### 嵌套函数示例

```python
def outer_function():
    outer_var = "外层函数变量"  # E作用域
    
    def inner_function():
        print(f"内层函数访问外层变量: {outer_var}")
    
    inner_function()

outer_function()
```

在这个例子中，内层函数可以访问外层函数的变量，这就是LEGB规则在起作用。

## 全局变量详解

全局变量是定义在文件最外层的变量，可以在整个模块的任何地方访问。

### 全局变量的命名规范

建议使用 `g_` 前缀来标识全局变量：

```python
# 推荐的全局变量命名方式
g_global_var = 999
g_name = "全局变量"

def test_global_access():
    print(f"函数内访问全局变量: {g_global_var}")
    print(f"函数内访问全局变量: {g_name}")

test_global_access()
```

### 修改全局变量的正确方式

这里有一个重要的陷阱需要注意：

#### 错误的修改方式

```python
g_counter = 0

def wrong_modify():
    print(f"修改前: {g_counter}")
    g_counter = 100  # 这创建了一个新的局部变量！
    print(f"函数内: {g_counter}")

print(f"全局变量: {g_counter}")  # 0
wrong_modify()
print(f"全局变量未改变: {g_counter}")  # 仍然是 0
```

#### 正确的修改方式

```python
g_counter = 0

def correct_modify():
    global g_counter  # 声明要修改全局变量
    print(f"修改前: {g_counter}")
    g_counter = 100
    print(f"修改后: {g_counter}")

correct_modify()
print(f"全局变量已改变: {g_counter}")  # 100
```

## nonlocal关键字的使用

当我们需要在内层函数中修改外层函数的变量时，使用`nonlocal`关键字：

```python
def outer_with_nonlocal():
    outer_var = "原始值"
    
    def inner_modify():
        nonlocal outer_var  # 声明要修改外层函数的变量
        outer_var = "被内层函数修改"
        print(f"内层函数修改: {outer_var}")
    
    print(f"修改前: {outer_var}")
    inner_modify()
    print(f"修改后: {outer_var}")

outer_with_nonlocal()
```

## 变量查看工具

Python提供了两个有用的函数来查看变量：

```python
def demo_variables():
    local_a = 10
    local_b = 20
    
    print("局部变量:")
    for name, value in locals().items():
        print(f"  {name} = {value}")
    
    print("\n全局变量:")
    for name, value in globals().items():
        if name.startswith('g_'):
            print(f"  {name} = {value}")

demo_variables()
```

## 常见陷阱和注意事项

### 1. 变量定义时机问题

```python
def early_call():
    print(f"early_var = {early_var}")

# early_call()  # 会报错，因为 early_var 还未定义
early_var = "现在定义了"
early_call()  # 现在可以正常调用
```

### 2. 就近原则

当存在同名变量时，Python遵循就近原则：

```python
g_name = "全局变量"

def scope_demo():
    print(f"访问全局变量: {g_name}")
    
    # 定义同名局部变量
    g_name = "局部变量"
    print(f"访问局部变量: {g_name}")

print(f"调用前全局变量: {g_name}")
scope_demo()
print(f"调用后全局变量未变: {g_name}")
```

## 最佳实践总结

### 1. 命名规范
- 全局变量使用 `g_` 前缀
- 局部变量使用清晰的描述性名称

### 2. 变量定义
- 全局变量定义在文件顶部
- 避免在函数中频繁修改全局变量
- 必要时明确使用 `global` 关键字

### 3. 作用域规则
- 记住LEGB查找顺序：Local → Enclosing → Global → Built-in
- 就近原则：优先访问最近作用域的变量
- 使用 `nonlocal` 修改外层函数变量

### 4. 调试技巧
- 使用 `locals()` 查看局部变量
- 使用 `globals()` 查看全局变量
- 注意变量的生命周期和访问时机

## 实际应用建议

在实际编程中，建议：

1. **最小化全局变量的使用**：过多的全局变量会让代码难以维护
2. **优先使用函数参数和返回值**：这样代码更清晰、更容易测试
3. **当确实需要全局状态时**：使用类或者模块级别的配置
4. **保持作用域的清晰性**：避免复杂的嵌套和变量名冲突

理解变量作用域是成为Python高手的必经之路。掌握了这些概念，你就能写出更加清晰、可维护的Python代码！

---

**下期预告：** 我们将学习Python的函数高级特性，包括装饰器、闭包等概念，敬请期待！

如果觉得这篇文章对你有帮助，欢迎点赞转发，让更多的朋友一起学习Python！
