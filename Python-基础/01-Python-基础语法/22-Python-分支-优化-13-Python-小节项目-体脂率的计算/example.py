# 身高范围 · 0<身高<3
# 输入部分容错处理
# 体重 · 0<体重< 300
# 年龄 · 0<年龄< 150
# 性别。 是1或者0
# 案例
# 优化-"体脂率计算"案例
# 数据处理
# 针对男女的判定标准,分别进行判断而不是通过找规律计算出的最大最小值,进行判定
# 输出
# 结果提示优化
# 男皮
# 先生你好女士你好
# 正常/不正常
# 恭喜您,身体非常健康,请继续保持
# 请注意,您的身体偏瘦/胖
# 示例
# 先生你好,请注意,您的身体偏胖

# 输入部分及容错处理
def get_valid_input(prompt, valid_type, min_value, max_value):
    while True:
        try:
            value = valid_type(input(prompt))
            if min_value < value < max_value:
                return value
            else:
                print(f"输入超出范围，请输入{min_value}到{max_value}之间的数值。")
        except ValueError:
            print("输入格式不正确，请重新输入。")

def get_gender_input():
    while True:
        try:
            gender = int(input("请输入您的性别（男填1，女填0）："))
            if gender in [0, 1]:
                return gender
            else:
                print("性别只能是0（女）或1（男），请重新输入。")
        except ValueError:
            print("输入格式不正确，请输入0或1。")

# 获取有效输入
height = get_valid_input("请输入您的身高（米，例如1.70）：", float, 0, 3)
weight = get_valid_input("请输入您的体重（千克）：", float, 0, 300)
age = get_valid_input("请输入您的年龄：", int, 0, 150)
gender = get_gender_input()

# 计算 BMI
bmi = weight / (height * height)

# 计算体脂率 (本公式返回的就是百分比)
body_fat = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * gender

# 判定体脂率是否正常并给出详细建议
if gender == 1:  # 男性
    greeting = "先生您好，"
    if body_fat < 6:
        status = "您的体脂率过低，可能影响健康，请注意适当增加营养摄入。"
    elif 6 <= body_fat < 13:
        status = "您的体脂率偏瘦，但仍在健康范围内，请保持均衡饮食。"
    elif 13 <= body_fat <= 17:
        status = "恭喜您，身体非常健康，体脂率处于理想范围，请继续保持。"
    elif 17 < body_fat <= 25:
        status = "您的体脂率偏高，建议适当增加运动量。"
    else:
        status = "您的体脂率过高，请注意，您的身体偏胖，建议调整饮食并增加运动。"
else:  # 女性
    greeting = "女士您好，"
    if body_fat < 14:
        status = "您的体脂率过低，可能影响健康，请注意适当增加营养摄入。"
    elif 14 <= body_fat < 20:
        status = "您的体脂率偏瘦，但仍在健康范围内，请保持均衡饮食。"
    elif 20 <= body_fat <= 25:
        status = "恭喜您，身体非常健康，体脂率处于理想范围，请继续保持。"
    elif 25 < body_fat <= 32:
        status = "您的体脂率偏高，建议适当增加运动量。"
    else:
        status = "您的体脂率过高，请注意，您的身体偏胖，建议调整饮食并增加运动。"

# 输出结果
print("\n体脂率计算结果:")
print("=" * 40)
print(f"您的BMI指数为：{bmi:.2f}")
print(f"您的体脂率为：{body_fat:.2f}%")
print("-" * 40)
print(f"{greeting}{status}")
print("=" * 40)
