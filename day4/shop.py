user = 'root'
password = 'admin'
count = 0
coin = 0
coupon = [
    ["免单券", 6], ["免半券", 3], ["满600减100券", 50], ["满10000减1000券", 10], ["无券", 999],
]

while count < 3:
    print("请输入用户名：")
    _user = input()
    print("请输入密码：")
    _password = input()
    if _user != user or _password != password:
        print("登陆失败，您一共有三次机会")
        count = count + 1

    else:
        print("成功登陆")

        break
shop = [
    ["油条", 1],
    ["馄饨", 10],
    ["包子", 2],
    ["炒肝", 20],
    ["焦圈", 3],
    ["豆汁", 8]
]
salary = int(input("请输入您的初始资金："))

print("恭喜您获得优惠券，请进入系统后查看")
mycat = []

while True:

    for index, value in enumerate(shop):
        print(index, value)

    num = input("亲输入您要的商品编号：")

    if num.isdigit():

        num = int(num)
        if num in range(len(shop)):
            if salary >= shop[num][1]:

                mycat.append(shop[num])

                salary = salary - shop[num][1]
                coin = coin + shop[num][1]
                print("\033[32;20;1m购买成功！您的余额为：", salary, "￥！\033[0m", "积分为：", coin)
            else:
                print("\033[41;20;1m对不起，您的余额不支持买改商品！穷鬼！\033[0m")
        else:
            print("该商品不存在！别瞎弄！")
    elif num == "Q" or num == "q":
        print("欢迎下次光临！")
        break
    else:
        print("输入非法，请重新输入！")

print("您的购买内容为：")
for index, value in enumerate(mycat):
    print(index, ":", value)
print("------------您的余额：", salary, "积分为：", coin, "------------------")
