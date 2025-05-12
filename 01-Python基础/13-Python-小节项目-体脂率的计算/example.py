# 输入部分
height = float(input("请输入您的身高（米，例如1.70）："))
weight = float(input("请输入您的体重（千克）："))
age = int(input("请输入您的年龄："))
gender = int(input("请输入您的性别（男填1，女填0）："))

# 计算 BMI
bmi = weight / (height * height)

# 计算体脂率 (本公式返回的就是百分比)
body_fat = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * gender

# 判定体脂率是否正常
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

# 输出结果
print("您的体脂率为：{:.2f}%".format(body_fat))
print(status)
