import random
import pymysql

# 确定银行的开户名称
bank_name = "中国工商银行昌平区回龙观支行"

info = '''
    *********************************
    *    中国工商银行账户管理系统     *
    *********************************
    *   1.开户                      *
    *   2.存款                      *
    *   3.取款                      *
    *   4.转账                      *
    *   5.查询账户                   *
    *   6.Bye！                     *
    ********************************
'''


# 银行的开户逻辑
def bank_adduser(account, username, password, country, province, street, door, money):
    con = pymysql.connect(host="localhost", user="root", password="root", database="银行数据库")
    # 通过con连接得到游标（执行sql语句的地方）
    cursor = con.cursor()
    # 准备一条sql语句
    sql = "select * from bank"
    cursor.execute(sql)
    # 查询，从游标里提取数据
    data = cursor.fetchall()
    # 判断用户库是否已满
    if len(data) >= 100:
        return 3

    # 判断是否存在
    # 获取所有键，然后在判断是否有
    for d in data:
        if d[0] == account:
            return 2

    sql2 = "insert into bank  values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = [account, username, password, country, province, street, door, bank_name, money]
    cursor.execute(sql2, param)
    con.commit()
    cursor.close()
    con.close()
    return 1


# 开户逻辑
def adduser():
    # 生成账号：  8位随机
    string = ""  # 随机数缓冲
    for i in range(8):  # 循环8次取字符

        string = string + "1234567890"[random.randint(0, 9)]  # 拼接

    account = string
    print("账号为：", account)
    username = input("请输入姓名：")
    password = input("请输入密码：")
    print("接下来输入地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street = input("\t输入街道：")
    door = input("\t输入门牌号：")
    money = input("请初始化您的余额：")

    # 调用银行的开户方法
    s = bank_adduser(account, username, password, country, province, street, door, money)

    if s == 1:
        print("开户成功！")
        print("以下是您的开户个人信息：")
        print("***********************")
        print("账号：", account)
        print("用户名：", username)
        print("密码：******")
        print("国家：", country)
        print("省份：", province)
        print("街道：", street)
        print("门牌号：", door)
        print("账户余额：", money)
        print("******************开户行地址：", bank_name)

    elif s == 2:
        print("该用户已存在！")
    elif s == 3:
        print("对不起，该银行已满！请携带证件到其他银行办理！")


# 银行的存款逻辑
def bank_deposit(account):
    con = pymysql.connect(host="localhost", user="root", password="root", database="银行数据库")
    # 通过con连接得到游标（执行sql语句的地方）
    cursor = con.cursor()
    # 准备一条sql语句
    sql = "select * from bank"
    cursor.execute(sql)
    # 查询，从游标里提取数据
    data = cursor.fetchall()
    # 账号存在
    for d in data:
        if d[0] == account:
            money = int(input("请输入金额："))
            money = money + int(d[8])
            update = "update bank set 余额='" + str(money) + "' where 账号=" + account
            cursor.execute(update)
            con.commit()
            cursor.close()
            con.close()
            return True

    # 账号不存在
    return False


# 存款逻辑
def deposit():
    account = input("请输入账号：")
    s = bank_deposit(account)

    if s is True:
        con = pymysql.connect(host="localhost", user="root", password="root", database="银行数据库")
        # 通过con连接得到游标（执行sql语句的地方）
        cursor = con.cursor()
        # 准备一条sql语句
        sql = "select * from bank"
        cursor.execute(sql)
        # 查询，从游标里提取数据
        data = cursor.fetchall()
        for d in data:
            if d[0] == account:
                print("存款成功，现有金额：", d[8])
        cursor.close()
        con.close()
    if s is False:
        print("账号不存在")


# 银行的取钱逻辑
def bank_withdraw(account):
    con = pymysql.connect(host="localhost", user="root", password="root", database="银行数据库")
    # 通过con连接得到游标（执行sql语句的地方）
    cursor = con.cursor()
    # 准备一条sql语句
    sql = "select * from bank"
    cursor.execute(sql)
    # 查询，从游标里提取数据
    data = cursor.fetchall()
    # 账号存在
    for d in data:
        if d[0] == account:
            password = input("请输入密码：")
            if d[2] == password:
                money = int(input("请输入金额："))
                if money <= int(d[8]):
                    money = int(d[8]) - money
                    update = "update bank set 余额='" + str(money) + "' where 账号=" + account
                    cursor.execute(update)
                    con.commit()
                    return 0
                else:
                    return 3
            else:
                return 2
    return 1

    cursor.close()
    con.close()


# 取钱逻辑
def withdraw():
    account = input("请输入账号：")
    s = bank_withdraw(account)
    if s == 0:
        con = pymysql.connect(host="localhost", user="root", password="root", database="银行数据库")
        # 通过con连接得到游标（执行sql语句的地方）
        cursor = con.cursor()
        # 准备一条sql语句
        sql = "select * from bank"
        cursor.execute(sql)
        # 查询，从游标里提取数据
        data = cursor.fetchall()
        for d in data:
            if d[0] == account:
                print("取款成功，剩余：", d[8])
        cursor.close()
        con.close()
    elif s == 1:
        print("账号不存在")
    elif s == 2:
        print("密码不正确")
    elif s == 3:
        print("金额不足")


# 银行的转账逻辑
def bank_transfer(out_account, in_account):
    con = pymysql.connect(host="localhost", user="root", password="root", database="银行数据库")
    # 通过con连接得到游标（执行sql语句的地方）
    cursor = con.cursor()
    # 准备一条sql语句
    sql = "select * from bank"
    cursor.execute(sql)
    # 查询，从游标里提取数据
    data = cursor.fetchall()
    # 账号存在
    for c in data:
        if c[0] == in_account:
            for d in data:
                if d[0] == out_account:
                    password = input("请输入密码：")
                    if d[2] == password:
                        money = int(input("请输入金额："))
                        if money <= int(d[8]):
                            money1 = int(d[8]) - money
                            money2 = int(c[8]) + money
                            update1 = "update bank set 余额='" + str(money1) + "' where 账号=" + out_account
                            update2 = "update bank set 余额='" + str(money2) + "' where 账号=" + in_account
                            cursor.execute(update1)
                            cursor.execute(update2)
                            con.commit()
                            return 0
                        else:
                            return 3
                    else:
                        return 2

    return 1
    cursor.close()
    con.close()


# 转账逻辑
def transfer():
    out_account = input("请输入转出的账号：")
    in_account = input("请输入转入的账号：")

    s = bank_transfer(out_account, in_account)
    if s == 0:
        con = pymysql.connect(host="localhost", user="root", password="root", database="银行数据库")
        # 通过con连接得到游标（执行sql语句的地方）
        cursor = con.cursor()
        # 准备一条sql语句
        sql = "select * from bank"
        cursor.execute(sql)
        # 查询，从游标里提取数据
        data = cursor.fetchall()
        # 账号存在
        for c in data:
            if c[0] == in_account:
                for d in data:
                    if d[0] == out_account:
                        print("转账成功")
                        print("转出账号剩余：", d[8])
                        print("转入账号剩余：", c[8])
        cursor.close()
        con.close()
    elif s == 1:
        print("转出或转入账号不存在")
    elif s == 2:
        print("密码不正确")
    elif s == 3:
        print("金额不足")


# 银行的查询逻辑
def bank_inquire(account):
    con = pymysql.connect(host="localhost", user="root", password="root", database="银行数据库")
    # 通过con连接得到游标（执行sql语句的地方）
    cursor = con.cursor()
    # 准备一条sql语句
    sql = "select * from bank"
    cursor.execute(sql)
    # 查询，从游标里提取数据
    data = cursor.fetchall()
    # 账号存在
    i = 0
    for c in data:
        if c[0] == account:
            i = i + 1
            password = input("请输入密码：")
            if password == c[2]:
                print("前账号：", account)
                print("密码：******")
                print("余额：", c[8])
                print("用户居住地址：", c[3], c[4], c[5], c[6])
                print("当前账户的开户行：", c[7])
            else:
                print("密码不正确")
    if i == 0:
        print("账户不存在")
    cursor.close()
    con.close()


# 查询逻辑
def inquire():
    account = input("请输入账号")
    bank_inquire(account)


while True:  # 一直循环的进入选项
    print(info)
    chose = input("请输入您的选项：")
    if chose == "1":  # 判断是否是1
        adduser()  # 开户
    elif chose == "2":  # 判断是否是2
        deposit()
    elif chose == "3":  # 判断是否是3
        withdraw()
    elif chose == "4":  # 判断输入的是否是4
        transfer()
    elif chose == "5":  # 判断输入的是否是5
        inquire()
    elif chose == "6":  # 判断输入的是否是6，若是6则需要退出 break
        print("拜拜了您嘞！")
        break
    else:
        print("输入非法！重新输入！")
