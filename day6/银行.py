import random
import pymysql

check_sql = 'select name from user_table where BINARY name =%s '
register_sql = 'insert into user_table(account,password) values(%s,%s)'
bank = {}
bank_name = "中国工商银行昌平区回龙观支行"
info = '''
    ********************************
    *    中国工商银行账户管理系统       *
    ********************************
    *    1、开户                    *
    *    2、存钱                    *
    *    3、取钱                    *
    *    4、转账                    *
    *    5、查询                    *
    *    6、Bye!                    *
    ********************************

    '''


# 银行的开户逻辑

def bank_addUser(account, username, password, country, province, street, door, money):
    # 判断用户库是否已满

    # 判断是否存在
    # 获取所有键，然后在判断是否有
    conn = pymysql.connect(host="localhost", user="root", password="root", database="银行数据库", charset="utf8")
    cur = conn.cursor()
    sql = "select * from user_table"
    param = []
    cur.execute(sql)
    data = cur.fetchall()
    for d in data:
        if d[0] == account:
            return 2

    else:

        conn = pymysql.connect(host="localhost", user="root", password="root", database="银行数据库", charset="utf8")
        cur = conn.cursor()
        sql = 'insert into user_table(account, username, password, country, province, street, door, money) values(%s, %s,%s, %s, %s, %s, %s, %s) '
        cur.execute(sql, (account, username, password, country, province, street, door, money))
        conn.commit()
        cur.close()
        conn.close()
        return 1


# 开户逻辑
def addUser():
    # 生成账号：  8位随机

    string = ""  # 随机数缓冲
    for i in range(8):  # 循环8次取字符

        string = string + "1234567890"[random.randint(0, 9)]  # 拼接

    account = string
    print("账号为：", account)
    username = input("请输入姓名：")
    password = int(input("请输入密码："))
    print("接下来输入地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street = input("\t输入街道：")
    door = input("\t输入门牌号：")
    money = int(input("请初始化您的余额："))

    a = 0
    a = bank_addUser(account, username, password, country, province, street, door, money)
    if a == 1:
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

    elif a == 2:
        print("该用户已存在！")


# 调用银行的开户方法


#############################################################################

# 存款逻辑
def addMoney():
    conn = pymysql.connect(host="localhost", user="root", password="root", database="银行数据库", charset="utf8")
    cur = conn.cursor()
    money_account = input('请输入账户：')

    a = bank_addMoney(money_account)
    if a == 1:
        add_money = int(input('请输入存入金额:'))
        sql = 'UPDATE user_table SET money = money + %s WHERE account = %s'
        cur.execute(sql, (add_money, money_account))
        conn.commit()
        cur.close()
        conn.close()
        print('已添加:', add_money, "元")
    else:
        print('此账户不存在')
        conn.commit()
        cur.close()
        conn.close()


def bank_addMoney(money_account):
    conn = pymysql.connect(host="localhost", user="root", password="root", database="银行数据库", charset="utf8")
    cur = conn.cursor()
    sql = "select * from user_table"
    param = []
    cur.execute(sql)
    data = cur.fetchall()
    for d in data:
        if d[0] == money_account:
            return True
        else:
            return False


#############################################################################
# 取钱逻辑
def takemoney():
    while True:

        account = input("请输入您的账号：")
        password = input("请输入密码：")
        take = int(input("请输入您要取得金额："))

        a = bank_takemoney(account, password, take)
        if a == 1:
            print("账号不存在")
            conn.commit()
            cur.close()
            conn.close()
        elif a == 2:
            print("密码错误")
            conn.commit()
            cur.close()
            conn.close()
        elif a == 3:
            print("钱不够")
            conn.commit()
            cur.close()
            conn.close()
        elif a == 0:

            take = bank[account]["money"] - take
            print("取钱成功！您的余额为：", take)
            bank[account]['money'] = take
            conn.commit()
            cur.close()
            conn.close()
            break


# 银行的取款逻辑
def bank_takemoney(account, password, take):
    conn = pymysql.connect(host="localhost", user="root", password="root", database="银行数据库", charset="utf8")
    cur = conn.cursor()
    sql = "select * from user_table"
    cur.execute(sql)
    data = cur.fetchall()
    for d in data:
        if d not in data:
            return 1


def bank_Transfer(in_account, out_account, out_pause, out_money):
    keys = bank.keys()
    if in_account and out_account not in keys:
        return 1
    elif bank[out_account]["password"] != out_pause:
        return 2
    elif bank[out_account]["money"] < out_money:
        return 3
    else:
        return 0


def Transfer():
    out_account = input('请输入转出账户：')
    in_account = input('请输入转入账户：')
    out_pause = input('请输入转出账户密码：')
    out_money = int(input('请输入转出金额：'))
    a = bank_Transfer(in_account, out_account, out_pause, out_money)
    if a == 1:
        print('账户错误')
    elif a == 2:
        print('密码错误')
    elif a == 3:
        print('余额不足')
    elif a == 0:
        bank[out_account]["money"] -= out_money
        bank[in_account]["money"] += out_money
        print('转出账户余额', bank[out_account]["money"])
        print('转入账户余额', bank[in_account]["money"])


# 查询的逻辑
def inquire():
    while True:
        account = input("请输入您的账号：")
        password = input("请输入密码：")
        if account in bank:
            if password == bank[account]['password']:
                print("您的姓名为：", bank[account]["username"],
                      "您的密码为：", bank[account]["password"],
                      "国家：", bank[account]["country"],
                      "省份：", bank[account]["province"],
                      "街道：", bank[account]["street"],
                      "门牌号：", bank[account]["door"],
                      "您的余额为：", bank[account]["money"],
                      "开户行：", bank[account]["bank_name"])
                break
            else:
                print("密码错误！")
        else:
            print("您的账号不存在！")


#############################################################################

# 入口
while True:  # 一直循环的进入选项
    print(info)
    chose = input("请输入您的选项：")
    if chose == "1":  # 判断是否是1
        addUser()
    elif chose == "2":  # 判断是否是2
        addMoney()
    elif chose == "3":  # 判断是否是3
        takemoney()
    elif chose == "4":  # 判断输入的是否是4
        Transfer()
    elif chose == "5":  # 判断输入的是否是5
        inquire()
    elif chose == "6":  # 判断输入的是否是6，若是6则需要退出 break
        print("拜拜了您嘞！")
        break
    else:
        print("输入非法！重新输入！")
