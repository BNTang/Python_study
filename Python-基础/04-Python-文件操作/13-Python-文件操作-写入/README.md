# Python文件操作系列 | 写入操作详解

大家好，我是程序员NEO！

在前面的文章中，我们学习了Python文件的读取操作。今天我们来看看文件的写入操作，这个相对来说比较简单，因为我们之前就一直在使用。

## 基础写入操作

首先，我们来看最基本的文件写入方式：

```python
# 最简单的写入方式
f = open("a.txt", "a")  # 以追加模式打开文件
result = f.write("abc")  # 写入内容
print(result)  # 打印返回值
f.close()  # 关闭文件
```

运行这段代码，你会发现控制台输出了数字 `3`。

这里有个重要知识点：**write() 方法的返回值是写入内容的字节长度**，而不是文件的总长度。

让我们验证一下，再次运行相同的代码：

```python
f = open("a.txt", "a")
result = f.write("abc")  # 再次写入abc
print(result)  # 仍然是3，不是6
f.close()
```

虽然文件中现在有 `abcabc`（总共6个字符），但返回值依然是3，因为这次只写入了3个字节。

## 添加容错处理

作为一个严谨的程序员，我们需要考虑异常情况。如果文件无法写入怎么办？

我们可以使用 `writable()` 方法来检查文件是否可写：

```python
f = open("a.txt", "a")
if f.writable():  # 检查是否可写
    result = f.write("abc")
    print(f"写入成功，字节数：{result}")
else:
    print("文件不可写")
f.close()
```

让我们测试一下只读模式：

```python
f = open("a.txt", "r")  # 以只读模式打开
if f.writable():
    result = f.write("abc")
    print(f"写入成功，字节数：{result}")
else:
    print("只读模式 - 文件不可写，跳过写入操作")
f.close()
```

运行后你会看到输出 "只读模式 - 文件不可写，跳过写入操作"，这样就避免了程序出错。

## 不同写入模式的区别

Python文件操作有不同的模式，对写入行为有不同影响：

### 1. 'w' 模式 - 覆盖写入

```python
# 第一次写入
with open("test_w.txt", "w") as f:
    result = f.write("第一行内容\n")
    print(f"写入字节数: {result}")

# 第二次写入 - 会覆盖之前的内容
with open("test_w.txt", "w") as f:
    result = f.write("新内容")
    print(f"覆盖写入字节数: {result}")
```

使用 'w' 模式时，每次打开文件都会清空原有内容，然后写入新内容。

### 2. 'a' 模式 - 追加写入

```python
# 第一次写入
with open("test_a.txt", "a") as f:
    result = f.write("第一行内容\n")
    print(f"写入字节数: {result}")

# 第二次写入 - 在末尾追加
with open("test_a.txt", "a") as f:
    result = f.write("追加内容\n")
    print(f"追加写入字节数: {result}")
```

使用 'a' 模式时，新内容会添加到文件末尾，不会覆盖原有内容。

## 最佳实践 - 使用with语句

从上面的代码你可能注意到，我开始使用 `with` 语句了。这是Python文件操作的最佳实践：

```python
# 推荐的写入方式
filename = "best_practice.txt"

try:
    with open(filename, "w", encoding="utf-8") as f:
        if f.writable():
            content = "这是使用with语句的最佳实践示例\n包含中文内容测试"
            result = f.write(content)
            print(f"使用with语句写入成功，字节数: {result}")
        else:
            print("文件不可写")
except IOError as e:
    print(f"文件操作错误: {e}")
```

使用 `with` 语句的好处：

1. **自动关闭文件**：无需手动调用 `close()`
2. **异常安全**：即使出错也会正确关闭文件
3. **代码更简洁**：减少重复代码

## 知识点总结

通过今天的学习，我们掌握了以下重点：

1. **write() 方法返回写入内容的字节长度**，不是文件总长度
2. **使用 writable() 检查文件是否可写**，提高代码健壮性
3. **'w' 模式会覆盖原有内容，'a' 模式会追加内容**
4. **推荐使用 with 语句自动管理文件关闭**
5. **添加适当的异常处理**让程序更稳定

## 写在最后

文件写入操作看起来简单，但细节很重要。从最初的基础写法，到添加容错处理，再到使用 with 语句的最佳实践，这就是我们编程水平提升的过程。

记住：好的代码不仅要能运行，还要健壮、优雅、易维护。

下期预告：我们将学习Python文件操作的高级技巧，包括文件指针操作和二进制文件处理。

---

**关注我，持续分享Python实用技巧！**

如果觉得有帮助，别忘了点赞、转发支持一下～
