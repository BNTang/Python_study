# Python基础 - 分支循环综合案例：水仙花数

## 什么是水仙花数？

水仙花数是指一个三位数，它的每个位上的数字的立方和等于它本身。例如：

153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153

在这个例子中，153正好等于各位数字立方和，所以153是一个水仙花数。

## 问题分析

我们来分析一下如何判断一个数是否为水仙花数：

1. 首先，要确保输入的是一个三位数（100-999之间）
2. 然后，需要提取这个数字的百位、十位和个位
3. 计算这三个数字的立方和
4. 最后，判断立方和是否等于原数

## 实现思路

### 1. 获取用户输入
首先，我们需要获取用户输入的数字：

```python
num_str = input("请输入一个三位数: ")
num = int(num_str)
```

### 2. 验证是否是三位数
接着，我们需要验证输入是否是一个三位数：

```python
if 100 <= num <= 999:
    # 处理三位数
else:
    print("输入错误，请输入一个三位数")
```

### 3. 提取各个位的数字
如果是三位数，我们需要提取它的百位、十位和个位：

```python
hundreds = num // 100       # 百位
tens = (num % 100) // 10    # 十位
ones = num % 10             # 个位
```

### 4. 计算立方和并判断
最后，计算各位数字的立方和，并判断是否等于原数：

```python
sum_of_cubes = hundreds**3 + tens**3 + ones**3
if sum_of_cubes == num:
    print(f"{num} 是水仙花数")
else:
    print(f"{num} 不是水仙花数")
```

## 完整代码

下面是完整的Python代码实现：

```python
# 获取用户输入
num_str = input("请输入一个三位数: ")
num = int(num_str)

# 验证是否是三位数
if 100 <= num <= 999:
    # 提取各个位的数字
    hundreds = num // 100  # 百位
    tens = (num % 100) // 10  # 十位
    ones = num % 10  # 个位
     
    # 计算各位数字的立方和
    sum_of_cubes = hundreds**3 + tens**3 + ones**3
    
    # 判断是否是水仙花数
    if sum_of_cubes == num:
        print(f"{num} 是水仙花数")
    else:
        print(f"{num} 不是水仙花数")
else:
    print("输入错误，请输入一个三位数")
```

## 代码说明

1. `num // 100` 是整除操作，可以得到百位数字
2. `(num % 100) // 10` 先取得后两位（余数），再整除10得到十位数字
3. `num % 10` 直接取余数得到个位数字
4. `**3` 是Python中的幂运算符，用于计算立方

## 扩展思考

在实际编程中，我们还可以做以下优化或扩展：

1. **异常处理**：增加try-except块来处理用户输入非数字的情况
2. **寻找所有水仙花数**：编写一个循环遍历100-999之间所有的数，找出所有的水仙花数
3. **扩展到N位数**：将程序扩展到可以判断任意位数的"自幂数"（每个位上的数字的N次方和等于该数本身）

## 小结

通过这个简单的案例，我们练习了以下Python基础知识：
- 用户输入与类型转换
- 条件判断
- 算术运算（整除、取余、幂运算）
- 字符串格式化输出

水仙花数是一个很好的编程练习，它结合了数学思维和基本的编程技能。尝试自己实现并找出所有的水仙花数吧！

---

> 如果您有任何问题或建议，欢迎在评论区留言，我们一起交流学习！