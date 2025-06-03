# Python文件操作 - 创建目录详解

## 前言

在Python编程中，文件和目录操作是基础且重要的技能。今天我们来详细学习如何使用Python创建目录，重点掌握`os.mkdir()`函数的使用方法和注意事项。

## 核心函数介绍

### os.mkdir() 函数

`os.mkdir()`是Python中用于创建目录的基础函数，其语法结构如下：

```python
os.mkdir(path, mode=0o777)
```

**参数说明：**
- `path`：要创建的目录路径（必需参数）
- `mode`：目录权限模式（可选参数，默认为0o777）

## 基础用法演示

让我们从最简单的例子开始：

### 1. 创建单个目录

```python
import os

# 创建名为 'a' 的目录
os.mkdir("a")
```

运行这段代码后，你会发现在当前目录下成功创建了一个名为 'a' 的文件夹。

### 2. 处理异常情况

在实际开发中，我们需要考虑各种异常情况。比如目录已存在、权限不足等问题：

```python
import os

try:
    os.mkdir("a")
    print("✓ 成功创建目录 'a'")
except FileExistsError:
    print("⚠ 目录 'a' 已存在")
except Exception as e:
    print(f"✗ 创建失败: {e}")
```

这样的写法更加安全，能够优雅地处理各种异常情况。

## 重要限制和注意事项

### 不支持多级目录创建

这是初学者经常遇到的问题。`os.mkdir()`只能创建单级目录，无法直接创建多级目录结构：

```python
# ❌ 这样写会报错
try:
    os.mkdir("b/c/d")  # 系统找不到指定的路径
except FileNotFoundError:
    print("✗ 失败: 无法创建多级目录，父目录不存在")
```

**为什么会报错？**

因为`os.mkdir()`只能创建最后一级目录，但前提是父目录必须存在。在上面的例子中，要创建目录'd'，必须先有目录'b'和'c'，但它们并不存在。

### 重复创建已存在目录

如果尝试创建一个已经存在的目录，会抛出`FileExistsError`异常：

```python
# 假设目录 'a' 已经存在
try:
    os.mkdir("a")
except FileExistsError:
    print("✗ 失败: 目录已存在，无法重复创建")
```

## 进阶用法：权限模式

### mode参数详解

`mode`参数用于设置目录的权限，采用八进制数字表示：

```python
os.mkdir("b", mode=0o777)
```

**权限系统说明：**

权限分为三组用户：
1. **文件拥有者**（Owner）
2. **同组用户**（Group）  
3. **其他用户**（Others）

每组用户都有三种权限：
- **读权限**：4
- **写权限**：2
- **执行权限**：1

**常用权限组合：**
- `7 = 4+2+1`：读写执行全部权限
- `6 = 4+2`：读写权限
- `5 = 4+1`：读执行权限
- `4`：只读权限

**实际例子：**
- `0o777`：所有用户都有读写执行权限
- `0o755`：拥有者有读写执行权限，其他用户有读执行权限
- `0o644`：拥有者有读写权限，其他用户只有读权限

### 实际应用场景

```python
# 创建一个只有拥有者能操作的私有目录
os.mkdir("private_dir", mode=0o700)

# 创建一个大家都能访问的公共目录
os.mkdir("public_dir", mode=0o755)
```

**注意：** 在Windows系统中，`mode`参数通常被忽略，因为Windows的权限系统与Unix/Linux不同。

## 实用技巧：安全创建函数

为了更好地处理各种异常情况，我们可以封装一个安全的目录创建函数：

```python
def safe_mkdir(path, mode=0o777):
    """
    安全创建目录函数，处理各种异常情况
    """
    try:
        os.mkdir(path, mode)
        print(f"✓ 成功创建目录: {path}")
        return True
    except FileExistsError:
        print(f"⚠ 目录已存在: {path}")
        return False
    except FileNotFoundError:
        print(f"✗ 父目录不存在: {path}")
        return False
    except PermissionError:
        print(f"✗ 权限不足: {path}")
        return False
    except Exception as e:
        print(f"✗ 创建失败: {path}, 错误: {e}")
        return False

# 使用示例
safe_mkdir("test_dir")
safe_mkdir("existing_dir")  # 如果已存在，会给出友好提示
```

这个函数的优势在于：
1. **异常处理完善**：涵盖了常见的各种错误情况
2. **用户友好**：提供清晰的错误信息
3. **返回值明确**：通过返回值判断操作是否成功

## 扩展知识

### 创建多级目录的解决方案

如果确实需要创建多级目录，可以使用`os.makedirs()`：

```python
# 创建多级目录
os.makedirs("a/b/c/d", exist_ok=True)
```

`exist_ok=True`参数表示如果目录已存在不报错。

### 目录操作的完整流程

在实际项目中，通常需要配合其他操作：

```python
import os

# 1. 检查目录是否存在
if not os.path.exists("my_project"):
    # 2. 不存在则创建
    os.mkdir("my_project")
    print("项目目录创建成功")
else:
    print("项目目录已存在")

# 3. 切换到新目录
os.chdir("my_project")
print(f"当前工作目录: {os.getcwd()}")
```

## 总结

通过本文的学习，我们掌握了以下核心要点：

1. **基础用法**：`os.mkdir(path)`用于创建单级目录
2. **重要限制**：不支持多级目录创建，父目录必须存在
3. **异常处理**：必须处理`FileExistsError`等异常情况
4. **权限设置**：通过`mode`参数控制目录权限（主要在Unix/Linux系统中有效）
5. **最佳实践**：封装安全的创建函数，提供完善的错误处理

在日常开发中，建议优先使用带异常处理的版本，这样能让程序更加健壮和用户友好。对于需要创建多级目录的场景，记住使用`os.makedirs()`而不是`os.mkdir()`。

掌握这些基础的目录操作技能，将为后续的文件处理和项目开发打下坚实的基础。

---

*本文是Python文件操作系列教程的一部分，更多精彩内容敬请关注后续更新。*
