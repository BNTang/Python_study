# Python_study

本项目为 Python 基础学习与练习项目，包含了分支结构、输入输出、数据处理等基础知识点的代码示例与小节项目。

## 目录结构

- `01-Python基础/`：基础语法、分支、循环等知识点
- `22-Python-分支-优化-13-Python-小节项目-体脂率的计算/`：体脂率计算案例及优化

## 体脂率计算案例

示例代码实现了根据用户输入的身高、体重、年龄和性别，计算 BMI 和体脂率，并根据性别判断体脂率是否在正常范围。

### 主要功能

- 输入数据有效性检查
- BMI 及体脂率计算
- 针对男女的体脂率判定标准
- 健康提示输出

### 示例

```python
height = float(input("请输入您的身高（米，例如1.70）："))
weight = float(input("请输入您的体重（千克）："))
age = int(input("请输入您的年龄："))
gender = int(input("请输入您的性别（男填1，女填0）："))

bmi = weight / (height * height)
body_fat = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * gender

if gender == 1:
    if 15 <= body_fat <= 18:
        status = "您的体脂率在正常范围。"
    else:
        status = "您的体脂率不在正常范围，请注意健康。"
elif gender == 0:
    if 25 <= body_fat <= 28:
        status = "您的体脂率在正常范围。"
    else:
        status = "您的体脂率不在正常范围，请注意健康。"
else:
    status = "性别输入有误，请确认输入是否正确。"

print("您的体脂率为：{:.2f}%".format(body_fat))
print(status)
```

## 适用人群

- Python 初学者
- 需要基础语法练习的学习者

## 运行环境

- Python 3.x

## 贡献

欢迎提交 PR 或 issue 进行交流与改进。
