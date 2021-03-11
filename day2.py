import random

ranNum = random.randint(1, 10000)

while True:
    num = input("请输入您要猜的数字：")
    num = int(num)
    if num > ranNum:
        print("大了！")
    elif num < ranNum:
        print("小了！")
    else:
        print("恭喜，猜对了！数字为：", ranNum)
        break
