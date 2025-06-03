# Python文件操作：目录相关操作详解

大家好，今天我们来学习Python中关于目录操作的几个重要功能：**获取当前目录**、**改变默认目录**以及**获取目录内容列表**。这些操作在文件处理中非常实用，让我们一步步来掌握它们。

## 1. 获取当前工作目录

在开始之前，我们需要了解一个重要概念：**当前工作目录**。

当我们创建文件时，如果只指定文件名而不指定完整路径，Python会默认在当前工作目录下创建文件。那么，如何知道当前工作目录是什么呢？

```python
import os

# 获取当前工作目录
current_dir = os.getcwd()
print(f"当前目录：{current_dir}")
```

运行这段代码，你会看到类似这样的输出：
```
当前目录：D:\IdeaPro\Python_study\Python-基础\04-Python-文件操作\18-Python-文件操作-其他操作-查看改变列举目录
```

这就是你的Python文件所在的目录，也是默认的工作目录。

## 2. 文件创建的默认行为

让我们通过一个实际例子来理解当前目录的作用：

```python
# 在当前目录创建文件
with open("cc.py", "w", encoding="utf-8") as f:
    f.write("# 这是测试文件")
```

运行这段代码后，你会发现在当前目录下多了一个`cc.py`文件。这说明：
- 当只指定文件名时，文件会创建在当前工作目录下
- 这是相对路径的默认行为

## 3. 在指定目录中创建文件

如果我们想在其他目录中创建文件，有两种方法：

### 方法一：直接指定路径

```python
# 如果a目录不存在，先创建它
if not os.path.exists("a"):
    os.makedirs("a")

# 在a目录下创建文件
with open("a/dd.py", "w", encoding="utf-8") as f:
    f.write("# 这是在a目录下的文件")
```

这种方法简单直接，通过路径前缀指定目标目录。

### 方法二：改变当前工作目录

```python
# 保存原来的目录
original_dir = os.getcwd()
print(f"原目录：{original_dir}")

# 切换到a目录
os.chdir("a")
print(f"切换后的目录：{os.getcwd()}")

# 现在在a目录下创建文件
with open("ee.py", "w", encoding="utf-8") as f:
    f.write("# 切换目录后创建的文件")

# 切换回原目录
os.chdir(original_dir)
print(f"恢复到：{os.getcwd()}")
```

这种方法的优势是：
- 一旦切换目录，后续的所有相对路径操作都会基于新目录
- 适合需要在同一目录下进行多个操作的场景

⚠️ **注意**：使用`os.chdir()`时记得保存原目录路径，以便后续恢复。

## 4. 列举目录内容

有时我们需要查看某个目录下有哪些文件和文件夹，这时可以使用`os.listdir()`：

### 基础用法

```python
# 列举当前目录内容
contents = os.listdir(".")
print("当前目录内容：", contents)

# 列举指定目录内容
a_contents = os.listdir("a")
print("a目录内容：", a_contents)
```

### 特殊路径符号

Python中有两个特殊的路径符号：

- **`.`** ：表示当前目录
- **`..`** ：表示上级目录

```python
# 当前目录
current = os.listdir(".")
print("当前目录：", current)

# 上级目录
try:
    parent = os.listdir("..")
    print("上级目录：", parent[:5])  # 只显示前5个
except Exception as e:
    print(f"无法访问上级目录：{e}")
```

## 5. 重要知识点总结

通过今天的学习，我们掌握了以下重要概念：

| 函数/符号 | 作用 | 示例 |
|----------|------|------|
| `os.getcwd()` | 获取当前工作目录 | `current = os.getcwd()` |
| `os.chdir(path)` | 改变当前工作目录 | `os.chdir("a")` |
| `os.listdir(path)` | 列举目录内容 | `files = os.listdir(".")` |
| `.` | 当前目录 | `os.listdir(".")` |
| `..` | 上级目录 | `os.listdir("..")` |

## 6. 实用技巧

1. **相对路径基准**：所有相对路径都是相对于当前工作目录的
2. **返回值类型**：`os.listdir()`返回的是列表，包含文件名和目录名
3. **深度限制**：`listdir()`只列举一级目录内容，不会递归遍历子目录
4. **目录切换**：使用`os.chdir()`时要注意保存和恢复原目录

## 完整示例代码

```python
# -*- coding: utf-8 -*-

import os

print("=== Python文件操作：目录相关操作 ===\n")

# 1. 获取当前工作目录
print("1. 获取当前工作目录：")
current_dir = os.getcwd()
print(f"当前目录：{current_dir}\n")

# 2. 在当前目录创建文件
print("2. 在当前目录创建文件：")
with open("cc.py", "w", encoding="utf-8") as f:
    f.write("# 这是在当前目录创建的文件")
print("创建文件：cc.py\n")

# 3. 创建目录并在其中创建文件
print("3. 创建目录并在其中创建文件：")
if not os.path.exists("a"):
    os.makedirs("a")
    print("创建目录：a")

# 方法1：直接指定路径创建文件
with open("a/dd.py", "w", encoding="utf-8") as f:
    f.write("# 这是在a目录下创建的文件")
print("在a目录下创建文件：dd.py\n")

# 4. 改变当前目录
print("4. 改变当前目录：")
original_dir = os.getcwd()
os.chdir("a")
print(f"切换后的当前目录：{os.getcwd()}")

# 在新目录下创建文件
with open("ee.py", "w", encoding="utf-8") as f:
    f.write("# 这是切换目录后创建的文件")
print("在a目录下创建文件：ee.py")

# 恢复到原目录
os.chdir(original_dir)
print(f"恢复到原目录：{os.getcwd()}\n")

# 5. 列举目录内容
print("5. 列举目录内容：")

# 列举当前目录（使用 "." 表示当前目录）
print("当前目录内容（使用 '.'）：")
current_contents = os.listdir(".")
print(current_contents)
print()

# 列举a目录内容
print("a目录内容：")
a_contents = os.listdir("a")
print(a_contents)
print()

# 列举上级目录（使用 ".." 表示上级目录）
print("上级目录内容（使用 '..'）：")
try:
    parent_contents = os.listdir("..")
    print(parent_contents[:5])  # 只显示前5个，避免输出过多
    print("...")
except Exception as e:
    print(f"无法访问上级目录：{e}")

print("\n=== 目录操作核心要点 ===")
print("• os.getcwd() - 获取当前工作目录")
print("• os.chdir(path) - 改变当前工作目录")
print("• os.listdir(path) - 列举指定目录的内容")
print("• '.' - 表示当前目录")
print("• '..' - 表示上级目录")
print("• 相对路径是相对于当前工作目录的")
print("• listdir()返回的是列表，只列举一级目录内容")
```

掌握这些目录操作，你就能更灵活地处理文件路径问题了。在实际项目中，这些技能会让你的文件操作更加得心应手！

---

*今天的分享就到这里，如果你觉得有用，别忘了点赞和转发哦！有问题欢迎在评论区讨论。*
