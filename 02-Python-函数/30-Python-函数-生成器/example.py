# -*- coding: utf-8 -*-

# @Time    : 2025-5-30
# @Author  : 程序员NEO
# @FileName: example.py
# @Software: VSCode
# @Email   : it666@linux.do
# @Github  : https://github.com/BNTang
# @Description: 30-Python-函数-生成器

"""
Python 生成器 (Generator) 学习笔记
=====================================

生成器是什么？
- 生成器是一种特殊的迭代器
- 抽象层次更高的迭代器
- 具备迭代器的所有特性，但更加优雅

迭代器的三大特性：
1. 惰性计算数据，节省内存
2. 记录状态，通过next()访问下一个状态
3. 具备可迭代特性（可用for循环遍历）
"""

print("=" * 50)
print("1. 迭代器 vs 普通列表 - 内存对比")
print("=" * 50)

# 普通列表 - 一次性加载所有数据到内存
def create_large_list():
    """创建大列表 - 占用大量内存"""
    return [x for x in range(1000000)]  # 一次性创建100万个数字

# 迭代器 - 惰性计算，按需生成
def create_large_iterator():
    """创建大迭代器 - 节省内存"""
    return (x for x in range(1000000))  # 生成器表达式

# 演示内存差异
print("普通列表会一次性占用大量内存")
print("迭代器只在需要时才生成数据，节省内存\n")

print("=" * 50)
print("2. 生成器的创建方式")
print("=" * 50)

# 方式1：生成器函数（使用yield关键字）
def simple_generator():
    """简单生成器函数"""
    print("生成第一个值")
    yield 1
    print("生成第二个值")
    yield 2
    print("生成第三个值")
    yield 3

print("方式1：生成器函数（使用yield）")
gen1 = simple_generator()
print(f"生成器对象：{gen1}")
print("逐个获取值：")
print(next(gen1))
print(next(gen1))
print(next(gen1))
print()

# 方式2：生成器表达式
print("方式2：生成器表达式")
gen2 = (x ** 2 for x in range(5))
print(f"生成器对象：{gen2}")
print("转换为列表查看：", list(gen2))
print()

print("=" * 50)
print("3. 生成器的状态记录特性")
print("=" * 50)

def fibonacci_generator(n):
    """斐波那契数列生成器 - 演示状态记录"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("斐波那契数列生成器（记录状态）：")
fib_gen = fibonacci_generator(8)
for i, value in enumerate(fib_gen):
    print(f"第{i+1}个数：{value}")
print()

print("=" * 50)
print("4. 生活中的例子 - 吃西瓜类比")
print("=" * 50)

class WatermelonEater:
    """西瓜吃货类 - 演示惰性计算"""
    
    def __init__(self, total_melons):
        self.total_melons = total_melons
        self.current_melon = 0
    
    def eat_all_at_once(self):
        """一次性抱所有西瓜（占用大量空间）"""
        melons = [f"西瓜{i+1}" for i in range(self.total_melons)]
        print(f"一次性抱了{len(melons)}个西瓜，手都拿不下了！")
        return melons
    
    def eat_one_by_one(self):
        """一个一个吃西瓜（生成器方式）"""
        for i in range(self.total_melons):
            melon = f"西瓜{i+1}"
            print(f"拿了{melon}，吃完后扔掉")
            yield melon

print("对比两种吃西瓜方式：")
eater = WatermelonEater(5)

print("\n传统方式（占用大量空间）：")
all_melons = eater.eat_all_at_once()

print("\n生成器方式（按需取用）：")
melon_gen = eater.eat_one_by_one()
for melon in melon_gen:
    print(f"正在享用：{melon}")
print()

print("=" * 50)
print("5. 实际应用 - 学生管理系统")
print("=" * 50)

class StudentClass:
    """班级类 - 使用生成器管理学生"""
    
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
    
    def add_student(self, name):
        """添加学生"""
        self.students.append(name)
    
    def get_students_traditional(self):
        """传统方式 - 返回所有学生列表"""
        return self.students.copy()  # 复制整个列表
    
    def get_students_generator(self):
        """生成器方式 - 按需生成学生"""
        for student in self.students:
            print(f"叫到了：{student}")
            yield student

# 创建班级并添加学生
my_class = StudentClass("Python学习班")
students = ["张三", "李四", "王五", "赵六", "田七"]
for student in students:
    my_class.add_student(student)

print(f"班级：{my_class.class_name}")
print(f"学生总数：{len(my_class.students)}")

print("\n传统方式点名（一次性获取所有学生）：")
all_students = my_class.get_students_traditional()
print(f"获取到所有学生：{all_students}")

print("\n生成器方式点名（按需叫学生）：")
student_gen = my_class.get_students_generator()
for i, student in enumerate(student_gen):
    print(f"第{i+1}个学生：{student}")
    if i == 2:  # 只叫前3个学生
        print("暂停点名...")
        break
print()

print("=" * 50)
print("6. 生成器 vs 迭代器关系总结")
print("=" * 50)

print("""
关系类比：
- 生成器 是 迭代器 （生成器是特殊的迭代器）
- 就像：人 是 动物 （人是特殊的动物）

但反过来不成立：
- 迭代器 不一定是 生成器
- 就像：动物 不一定是 人 （动物可能是狗、猫等）

抽象层级：
- 迭代器：抽象层级更高（like 动物）
- 生成器：更加具体化（like 人）

优势对比：
- 迭代器：功能强大，但实现复杂（需要实现__iter__和__next__方法）
- 生成器：功能同样强大，但实现简单（只需yield关键字）
""")

print("=" * 50)
print("7. 生成器的优势总结")
print("=" * 50)

def demonstrate_generator_advantages():
    """演示生成器的优势"""
    
    # 1. 内存效率
    print("✓ 内存效率：惰性计算，按需生成")
    
    # 2. 状态保持
    print("✓ 状态保持：自动记录执行位置")
    
    # 3. 简洁优雅
    print("✓ 代码简洁：yield关键字即可实现")
    
    # 4. 可迭代性
    print("✓ 可迭代：支持for循环和next()函数")

demonstrate_generator_advantages()

print("\n学习重点：")
print("1. 生成器是特殊的迭代器，抽象层次更高")
print("2. 使用yield关键字创建生成器函数")
print("3. 生成器具备惰性计算、状态记录、可迭代三大特性")
print("4. 相比手动实现迭代器，生成器更加简洁优雅")
print("5. 适用于处理大量数据或需要按需生成数据的场景")
