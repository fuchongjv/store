# 人类：
# 属性:
# 姓名，性别，年龄，话费，品牌，电池，屏幕，待机时长，积分。
# 功能：
num1 = [1, 2, 3, 4, 5]


class People:
    __name = ""
    __sex = ""
    __age = 0
    __bill = 0
    __brand = ""
    __battery = ""
    __screen = ""
    __standbyTime = ""
    __points = 0

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setBill(self, bill):
        self.__name = bill

    def getBill(self):
        return self.__bill

    def SMS(self, sms):
        print("您的输入的内容为：", sms)

    def call(self, time, num):
        if self.__bill < 1 or num not in num1:
            print("错误")
        elif time < 10:
            return 1 * time
        elif time > 10 & time < 20:
            return 0.8 * time
        else:
            return 0.65 * time


p = People()
p.setName(1)
p.setBill(21)
sms = input("您要发送的信息为：")
p.SMS(sms)
p.call(1,1)
