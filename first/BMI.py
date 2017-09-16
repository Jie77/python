print("请输入身高:(m)")
height = float(input())
print("请输入体重:(kg)")
weight = float(input())
BMI = weight/(height*height)
print("您的BMI值为:%f" % BMI)
print("国内标准请输1，国际标准请输0:")
choose = input()
if choose == '0':
    sug = "  建议BMI标准范围：18.5 -- 25"
    if BMI >= 30:
        print("肥胖"+sug)
    elif BMI >= 25:
        print("偏胖"+sug)
    elif BMI >= 18.5:
        print("正常"+sug)
    else:
        print("偏瘦"+sug)
else:
    sug = "  建议BMI标准范围：18.5 -- 24"
    if BMI >= 28:
        print("肥胖"+sug)
    elif BMI >= 24:
        print("偏胖"+sug)
    elif BMI >= 18.5:
        print("正常"+sug)
    else:
        print("偏瘦"+sug)
