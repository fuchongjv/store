count = 0
user = 'root'
password = 'admin'

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
