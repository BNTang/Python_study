# Python分支循环结构综合案例

在掌握了Python的基本语法、分支和循环结构后，我们来通过两个实际案例来巩固所学知识，提升编程能力。

## 案例一：水仙花数判断

**什么是水仙花数？**
水仙花数（Narcissistic number）是指一个三位数，其各位数字的立方和等于该数本身。例如：153 是一个水仙花数，因为 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153。

**案例需求：**
1. 用户输入一个数值
2. 验证是否是三位数（100-999）
3. 判断是否是水仙花数

**实现思路：**
1. 获取用户输入
2. 检查是否为三位数
3. 分别计算百位、十位和个位数字
4. 计算各位数字的立方和并与原数比较

**代码实现：**

```python
# 获取用户输入
num = int(input("请输入一个三位数："))

# 判断是否是三位数
if 100 <= num <= 999:
    # 分别获取百位、十位和个位
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
    
    # 计算各位数字的立方和
    sum_of_cubes = hundreds**3 + tens**3 + ones**3
    
    # 判断是否是水仙花数
    if sum_of_cubes == num:
        print(f"{num}是水仙花数！")
    else:
        print(f"{num}不是水仙花数！")
else:
    print("请输入一个三位数！")
```

**代码解析：**
- `num // 100` 获取百位数字
- `(num // 10) % 10` 获取十位数字
- `num % 10` 获取个位数字
- 通过 `**3` 计算每个数字的立方
- 最后比较立方和与原数是否相等

以153为例，我们可以验证：
- 百位：1，1^3 = 1
- 十位：5，5^3 = 125
- 个位：3，3^3 = 27
- 1 + 125 + 27 = 153，等于原数，所以153是水仙花数

**扩展思考：**
我们还可以编写一个程序，自动找出所有的三位水仙花数：

```python
print("所有的三位水仙花数有：")
for num in range(100, 1000):
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
    
    if hundreds**3 + tens**3 + ones**3 == num:
        print(num, end=" ")
```

## 案例二：猜数字游戏

**游戏规则：**
1. 程序内部预设一个数字（比如500）
2. 用户通过输入数值来猜这个数字
3. 如果猜对了，游戏结束
4. 如果猜错了，程序会提示数字是"大了"还是"小了"
5. 用户可以继续猜，直到猜对为止

**实现思路：**
1. 设置一个目标数字
2. 使用循环让用户反复猜测
3. 根据用户的输入给出相应的提示
4. 猜对后结束程序

**代码实现：**

```python
import random  # 导入随机数模块

# 设置目标数字（1-1000之间的随机数）
target_number = random.randint(1, 1000)
guess_count = 0  # 记录猜测次数

print("欢迎参加猜数字游戏！")
print("我已经想好了一个1-1000之间的数字，请你来猜一猜。")

while True:
    # 获取用户猜测的数字
    user_guess = int(input("请输入你猜的数字："))
    guess_count += 1
    
    # 判断猜测结果
    if user_guess == target_number:
        print(f"恭喜你，猜对了！目标数字就是{target_number}")
        print(f"你总共猜了{guess_count}次")
        break
    elif user_guess > target_number:
        print("猜大了，请继续猜！")
    else:
        print("猜小了，请继续猜！")
```

**代码解析：**
- 使用`random.randint(1, 1000)`生成1-1000之间的随机数
- `while True`创建一个无限循环，直到用户猜对为止
- 通过比较用户输入与目标数字的大小，给出相应提示
- 当用户猜对后，使用`break`退出循环，结束游戏

**优化版本：**
我们可以添加一些功能来增强游戏体验：
1. 限制猜测次数
2. 记录最高分（最少猜测次数）

```python
import random

def guess_game():
    target_number = random.randint(1, 1000)
    max_attempts = 10
    guess_count = 0
    
    print("欢迎参加猜数字游戏！")
    print(f"我已经想好了一个1-1000之间的数字，你有{max_attempts}次机会来猜一猜。")
    
    while guess_count < max_attempts:
        user_guess = int(input(f"第{guess_count+1}次猜测，请输入你猜的数字："))
        guess_count += 1
        
        if user_guess == target_number:
            print(f"恭喜你，猜对了！目标数字就是{target_number}")
            print(f"你总共用了{guess_count}次就猜出来了！")
            return True
        elif user_guess > target_number:
            print("猜大了，请继续猜！")
        else:
            print("猜小了，请继续猜！")
            
    print(f"很遗憾，你已用完{max_attempts}次机会。正确答案是：{target_number}")
    return False

# 开始游戏
guess_game()
```

## 总结

通过这两个案例，我们综合运用了Python的基本数据类型、输入输出、条件判断和循环控制等知识点。这种实战练习能够帮助我们更好地掌握Python编程技巧，培养解决实际问题的能力。

在实际编程中，我们往往需要将问题分解为多个小步骤，然后逐步实现。通过这种方法，即使是复杂的问题也能被有条理地解决。希望这两个案例能帮助你更好地理解Python的分支循环结构！