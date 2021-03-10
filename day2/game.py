import random
rannum = random.randint(1, 10000)
counter = 0
gold = 0
print("————————————————猜字游戏————————————————")
print("一共可猜10次，猜对奖励200金币")
print("现有金币：", gold)

while counter < 10:
    num = input("请输入您要猜的数字：")
    num = int(num)
    counter += 1
    if num > rannum:
        print("大了！第", counter, "次")
    elif num < rannum:
        print("小了！第", counter, "次")
    else:
        print("恭喜，猜对了！数字为：", rannum, "用了", counter, "次")
        gold += 200
        print("金币增加200，现有：", gold)
        break
    print("只能猜10次")