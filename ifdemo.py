fraction = input("请输入您的分数:")
fraction = int(fraction)

if fraction >= 90 & fraction >= 100:
    print("优秀！")
elif fraction >= 80 & fraction <= 90:
    print("良好！")
elif fraction >= 70 & fraction <= 80:
    print("一般！")
elif fraction >= 60 & fraction <= 70:
    print("及格！")
elif fraction >= 0 & fraction <= 60:
    print("不及格！")
else:
    print("输入非法")