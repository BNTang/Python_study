# Python文件操作 - 判定文件是否可读

## 前言

在Python文件操作中，我们经常会遇到这样的问题：当我们尝试读取一个文件时，程序突然报错了。错误信息告诉我们"不支持的操作"或者"文件不可读"。

这是为什么呢？今天我们就来学习一个重要的知识点：**如何判定文件是否可读**。

## 为什么需要判定文件是否可读？

### 问题的由来

让我们先看一个简单的例子：

```python
# 创建一个测试文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("12345\n这是测试内容")

# 尝试读取文件内容
with open("test.txt", "a", encoding="utf-8") as f:
    content = f.read()  # 这里会报错！
    print(content)
```

运行这段代码，你会发现程序直接崩溃了，报错信息是："不支持的操作"。

**为什么会这样？**

原因很简单：我们用的是 `"a"` 模式（追加模式）打开文件，而追加模式只允许写入，不允许读取。但我们却尝试用 `f.read()` 来读取内容，这就产生了冲突。

### 问题的严重性

在实际开发中，这种错误是非常危险的，因为：

1. **程序会崩溃**：一旦报错，后续的代码都无法执行
2. **用户体验差**：用户看到程序突然停止工作
3. **难以调试**：在复杂的项目中，这种错误可能很难定位

## 解决方案：使用 readable() 方法

Python为我们提供了一个非常实用的方法：`file.readable()`

### 基本用法

```python
with open("test.txt", "a", encoding="utf-8") as f:
    if f.readable():
        content = f.read()
        print(content)
    else:
        print("文件不可读，跳过读取操作")
```

`readable()` 方法的返回值：
- `True`：文件可读
- `False`：文件不可读

### 不同文件模式的可读性

让我们来测试一下不同文件打开模式的可读性：

```python
# 读取模式 - 可读
with open("test.txt", "r", encoding="utf-8") as f:
    print(f"读取模式(r): {f.readable()}")  # True

# 写入模式 - 不可读
with open("test.txt", "w", encoding="utf-8") as f:
    print(f"写入模式(w): {f.readable()}")  # False

# 追加模式 - 不可读
with open("test.txt", "a", encoding="utf-8") as f:
    print(f"追加模式(a): {f.readable()}")  # False

# 读写模式 - 可读
with open("test.txt", "r+", encoding="utf-8") as f:
    print(f"读写模式(r+): {f.readable()}")  # True
```

## 容错处理的重要性

### 对比：有无容错处理

**不使用容错处理的代码（危险）：**

```python
with open("test.txt", "a", encoding="utf-8") as f:
    content = f.read()  # 直接崩溃！
    print(content)
print("这行代码永远不会执行")
```

**使用容错处理的代码（安全）：**

```python
with open("test.txt", "a", encoding="utf-8") as f:
    if f.readable():
        content = f.read()
        print(content)
    else:
        print("文件不可读，程序正常继续执行")
print("这行代码会正常执行")  # 程序继续运行
```

### 容错处理的核心思想

在编程中，有一个重要的原则：

> **你可以让代码执行起来没有效果，但绝对不能让它报错崩溃**

因为一旦程序崩溃，会影响后续所有代码的执行，这在生产环境中是绝对不能接受的。

## 实际应用：安全的文件读取函数

基于以上知识点，我们可以封装一个更加健壮的文件读取函数：

### 基础版本

```python
def safe_read_file(filename):
    """安全读取文件内容"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            if f.readable():
                return f.read()
            else:
                print(f"警告: 文件 {filename} 不可读")
                return None
    except FileNotFoundError:
        print(f"错误: 文件 {filename} 不存在")
        return None
    except Exception as e:
        print(f"错误: 读取文件时发生异常 - {e}")
        return None
```

### 增强版本

```python
def safe_read_file(filename, mode="r"):
    """
    安全读取文件的函数
    
    Args:
        filename: 文件名
        mode: 打开模式
    
    Returns:
        文件内容或None
    """
    try:
        with open(filename, mode, encoding="utf-8") as f:
            if f.readable():
                return f.read()
            else:
                print(f"警告: 文件 {filename} 在 {mode} 模式下不可读")
                return None
    except FileNotFoundError:
        print(f"错误: 文件 {filename} 不存在")
        return None
    except Exception as e:
        print(f"错误: 读取文件时发生异常 - {e}")
        return None
```

### 使用示例

```python
# 测试不同场景
result1 = safe_read_file("test.txt", "r")    # 正常读取
result2 = safe_read_file("test.txt", "a")    # 模式不可读
result3 = safe_read_file("不存在.txt", "r")   # 文件不存在

print(f"读取模式结果: {result1}")
print(f"追加模式结果: {result2}")
print(f"不存在文件结果: {result3}")
```

## 文件操作模式总结

| 模式 | 说明 | 可读性 | 可写性 |
|------|------|--------|--------|
| `r` | 只读模式 | ✅ | ❌ |
| `w` | 写入模式 | ❌ | ✅ |
| `a` | 追加模式 | ❌ | ✅ |
| `r+` | 读写模式 | ✅ | ✅ |
| `w+` | 读写模式 | ✅ | ✅ |
| `a+` | 读写模式 | ✅ | ✅ |

## 最佳实践建议

1. **养成检查习惯**：在读取文件前，先检查文件是否可读
2. **完善异常处理**：结合 try-except 和 readable() 双重保护
3. **提供友好提示**：当文件不可读时，给出清晰的提示信息
4. **保持程序健壮**：确保程序在任何情况下都不会崩溃

## 总结

今天我们学习了Python文件操作中的一个重要知识点：**判定文件是否可读**。

核心要点：
- 使用 `file.readable()` 方法判定文件是否可读
- 不同文件打开模式有不同的读写权限
- 容错处理可以提升代码健壮性，避免程序崩溃
- 在文件操作前进行权限检查是良好的编程习惯

记住，在实际开发中，我们不仅要让代码能够工作，更要让它能够优雅地处理各种异常情况。这样才能写出真正专业的代码。

---

*关注我，一起学习更多Python实用技巧！*
